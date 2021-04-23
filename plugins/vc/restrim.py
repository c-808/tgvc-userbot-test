import asyncio
import os
from typing import Optional

from pytgcalls import GroupCallRaw
import pyrogram

# EDIT VALUES!
PEER_ID = -1001239894073    # chat or channel where you want to get audio
PEER_ID2 = -1001225640227    # chat or channel where you want to play audio

# global variable to transfer audio data between voice chats
# it's not a good implementation, but its works and so easy to understand
LAST_RECORDED_DATA = None


def on_played_data(gc: GroupCallRaw, length: int) -> Optional[bytes]:
    return LAST_RECORDED_DATA


def on_recorded_data(gc: GroupCallRaw, data: bytes, length: int) -> None:
    global LAST_RECORDED_DATA
    LAST_RECORDED_DATA = data


async def main(client):
    await client.start()
    while not client.is_connected:
        await asyncio.sleep(1)

    # handle input audio data from the first peer
    group_call_from = GroupCallRaw(client, on_recorded_data=on_recorded_data)
    await group_call_from.start(PEER_ID)
    # transfer input audio from the first peer to the second using handlers
    group_call_to = GroupCallRaw(client, on_played_data=on_played_data)
    await group_call_to.start(PEER_ID2)

    await pyrogram.idle()


if __name__ == '__main__':
    pyro_client = pyrogram.Client(
        os.environ.get('SESSION_NAME', 'pytgcalls'),
        api_hash=os.environ.get('API_HASH', API_HASH),
        api_id=os.environ.get('API_ID', API_ID)
    )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(pyro_client))
