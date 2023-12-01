import network
import socket
import uasyncio

wlan = network.WLAN(network.STA_IF)

command_queue = []
result_queue = []

def result():
  return result_queue.pop(0)

async def run_connect(ssid, password):
  wlan.active(True)
  wlan.config(pm = 0xa11140)
  wlan.connect(ssid, password)

  max_wait = 10
  while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
      break

    max_wait -= 1
    print('waiting for connection...')
    await uasyncio.sleep(1)

  if wlan.status() != 3:
    print('connect fail')
    result_queue.append(False)
  else:
    print('connected')
    result_queue.append(True)

async def run_tcp(host, port):
  test = 1



async def run():
  functions = {
    'connect': run_connect
  }

  while True:
    if len(command_queue) == 0:
      continue
    
    command = command_queue.pop(0)
    await functions[command['name']](*command['args'])
    