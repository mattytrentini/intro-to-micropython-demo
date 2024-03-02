# Intro to MicroPython: Demo

An async-webserver to scroll your messages!

Designed to run on the M5Stack Atom Matrix with a connected LED matrix display.

This demo will run a small webserver that will allow messages to be queued for
display on the connected LED display (an 8x 8x8 MAX7219-powered device). The
depth of the queue will be indicated by the number of lit NeoPixels on the
Atom's Matrix. Because the system is asyncio-based, a connection can be made via
the aiorepl to interact with the system _live_.

## Installation

### Dependencies

* aiorepl
* MAX7219 driver
* microdot (including the utemplate extension)
* utemplate

Since this is a demo, the easiest way to install these dependencies is with mip
using mpremote:

```bash
> mpremote mip install aiorepl
> mpremote mip install github:mattytrentini/micropython-max7219/max7219.py
> mpremote mip install --target /lib/microdot github:miguelgrinberg/microdot/src/microdot/microdot.py
> mpremote mip install --target /lib/microdot github:miguelgrinberg/microdot/src/microdot/utemplate.py
> mpremote mip install --target /lib/microdot github:miguelgrinberg/microdot/src/microdot/__init__.py
> mpremote mip install --target /lib/utemplate github:falcon/utemplate/utemplate/compiled.py
> mpremote mip install --target /lib/utemplate github:falcon/utemplate/utemplate/source.py
> mpremote mip install --target /lib/utemplate github:falcon/utemplate/utemplate/recompile.py
```

If this were to be used in production it would be more appropriate to freeze
these dependencies after adding them to this repository via a git submodule.
