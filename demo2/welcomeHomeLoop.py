import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
mc.setBlock(0,-1,2, block.WOOL.id, 5)
mc.postToChat("Time to go home!")

while True:
	time.sleep(1)
	pos = mc.player.getTilePos()

	if pos.x == 0 and pos.z == 2:
		mc.postToChat("welcome home")
        

