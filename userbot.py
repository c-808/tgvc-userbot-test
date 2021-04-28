from pyrogram import Client, idle

api_id = 2088606
api_hash = "02423b23b1c16d7d0c0ec86a3ac07108"

plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "vc.restrim",
        "ping",
        "sysinfo"
    ]
)

app = Client("tgvc", api_id, api_hash, plugins=plugins)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
