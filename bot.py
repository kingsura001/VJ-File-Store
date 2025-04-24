from pyrogram import Client
from pyrogram import idle
import logging
import asyncio
from config import *

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

app = Client(
    "FileStoreBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=BOT_WORKERS,
    plugins=dict(root="plugins"),
)

async def main():
    await app.start()
    print(f"Bot Started Powered By @{OWNER_USERNAME}")
    await idle()

    await app.stop()
    print("Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())
