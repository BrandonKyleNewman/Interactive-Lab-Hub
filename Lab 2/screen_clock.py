import time
import subprocess
import digitalio
import board
import random
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
font_2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    # Draw a black filled box to clear the image.
    # draw.rectangle((0, 0, width, height), outline=0, fill=0)
    y = top
    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    if str(time.localtime().tm_mon) in ["3","4","5"]:
        current_season = "Spring"
        random_sayings = ["It's sprung,", "Smell a flower,", "Grab an umbrella,"]
        season_image = Image.open('spring-1.png').convert('RGBA')
    elif str(time.localtime().tm_mon) in ["6","7","8"]:
        current_season = "Summer"
        random_sayings = ["Get some rays,", "Suns out, guns out,", "Wear sunscreen,"]
        season_image = Image.open('summer-1.png').convert('RGBA')
    elif str(time.localtime().tm_mon) in ["9","10","11"]:
        current_season = "Autumn"
        random_sayings = ["Crunchy leaves,", "Pumpkin spice me,", "Grab a coat,"]
        season_image = Image.open('autumn-1.png').convert('RGBA')
    else:
        current_season = "Winter"
        random_sayings = ["It's a wonderland,", "Build a snowman,", "Does it snow in Cali,"]
        season_image = Image.open('winter-1.png').convert('RGBA')
       
    draw = ImageDraw.Draw(season_image)
    current_hour = time.localtime().tm_hour % 12
    if current_hour == 0:
        current_hour = 12
            
    draw.text((x,y), "It's, uh, " + current_season, font=font, flush=True, fill="#5E1560")
    y += 24
    draw.text((x,y), "and about " + str(current_hour) + "ish", font=font, flush=True, fill="#5E1560")
    y += 48
    draw.text((x+100,y), random.choice(random_sayings), font=font_2, flush=True, fill="#5E1560")
    y += 12
    draw.text((x+100,y), random.choice(["dude","bro","brother","my man", "my guy"]), font=font_2, fill="#5E1560")
    # Display image.
    disp.image(season_image, rotation)
    time.sleep(600)
