import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

def bomb(x, y, z):
	mc.setBlock(x+1, y, z+1, block.TNT.id)

	for a in range(5, 0, -1):
		mc.postToChat(str(a))
		time.sleep(1)

	mc.postToChat("BANG!")
	mc.setBlocks(x-10, y-5, z-10, x+10, y+10, z+10, block.AIR.id)
	#mc.player.setTilePos(x, y+40, z)


mc.postToChat("READY!")
time.sleep(2)

pos = mc.player.getTilePos()
bomb(pos.x, pos.y, pos.z)

