#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from IT8951 import constants
import json
import requests

def pocasi():

    #url = "https://example.com/pocasi.json"
    #response = requests.get(url)
    #pocasi = json.loads(response.text)
    pocasi = json.loads(open('pocasi.json', 'r').read())

    from IT8951.display import AutoEPDDisplay

    display = AutoEPDDisplay(vcom=-2.06)

    image = Image.new('L', (display.width, display.height), 1)   
    draw = ImageDraw.Draw(image)

    fontdir = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/'
    big_font = ImageFont.truetype(fontdir + 'Roboto-Regular.ttf', 250)
    small_font = ImageFont.truetype(fontdir + 'Roboto-Bold.ttf', 30)

    draw.rectangle((0, 0, 1200, 825), fill = 0)
    draw.text((50, 20), "Venkovní teplota [°C]:", font = small_font, fill = 255)
    draw.text((650, 20), "Vnitřní teplota [°C]:", font = small_font, fill = 255)

    draw.text((50, 80), str(pocasi["teplota"]), font = big_font, fill = 255)
    draw.text((650, 80), str(pocasi["ds18b20"]), font = big_font, fill = 255)

    draw.text((50, 410), "Zdánlivá teplota: " + str(pocasi["zdanlivateplota"]) + " °C", font = small_font, fill = 255)
    draw.text((50, 480), "Rosný bod: " + str(pocasi["rosnybod"]) + " °C", font = small_font, fill = 255)
    draw.text((50, 550), "Vlhkost vzduchu: " + str(pocasi["vlhkost"]) + " %", font = small_font, fill = 255)
    draw.text((50, 630), "Srážky: " + str(pocasi["srazky"]) + " mm/den", font = small_font, fill = 255)

    draw.text((650, 410), "Osvit: " + str(pocasi["osvit"]) + " W/m2", font = small_font, fill = 255)
    draw.text((650, 480), "Tlak: " + str(pocasi["tlak"]) + " hPa", font = small_font, fill = 255)
    draw.text((650, 550), "Vítr: " + str(pocasi["rychlostvetru"]) + " m/s, směr: " + pocasi["smervetru"], font = small_font, fill = 255)
    draw.text((650, 630), "Nárazový vítr: " + str(pocasi["narazovyvitr"]) + " m/s", font = small_font, fill = 255)

    draw.text((870, 775), pocasi["zmereno"], font = small_font, fill = 255)

    color = 0x10
    display.frame_buf.paste(color, box=image)

    display.draw_full(constants.DisplayModes.GC16)

pocasi()
