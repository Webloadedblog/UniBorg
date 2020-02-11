from telethon import events

@borg.on(events.NewMessage(pattern="", incoming=True))
async def transfer(event):
    target_channel = -1147697612
    my_channel = -1276100737
    if event.chat_id == target_channel:
        await borg.send_message(my_channel, event.message)
