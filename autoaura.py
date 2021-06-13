#!/usr/bin/env python3

import json
import sys
import time

import pynput.mouse
import pynput.keyboard
from pynput.mouse import Button

def main():
	mouse = pynput.mouse.Controller()
	keyboard = pynput.keyboard.Controller()

	if len(sys.argv) == 2 and sys.argv[1] == 'setup':
		setup(mouse)
		return

	with open('positions.json', 'r') as f:
		aura_positions = json.load(f)
	for pos in aura_positions:
		activate_aura(mouse, keyboard, pos)

	mouse.position = (1636, 1163)
	time.sleep(0.05)
	mouse.click(Button.left)
	time.sleep(0.05)
	mouse.position = (1393 + 1 * 72, 990 - 3 * 72) # impurity of lightning
	time.sleep(0.05)
	mouse.click(Button.left)
	time.sleep(0.05)

def activate_aura(mouse, keyboard, pos):
	mouse.position = (1636, 1163)
	time.sleep(0.05)
	mouse.click(Button.left)
	time.sleep(0.05)

	mouse.position = (1393 + pos[0] * 72, 990 - pos[1] * 72)
	time.sleep(0.05)
	mouse.click(Button.left)
	time.sleep(0.05)

	keyboard.press('t')
	keyboard.release('t')
	time.sleep(0.05)

def setup(mouse : pynput.mouse.Controller):
	positions = set()

	def on_press(key):
		nonlocal positions
		if key == pynput.keyboard.Key.esc:
			return False
		elif key == pynput.keyboard.Key.ctrl_l:
			pos = ((mouse.position[0] - 1356) // 72, -(mouse.position[1] - 1038) // 72)
			print('recording', pos)
			positions.add(pos)

	with pynput.keyboard.Listener(on_press=on_press) as listener:
		listener.join()
	with open('positions.json', 'w') as f:
		json.dump(list(positions), f, indent='\t')

if __name__ == '__main__':
	main()
