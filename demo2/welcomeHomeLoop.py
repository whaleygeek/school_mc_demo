import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
	time.sleep(1)
	pos = mc.player.getTilePos()

	if pos.x == 0 and pos.z == 0:
		mc.postToChat("welcome home")
        

