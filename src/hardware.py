from machine import SoftSPI, Pin
from micropython import const
from max7219 import Matrix8x8

max_clk = const(33)
max_cs = const(23)
max_din = const(19)

spi = SoftSPI(sck=max_clk, mosi=max_din, miso=14)

display = Matrix8x8(spi, Pin(max_cs), 8)
display.scroll("MicroPython")

from neopixel import NeoPixel
neo = NeoPixel(Pin(27), 25)
neo.fill((0, 0, 0))
neo.write()

def light_neos(count, colour=(0, 10, 0)) -> None:
    neo.fill((0, 0, 0))
    count = min(count, 25)
    for i in range(count):         
        neo[i] = colour
    neo.write()
