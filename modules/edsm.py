import pendulum
import tanjun

from sirabot.utils import fetch

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_str_slash_option('system', 'The system name')
@tanjun.as_slash_command('sysinf', 'System info for a given system.')
async def system_inf(ctx: tanjun.abc.Context, system: str) -> None:
    api = await fetch(
        f'https://www.edsm.net/api-system-v1/factions?systemName={system}')
    if api:
        text = f"```{api['name']} Influence Overview```"
        for faction in api['factions']:
            if faction['influence'] != 0:
                text += await process_faction_inf(api, faction)

        text += pendulum.from_timestamp(api['factions'][0]
                                        ['lastUpdate']).to_rfc2822_string()
        await ctx.respond(text)
    else:
        await ctx.respond("I can't find that, senpai.")


async def process_faction_inf(api: dict, faction: dict) -> str:
    text = f"{':crown: ' if api['controllingFaction']['id'] == faction['id'] else ''}**{faction['name']}**"

    if faction['isPlayer']:
        text += await get_player_faction_indicator(faction)

    text += f""": {faction['influence']:.1%}{f" ({faction['state']})" if faction['state'] != 'None' else ''}\n"""

    if faction['pendingStates']:
        text += ':fast_forward: __Pending__:'
        for pending_state in faction['pendingStates']:
            text += f" {pending_state['state']} "
            if pending_state['trend'] >= 1:
                text += ':small_red_triangle:'
            elif pending_state['trend'] == 0:
                text += '(-)'
            else:
                text += ':small_red_triangle_down:'
            text += ';'
        text += '\n'

    if faction['recoveringStates']:
        text += ':twisted_rightwards_arrows: __Recovering__:'
        for recovering_state in faction['recoveringStates']:
            text += f" {recovering_state['state']} "
            if recovering_state['trend'] >= 1:
                text += ':small_red_triangle:'
            elif recovering_state['trend'] == 0:
                text += '(-)'
            else:
                text += ':small_red_triangle_down:'
            text += ';'
        text += '\n'

    text += f":classical_building: `{faction['allegiance']}, " \
            f"{faction['government']}`\n" \
            '---\n'

    return text


async def get_player_faction_indicator(faction):
    sira_name = 'SIRA Incorporated'
    ally_names = ['Iridium Wing', 'CROSS Corp', 'Pan Galactic Mining Corp.',
                  'Sirius Special Forces', 'Wrecking Crew', 'Aseveljet']
    enemy_names = ['EXO', 'The Fatherhood']

    if faction['name'] == sira_name:
        indicator = ' <:space_ireland:309204831548211201> '
    elif faction['name'] in ally_names:
        indicator = ' :green_heart: '
    elif faction['name'] in enemy_names:
        indicator = ' :skull: '
    else:
        indicator = ' :joystick: '

    return indicator


@component.with_slash_command
@tanjun.with_str_slash_option('system', 'The system name')
@tanjun.as_slash_command('traffic', 'Traffic report for a system.')
async def traffic_report(ctx: tanjun.abc.Context, system: str) -> None:
    api = await fetch(
        f'https://www.edsm.net/api-system-v1/traffic?systemName={system}')

    if api:
        traffic = api['traffic']
        text = f"```{api['name']} EDSM Traffic Report```" \
               f"Last 24 Hours: {traffic['day']}\n" \
               f"Last 7 Days: {traffic['week']}\n" \
               f"All Time: {traffic['total']}"
        # for ship in api['breakdown']:
        #    text += ship
        await ctx.respond(text)
    else:
        await ctx.respond("I can't find that, senpai.")


loader = component.make_loader()
