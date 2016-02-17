import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()


def refresh():
  import sys
  me = sys.modules["live"]
  reload(me)


def hello():
  mc.postToChat("hello minecraft world again")


def jump():
  pos = mc.player.getTilePos()
  mc.player.setTilePos(pos.x, pos.y+20, pos.z)
  mc.postToChat("Yippee!")


def tower(size=None):
  if size == None:
    size = int(raw_input("How tall a tower?"))
  pos = mc.player.getTilePos()
  mc.setBlocks(pos.x+1, pos.y, pos.z, pos.x+1, pos.y+size, pos.z, block.SAND.id)
  mc.postToChat("Look to the sky!")


def clear(size=None):
  if size == None:
    size = int(raw_input("How big?"))
  size/=2
  pos = mc.player.getTilePos()
  mc.setBlocks(pos.x-size, pos.y-1, pos.z-size, pos.x+size, pos.y+size,pos.z+size, block.AIR.id)
  mc.postToChat("BANG!")
  

def house(SIZE=None):
    if SIZE==None:
      SIZE = int(raw_input("Size of house?"))
    x,y,z = mc.player.getTilePos()
    x += 4
    midx = x+SIZE/2
    midy = y+SIZE/2  
    
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.COBBLESTONE.id)
    mc.setBlocks(x+1, y, z+1, x+SIZE-2, y+SIZE-1, z+SIZE-2, block.AIR.id)
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, block.WOOD.id)
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-2, y-1, z+SIZE-2, block.WOOL.id, 14)
    

