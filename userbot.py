from pyrogram import Client, idle

api_id = ***
api_hash = "***"

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
