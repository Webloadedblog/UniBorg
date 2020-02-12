from uniborg.util import admin_cmd
from uniborg import client
from bwb import bwb
import asyncio

bwb = bwb.bwb(client.uid)
wrap_users = {
    's': 504501114,  # Creator of this UserBot 
    't': 79316791,   # Tanner, Creator of BWB
    'j': 172033414,  # Jason
    'o': 358491576,  # Jonas
    'm': 964048273,  # Mini Eule
    'g': 234480941,  # Twit
    'v': 181585055,  # Viktor
}


@borg.on(admin_cmd(pattern='!!+init'), outgoing=True)
async def init(event):
    try:
        await event.respond('000000init ' + bwb.init())
    except:
        pass
