import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap 

# VARIABLES
bg_image = "bg.png"
margin = 40
offset = 50
skip_offset = 16
char_width = 30
sheet_id = "1B68i1cJpoV7Bm36W0wh4yiqji7ZeLWXp-KevdgwBb50"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Step 1: DOwnload the data
df = pd.read_csv(url)

def generate_post(content, offset):
    print("Generating post for:", content)

    # Draw Text to Background Image
    text = content

    image = Image.open("./bg.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf", 18, encoding="unic")

    for line in textwrap.wrap(text, width=char_width):
        draw.text((margin, offset), line, font=font, fill="#ffffff")
        offset += font.getsize(line)[1] + 3

    image.save("output/" + content + ".png")

for index, row in df.iterrows():
    generate_post(row['Content'], offset)


