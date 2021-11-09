import click
from autoig.utils import fetch_sheet
from autoig.utils import generate_post
from autoig.utils import get_system_fonts
from autoig.config import Options

@click.group()
def cli():
    pass

@cli.command()
@click.option('-b', '--background', help="Background Image")
@click.option('-f', '--font', help="System Font Name", default="/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf")
@click.option('-i', '--id', help="Google Sheet ID")
@click.option('-c', '--color', help="Text Color")
@click.option('-s', '--size', help="Font size", type=int)
def single(background, font, id, color, size):
    df = fetch_sheet(id)
    
    # Create Default Options
    opts = Options()
    opts.font = font
    opts.color = color
    opts.background = background
    opts.font_size = size
    for index, row in df.iterrows():
        generate_post(row['Content'], opts)
        exit(0)

@cli.command('fonts')
def fonts():
    fonts = get_system_fonts()
    for font in fonts:
        print(font)