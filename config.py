import ujson as json

data = 0

def init():
  try:
    with open('data.json', 'r') as f:
      data = json.load(f)
  except:
    print('JSON file is loaded successfully.')

def save():
  try:
    with open('data.json', 'w') as f:
      data = json.load(f)
  except:
    print('JSON data is write successfully.')