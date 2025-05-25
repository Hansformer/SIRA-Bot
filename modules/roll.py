import random
import re
from typing import List, Tuple, Dict, Optional

import tanjun

component = tanjun.Component()


def roll_exploding(die_size: int, num_dice: int) -> List[List[int]]:
    if die_size <= 0:
        return []
    if num_dice <= 0:
        return []

    rolls = []
    for _ in range(num_dice):
        subtotal = []
        r = random.randint(1, die_size)
        subtotal.append(r)
        while r == die_size:
            r = random.randint(1, die_size)
            subtotal.append(r)
        rolls.append(subtotal)
    return rolls


def flatten(rolls: List[List[int]]) -> List[int]:
    return [item for sublist in rolls for item in sublist]


def count_bust(rolls: List[List[int]]) -> bool:
    flat = flatten(rolls)
    return flat.count(1) > len(flat) // 2


def parse_roll_command(command: str) -> Tuple[List[Dict[str, int]], Optional[int], Optional[int]]:
    dice_pattern = r"(\d+)d(\d+)([+-]\d+)?"
    tn_pattern = r"(?:TN|tn)\s*(\d+)"
    size_pattern = r"(?:Sz|Size)\s*(\d+)"

    dice_parts = re.findall(dice_pattern, command)
    tn_match = re.search(tn_pattern, command)
    sz_match = re.search(size_pattern, command)

    tn = int(tn_match.group(1)) if tn_match else None
    size = int(sz_match.group(1)) if sz_match else None
    rolls = []
    for part in dice_parts:
        num, sides = int(part[0]), int(part[1])
        mod = 0
        if part[2]:
            mod = int(part[2])
        rolls.append({"num": num, "sides": sides, "mod": mod})

    return rolls, tn, size


def format_rolls(rolls: List[List[int]]) -> str:
    formatted = []
    for r in rolls:
        if len(r) == 1:
            formatted.append(str(r[0]))
        else:
            exploded = "+".join(str(d) for d in r)
            formatted.append(f"[{exploded}]")
    return ", ".join(formatted)


@component.with_slash_command
@tanjun.with_str_slash_option("command", "Dice roll format like 2d6+2 TN 7 or 3d6 Size 5")
@tanjun.as_slash_command("roll", "Roll dice for Trait, TN, or Hurtin'")
async def roll(ctx: tanjun.abc.Context, command: str) -> None:
    rolls, tn, size = parse_roll_command(command)
    if not rolls:
        await ctx.respond("No valid dice found in command. Try formats like '2d6', '3d8+2', etc.")
        return

    for roll_info in rolls:
        if roll_info["sides"] <= 0:
            await ctx.respond(f"Invalid die size: {roll_info['sides']}. Die size must be a positive number.")
            return
        if roll_info["num"] <= 0:
            await ctx.respond(f"Invalid number of dice: {roll_info['num']}. Number must be a positive number.")
            return

    # Determine roll type
    trait_roll = rolls[0] if rolls else None
    hurtin_roll = rolls[1] if size and len(rolls) > 1 else (rolls[0] if size else None)
    result_msg = ""
    trait_total = 0

    # --- Trait Roll ---
    if trait_roll is not None:
        trait_results = roll_exploding(trait_roll["sides"], trait_roll["num"])
        flat_trait = flatten(trait_results)
        if flat_trait:  # Check if flat_trait is not empty
            mod_trait = trait_roll["mod"]
            trait_total = max(flat_trait) + mod_trait
            result_msg += (
                f"**Trait Roll:** {trait_roll['num']}d{trait_roll['sides']}"
                f" {('+' if mod_trait >= 0 else '') + str(mod_trait)}\n"
            )

            result_msg += (
                f"Results: {format_rolls(trait_results)}  → Max: {max(flat_trait)}"
                f"{f' + {mod_trait}' if mod_trait != 0 else ''} = **{trait_total}**\n"
            )

            if count_bust(trait_results):
                result_msg += "**Gone Bust!** 🎲💥\n"
                await ctx.respond(result_msg)
                return
            # Target Number Check
            if tn:
                success = trait_total >= tn
                raises = (trait_total - tn) // 5 if success else 0
                result_msg += f"**Target Number:** {tn} → {'✅ Success' if success else '❌ Failure'}"
                if success and raises > 0:
                    result_msg += f" with {raises} Raise{'s' if raises != 1 else ''}!"
                result_msg += "\n"
        else:
            result_msg += "No valid dice rolls were made\n"

    # --- Hurtin' Roll ---
    if size is not None and hurtin_roll is not None:
        hurtin_results = roll_exploding(hurtin_roll["sides"], hurtin_roll["num"])
        flat_hurtin = flatten(hurtin_results)
        if flat_hurtin:  # Check if flat_hurtin is not empty
            mod_hurtin = hurtin_roll["mod"]
            total = sum(flat_hurtin) + mod_hurtin
            # Add Trait roll if combo
            if trait_roll and len(rolls) > 1:
                total += trait_total
            wounds = total // size
            result_msg += (
                f"\n**Hurtin' Roll:** {hurtin_roll['num']}d{hurtin_roll['sides']}"
                f" {('+' if mod_hurtin >= 0 else '') + str(mod_hurtin)}"
            )

            if trait_roll and len(rolls) > 1:
                result_msg += f" + Trait Result ({trait_total})"

            result_msg += f"\nResults: {format_rolls(hurtin_results)} → Total: {total} → **Wounds: {wounds}**"
            if wounds > 0:
                result_msg += f" {'💀' * min(wounds, 5)}"
            result_msg += "\n"
        else:
            result_msg += "No valid Hurtin' rolls were made\n"

    await ctx.respond(result_msg)


loader = component.make_loader()
