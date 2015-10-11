import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

#mc.player.setTilePos(0, 0, 0)

mc.setBlock(0, 0, 0, block.WOOL.id)

pos = mc.player.getTilePos()

if pos.x == 0 and pos.z == 0:
	mc.postToChat("welcome home")
