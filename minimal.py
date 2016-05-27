#!/usr/bin/python
#import demo
import pi3d
DISPLAY=pi3d.Display.create(x=150,y=150)
shader=pi3d.Shader("mat_light")
mycube=pi3d.Cuboid(z=6.0)
mycube.set_material((1.0,1.0,0.1))
mycube.set_shader(shader)

mykeys=pi3d.Keyboard() 
while DISPLAY.loop_running():
  mycube.draw()
  if mykeys.read()==27:
    mykeys.close()
    DISPLAY.destroy()
    break
