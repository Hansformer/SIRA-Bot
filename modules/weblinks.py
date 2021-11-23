import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_str_slash_option('resource', 'The resource you wan to fetch',
                              choices={
                                  'SIRA Website': 'website',
                                  'SIRA Lore/History': 'lore',
                                  'Inara Squadron Page': 'inara',
                                  'Bot help': 'help',
                                  'Space IRA': 'spaceira',
                                  'Territory Reference': 'territory',
                                  'Mining Reference': 'mining',
                                  'BGS Information': 'bgs'
                              })
@tanjun.as_slash_command('link', "Fetch a link to one of SIRA's resources.")
async def weblinks(ctx: tanjun.abc.Context, resource: str) -> None:
    msg = None

    if resource == 'website':
        msg = ':globe_with_meridians: **SIRA Website**: https://sira.space/'
    elif resource == 'lore':
        msg = ':book: **SIRA History/Lore**: <https://sira.space/?page=lore>'
    elif resource == 'inara':
        msg = '<:space_ireland:309204831548211201> **INARA Squadron Page**: <https://inara.cz/squadron/1470/>'
    elif resource == 'help':  # TODO: Make help command instead of this
        msg = ':robot: **SIRA-Bot Help**: <https://github.com/Hansformer/SIRA-Bot#helpcommands>'
    elif resource == 'spaceira':
        msg = 'https://www.youtube.com/watch?v=5h7UPVOz6MU'
    elif resource == 'territory':
        msg = '<:space_ireland:309204831548211201> **SIRA Territory Reference**: ' \
              '<https://inara.cz/squadron-documents/1470/517/>'
    elif resource == 'mining':
        msg = ':pick: **SIRA Mining Reference**: <https://inara.cz/squadron-documents/1470/864/>'
    elif resource == 'bgs':
        msg = ':bar_chart: **BGS Information**: ' \
              '<https://forums.frontier.co.uk/showthread.php/400110-Don-t-Panic-BGS-guides-and-help>'

    if msg:
        await ctx.respond(msg)


loader = component.make_loader()
