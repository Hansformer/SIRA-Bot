import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_str_slash_option('image', 'The image you want to see',
                              choices={
                                  'SIRA Flag': 'flag',
                                  'SIRA Battleflag': 'battleflag',
                                  'SIRA Logo': 'logo',
                                  'Bhadaba!': 'bhadaba',
                                  '>ASP': 'asp',
                                  'Landmine': 'landmine',
                                  'What is a skimmer?': 'skimmer',
                                  'Stay safe everyone': 'staysafe',
                                  'Conquest': 'conquest',
                                  'Aisling': 'aisling',
                                  'Biowaste': 'biowaste',
                                  'Parnut': 'parnut',
                                  'GymBoss': 'gymboss',
                                  'So Good': 'sogood',
                                  'Believable': 'believable',
                              })
@tanjun.as_slash_command('image', "Fetch some of SIRA's finest art.")
async def images(ctx: tanjun.abc.Context, image: str) -> None:
    # TODO: This seems dumb, why are we not just hosting the images and linking them?
    # SlashContext has no attachment property so we have to edit the response to add one
    await ctx.respond('One spicy image coming right up!')
    image_paths = {
        'flag': 'images/flag_of_space_ireland.png',
        'battleflag': 'images/battleflag.png',
        'logo': 'images/sira_logo.png',
        'bhadaba': 'images/images/Bhadaba.jpg',
        'asp': 'images/ASP.png',
        'landmine': 'images/landmines.jpg',
        'skimmer': 'images/what_is_a_skimmer.png',
        'staysafe': 'images/stay_safe_everyone.jpg',
        'conquest': 'images/achievement_meme.png',
        'aisling': 'images/aisling.jpg',
        'biowaste': 'images/brabowaste.png',
        'parnut': 'images/parnut.png',
        'gymboss': 'images/gym_boss.png',
        'sogood': 'images/so_good.png',
        'believable': 'images/believable.jpg'
    }
    await ctx.edit_initial_response(attachment=image_paths[image])


loader = component.make_loader()
