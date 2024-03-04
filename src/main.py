from hardware import neo, display, light_neos
import network_setup
import message_queue as mq

## Microdot
from microdot import Microdot, Response
from microdot.utemplate import Template

app = Microdot()
Response.default_content_type = "text/html"

import asyncio
import aiorepl

@app.route("/", methods=["GET", "POST"])
async def display_message(request):
    message = None
    if request.method == "POST":
        message = request.form.get("message")
        mq.add_message(message)
    return Template("index.html").render(message=message)

async def update_led_display() -> None:
    print('Starting display')
    await display.async_scroll("Welcome to Make, Create, Innovate!")
    while True:
        light_neos(mq.message_count())
        if mq.message_count():
            await display.async_scroll(mq.pop_message())
            light_neos(mq.message_count())
        await asyncio.sleep_ms(1_000)

async def start_webserver() -> None:
    print("Web server starting...")
    await app.start_server(port=80, debug=True)

async def main():
    webserver_task = asyncio.create_task(start_webserver())
    display_task = asyncio.create_task(update_led_display())
    repl_task = asyncio.create_task(aiorepl.task())

    await asyncio.gather(webserver_task, display_task, repl_task)


asyncio.run(main())
