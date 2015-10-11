import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import pygame

mc = minecraft.Minecraft.create()
pygame.mixer.init()
s = pygame.mixer.Sound('../demo3/squeak.wav')

mc.player.setTilePos(0,0,0)
mc.setBlock(0, -1, 2, block.WOOL.id, 3)

while True:
        time.sleep(1)
        pos = mc.player.getTilePos()
        if pos.x == 0 and pos.y == 0 and pos.z == 2:
                s.play()
                mc.postToChat("Yippeee!!!")
                mc.player.setTilePos(pos.x, pos.y+10, pos.z)
