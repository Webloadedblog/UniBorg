from telethon import events
import random
import string
import requests
from random import randint 
from uniborg.util import admin_cmd
  
@borg.on(pattern="enaclk ?(.*)", outgoing=True)
async def enaclk(event):
    await event.edit("K...")
    @borg.on(pattern="http") incoming=True, func=lambda e: e.is_private)
    async def clkstart(m):
        person = await m.get_sender()
        user=person.firstpattern="download ?(.*)_name
        rantext = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
        api_token = '32f9105a8194b5596482f0ed9631ab1483ec171e'
        req = requests.get('https://ilinkshort.com/api?api={}&url={}&alias={}'.format(api_token, m.text, rantext)).json()
        if(req["status"] == 'error'):
          smsg = req["message"]
        else:
          smsg = req["shortenedUrl"]
      
        sent = await m.reply(smsg)
    await event.edit("Done...")
