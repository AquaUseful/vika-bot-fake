import asyncio
import signal
import sys
import hypercorn
import os
from app import app
try:
    from app import config
except ImportError:
    pass

shutdown_event = asyncio.Event()


@app.after_serving
async def shutdown():
    pass


def signal_handler():
    shutdown_event.set()


hypercorn_cfg = hypercorn.Config()

try:
    hypercorn_cfg.bind = [f"{config.HOST}:{config.PORT}",
                          f"[{config.HOST_IPV6}]:{config.PORT}"]
except NameError:
    hypercorn_cfg.bind = [f"{os.environ['HOST']}:{os.environ['PORT']}",
                          f"[{os.environ['HOST_IPV6']}]:{os.environ['PORT']}"]


loop = asyncio.get_event_loop()
loop.add_signal_handler(signal.SIGINT, signal_handler)
loop.run_until_complete(hypercorn.asyncio.serve(
    app, hypercorn_cfg, shutdown_trigger=shutdown_event.wait))
