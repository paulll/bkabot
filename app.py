import logging

from src.client import client
import src.io.tg.input

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

client.parse_mode = 'html'
client.run_until_disconnected()
