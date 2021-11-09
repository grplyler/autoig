from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import textwrap
import matplotlib.font_manager

def calc_char_width(isize, fsize):
    return (int((isize*.9))/fsize)*2

def get_system_fonts():
    fonts = matplotlib.font_manager.findSystemFonts()
    return fonts

def generate_post(text, opts):
    print("Generating post for:", text)

    # Draw Text to Background Image
    image = Image.open(opts.background)
    image = image.resize((1024, 1024))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(opts.font, opts.font_size, encoding="unic")

    for line in textwrap.wrap(text, width=opts.char_width):
        draw.text((opts.margin, opts.offset), line, font=font, fill=opts.color)
        opts.offset += font.getsize(line)[1] + 3

    text = text.replace(' ', '_')
    image.save("output/" + text + ".png")


def fmt_link(sheet_id):
    sheet_name = "Sheet1"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return url

def fetch_sheet(sheet_id):
    url = fmt_link(sheet_id)
    print("Downloading Spreadsheet:", url)
    df = pd.read_csv(url)
    print("Done.")
    return df