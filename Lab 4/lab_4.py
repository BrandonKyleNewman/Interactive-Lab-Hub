import time
import subprocess
import digitalio
import board
import random
import evolution_image_set
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Setup APDS board
i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_color = True

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

EVOLUTION_MAX = 3
LUX_STEP = 10000

evolution_state = 0
total_lux_val = 0
image_count = 0

while True:
    if total_lux_val >= (evolution_state+1)*LUX_STEP:
        evolution_state += 1
        #evolve
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        disp.image(image, rotation)
        draw.text((x,y), "evolution time!", font=font_2, flush=True, fill="#FFFFFF")
        time.sleep(7)
        
    if evolution_state == EVOLUTION_MAX:
        text_str = "Press any button to play again"
    else:
        r, g, b, c = apds.color_data
        curr_lux = colorutility.calculate_lux(r, g, b)
        total_lux_val += curr_lux
        text_str = str(total_lux_val)
        
    curr_image_str = evolution_image_set.evolution_image_set[evolution_state][image_count%4]
    curr_image = Image.open(curr_image_str).convert('RGBA')
    
    y = top
    
    draw = ImageDraw.Draw(curr_image)
    draw.text((x,y), text_str, font=font, flush=True, fill="#5E1560")
            
    disp.image(curr_image, rotation)
    image_count += 1
    time.sleep(1)