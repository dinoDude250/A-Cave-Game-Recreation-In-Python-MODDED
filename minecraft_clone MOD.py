'''
Disclaimer: This solution is not scalable for creating a big world.
Creating a game like Minecraft requires specialized knowledge and is not as easy
to make as it looks.

You'll have to do some sort of chunking of the world and generate a combined mesh
instead of separate blocks if you want it to run fast. You can use the Mesh class for this.

You can then use blocks with colliders like in this example in a small area
around the player so you can interact with the world.
'''

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
import os
print(0)
app = Ursina()
print(1)

window.color = color.hex('#61a2ff')

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.

# This prints all files Ursina thinks it can find in its search path

# Manual check
if os.path.exists('textures/z64.png'):
    print("File definitely exists in the folder!")
else:
    print("File NOT found in textures folder. Check spelling or folder location.")

class Slayer(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            # Try the relative path if 'stone' alone fails
            texture='textures/g64.png', 
            color=color.white, # Use white to ensure texture isn't tinted
            highlight_color=color.white,
        )
class Clayer(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__ (
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            # Try the relative path if 'stone' alone fails
            texture='textures/z64.png', 
            color=color.white, # Use white to ensure texture isn't tinted
            highlight_color=color.white,
    )

class Wlayer(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__ (
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            # Try the relative path if 'stone' alone fails
            texture='textures/a64.png', 
            color=color.white, # Use white to ensure texture isn't tinted
            highlight_color=color.white,
    )

ny = 0
for j in range(7):
    for z in range(10):
        for x in range(10):
            if ny == 0:
                voxel = Slayer(position=(x,ny,z))
            else:
                voxel = Clayer(position=(x, ny,z))
    ny -= 1




def input(key):
    if key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            if hit_info.entity.position.y == -1:
                Slayer(position=hit_info.entity.position + hit_info.normal)
            elif hit_info.entity.position.y > -1:
                Wlayer(position=hit_info.entity.position + hit_info.normal)
            else:
                Clayer(position=hit_info.entity.position + hit_info.normal)
    if key == 'left mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)
    if key == 'q':
        sys.exit()
    if key == 'left shift':
        player.speed = 1
    else:
        player.speed = 6


player = FirstPersonController()
player.jump_height = 1
app.run()