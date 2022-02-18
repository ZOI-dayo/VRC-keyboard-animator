import argparse
import random
import time

from pythonosc import udp_client
from pyhooked import Hook, KeyboardEvent, MouseEvent

OSC_IP = "127.0.0.1"
OSC_PORT = 9000

def main():
  osc_client = init_osc()
  osc_client.send_message("/avatar/parameters/VRCSupine", 1)
#   send_message(osc_client, "/filter", random.random())

#   for x in range(10):
#     osc_client.send_message("filter", 1.0)
#     time.sleep(1)
#     print("send2")
#   hook = Hook()
#   hook.handler = on_keyboard_events
#   hook.hook()

def init_osc():
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default=OSC_IP, help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=OSC_PORT, help="The port the OSC server is listening on")
  args = parser.parse_args()
  osc_client = udp_client.SimpleUDPClient(args.ip, args.port)
  return osc_client

# def send_message(osc_client, path, value):
#   osc_client.send_message(path, value)

def on_keyboard_events(args):
  if isinstance(args, KeyboardEvent):
    print(args.key_code, args.current_key, args.event_type)

  if isinstance(args, MouseEvent):
    print(args.mouse_x, args.mouse_y)

if __name__ == '__main__':
  main()