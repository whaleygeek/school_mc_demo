import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

#mc.player.setTilePos(0, 0, 2)

mc.setBlock(0, -1, 2, block.WOOL.id, 4)

pos = mc.player.getTilePos()

if pos.x == 0 and pos.z == 2:
	mc.postToChat("welcome home")
