import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_str_slash_option('image', 'The image you want to see',
                              choices=[
                                  ('SIRA Flag', 'flag'),
                                  ('SIRA Battleflag', 'battleflag'),
                                  ('SIRA Logo', 'logo'),
                                  ('Bhadaba!', 'bhadaba'),
                                  ('>ASP', 'asp'),
                                  ('Landmine', 'landmine'),
                                  ('What is a skimmer?', 'skimmer'),
                                  ('Stay safe everyone', 'staysafe'),
                                  ('Conquest', 'conquest'),
                                  ('Aisling', 'aisling'),
                                  ('Biowaste', 'biowaste'),
                                  ('Parnut', 'parnut'),
                                  ('GymBoss', 'gymboss'),
                                  ('So Good', 'sogood'),
                                  ('Believable', 'believable'),
                              ])
@tanjun.as_slash_command('image', "Fetch some of SIRA's finest art.")
async def images(ctx: tanjun.abc.Context, image: str) -> None:
    # TODO: This seems dumb, why are we not just hosting the images and linking them?
    # SlashContext has no attachment property so we have to edit the response to add one
    await ctx.respond('One spicy image coming right up!')
    if image == 'flag':
        await ctx.edit_initial_response(attachment='images/flag_of_space_ireland.png')
    elif image == 'battleflag':
        await ctx.edit_initial_response(attachment='images/battleflag.png')
    elif image == 'logo':
        await ctx.edit_initial_response(attachment='images/sira_logo.png')
    elif image == 'bhadaba':
        await ctx.edit_initial_response(attachment='images/images/Bhadaba.jpg')
    elif image == 'asp':
        await ctx.edit_initial_response(attachment='images/ASP.png')
    elif image == 'landmine':
        await ctx.edit_initial_response(attachment='images/landmines.jpg')
    elif image == 'skimmer':
        await ctx.edit_initial_response(attachment='images/what_is_a_skimmer.png')
    elif image == 'staysafe':
        await ctx.edit_initial_response(attachment='images/stay_safe_everyone.jpg')
    elif image == 'conquest':
        await ctx.edit_initial_response(attachment='images/achievement_meme.png')
    elif image == 'aisling':
        await ctx.edit_initial_response(attachment='images/aisling.jpg')
    elif image == 'biowaste':
        await ctx.edit_initial_response(attachment='images/brabowaste.png')
    elif image == 'parnut':
        await ctx.edit_initial_response(attachment='images/parnut.png')
    elif image == 'gymboss':
        await ctx.edit_initial_response(attachment='images/gym_boss.png')
    elif image == 'sogood':
        await ctx.edit_initial_response(attachment='images/so_good.png')
    elif image == 'believable':
        await ctx.edit_initial_response(attachment='images/believable.jpg')


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
