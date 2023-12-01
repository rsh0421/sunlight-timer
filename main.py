import machine
import utime
import uasyncio
import wifi
import bluetooth

test = {'name':1}
print(test['name'])
async def message():
  while True:
    print("hello world!")
    await uasyncio.sleep(1)

async def blink():
  led = machine.Pin("LED", machine.Pin.OUT)
  while True:
    led.toggle()
    await uasyncio.sleep(1)

async def main():
  uasyncio.create_task(blink())
  uasyncio.create_task(message())

  while True:
    await uasyncio.sleep(10)

uasyncio.run(main())