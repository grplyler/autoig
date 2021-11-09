import click
from autoig.utils import fetch_sheet
from autoig.utils import generate_post
from autoig.utils import get_system_fonts
from autoig import utils
from autoig.config import Options

@click.group()
def cli():
    pass

@cli.command()
@click.option('-b', '--background', help="Background Image", default="./bg.png")
@click.option('-f', '--font', help="System Font Name", default="/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf")
@click.option('-i', '--id', help="Google Sheet ID")
@click.option('-c', '--color', help="Text Color", default="#FFFFFF")
@click.option('-s', '--size', help="Font size", type=int, default=40)
def single(background, font, id, color, size):
    df = fetch_sheet(id)
    
    # Create Default Options
    opts = Options()
    opts.font = font
    opts.color = color
    opts.background = background
    opts.font_size = size

    # Calculate char_width (image is 1024*1024)
    opts.char_width = utils.calc_char_width(1024, opts.font_size)
    print("char width:", opts.char_width)


    for index, row in df.iterrows():
        generate_post(row['Content'], opts)
        exit(0)

@cli.command('fonts')
def fonts():
    fonts = get_system_fonts()
    for font in fonts:
        print(font)