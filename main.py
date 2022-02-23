import argparse
import json

from pythonosc import udp_client
from pyhooked import Hook, KeyboardEvent, MouseEvent

OSC_IP = "127.0.0.1"
OSC_PORT = 9000

KEY_LOC = json.load(open('assets/keyLoc.json', 'r'))
KEY_FINGER = json.load(open('assets/keyFinger.json', 'r'))


def main():
  osc_client.send_message("/avatar/parameters/KBDMode", True)

#   send_message(osc_client, "/filter", random.random())

#   for x in range(10):
#     osc_client.send_message("filter", 1.0)
#     time.sleep(1)
#     print("send2")
  hook = Hook()
  hook.handler = on_keyboard_events
  hook.hook()

def init_osc():
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default=OSC_IP, help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=OSC_PORT, help="The port the OSC server is listening on")
  args = parser.parse_args()
  osc_client = udp_client.SimpleUDPClient(args.ip, args.port)
  return osc_client

# def send_message(osc_client, path, value):
#   osc_client.send_message(path, value)

osc_client = init_osc()
def send_loc(key):
  hand = KEY_FINGER[key][0]
  column = (KEY_LOC[key][1] - 7.5) / 7.5
  row = (KEY_LOC[key][0] - 2) / 2.0
  osc_client.send_message("/avatar/parameters/KBDColumn" + hand, column)
  osc_client.send_message("/avatar/parameters/KBDRow" + hand, row)
  osc_client.send_message("/avatar/parameters/test01", 1.0)
  print(hand, column, row)

def on_keyboard_events(args):
  if isinstance(args, KeyboardEvent):
    print(args.key_code, args.current_key, args.event_type)
    send_loc(args.current_key)

  if isinstance(args, MouseEvent):
    print(args.mouse_x, args.mouse_y)

if __name__ == '__main__':
  main()