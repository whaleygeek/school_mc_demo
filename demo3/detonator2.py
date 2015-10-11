import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import countdown

import RPi.GPIO as GPIO
BUTTON = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

mc = minecraft.Minecraft.create()
mc.postToChat("PRESS THE BUTTON!")

def bomb(x, y, z):
	mc.setBlock(x+1, y, z+1, block.TNT.id)

	for a in range(5, 0, -1):
		mc.postToChat(str(a))
		time.sleep(1)
	#countdown.count()

	mc.postToChat("BANG!")
	#countdown.bang()
	mc.setBlocks(x-10, y-5, z-10, x+10, y+10, z+10, block.AIR.id)
	#mc.player.setTilePos(x, y+40, z)

try: 
	while True:
		time.sleep(0.1)
		if GPIO.input(BUTTON) == False:
			pos = mc.player.getTilePos()
			bomb(pos.x, pos.y, pos.z)

finally: 
	GPIO.cleanup()

