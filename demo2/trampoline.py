import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

mc.setBlock(0, 0, 0, block.WOOL.id, 3)

while True:
	time.sleep(1)
	pos = mc.player.getTilePos()
	if pos.x == 0 and pos.y == 0 and pos.z == 0:
		mc.player.setTilePos(0, 40, 0)
