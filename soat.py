from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
from PIL import Image, ImageDraw, ImageFont
import textwrap
api_id = 967719 #my.telegram.org dan olgan apiidni qoying
api_hash = "ebf9b0ec85bde576ae2339974a5cdc41" #my.telegram.org dan olgan apihash ni qoying
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone("Asia/Tashkent")
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    app.send(functions.account.UpdateProfile(
    first_name=str(x),
    about="O'zbekistonda soat: " +str(x)
    ))
    photos = app.get_profile_photos("me")
    app.delete_profile_photos(photos[0].file_id)
    im = Image.open("background.jpg")
    MAX_W, MAX_H = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('for.ttf', 500)
    w, h = draw.textsize(x, font=font)
    draw.text(((MAX_W - w) / 2, (MAX_H - h) / 2),str(x),(255,255,255),font=font)
    im.save('test.png')
    app.set_profile_photo("test.png")
    time.sleep(10)
