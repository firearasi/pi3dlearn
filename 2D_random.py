import demo
import pi3d,math,numpy as np
import numpy.random

display=pi3d.Display.create(x=50,y=350,w=800,h=600,tk=True,
  window_title="AAA")
CAMERA= pi3d.Camera(is_3d=False)

matsh=pi3d.Shader('mat_flat')

vertices =np.array([[-100.0,-100.0,0.0],
              [-100.0,100.0,0.0],
              [100.0,100.0,0.0],
              [100.0,-100.0,0.0]])
square=pi3d.Lines(camera=CAMERA,vertices=vertices,
            closed=True,material=(1.0,0.8,0.05),line_width=3)
            
square.set_shader(matsh)
t_mat=np.eye(3,dtype=np.float32)
r_mat=np.eye(3,dtype=np.float32)
s_mat=np.eye(3,dtype=np.float32)
angle=0

def refresh_vertices(shape,old_verts):
  new_verts=[]
  for v in old_verts:
    # One order
    new_v=t_mat @ r_mat @ s_mat @ np.array([v[0],v[1],1.0])
    new_verts.append(new_v)
  shape.re_init(pts=np.array(new_verts))

def print_matrices():
  head_str = "        translation                 rotation                    scale"
  if hasattr(keys,"key"):
    keys.key.addstr(1, 0, head_str)
  else:
    print(head_str)
  for i in range(3):
    t, r, s = t_mat[i], r_mat[i], s_mat[i]
    out_str = ("{:8.3f},{:8.3f},{:8.3f} |{:8.3f},{:8.3f},{:8.3f} |{:8.3f},{:8.3f},{:8.3f}"
            .format(t[0], t[1], t[2], r[0], r[1], r[2], s[0], s[1], s[2]))
    if hasattr(keys,"key"): # curses set up
      keys.key.addstr(2 + i, 0, out_str)
    else:
      print(out_str)

keys=pi3d.Keyboard()
xaxis=pi3d.Lines(camera=CAMERA,vertices=[[-250,0,0],[250,0,0]],
          z=1.0,material=(0.0,1.0,1.0),line_width=2)
xaxis.set_shader(matsh)

yaxis=pi3d.Lines(camera=CAMERA,vertices=[[0,-250,0],[0,250,0]],
          z=1.0,material=(0.0,1.0,1.0),line_width=2)
yaxis.set_shader(matsh)

choices=['w','a','s','d','z','x','c','v']
import numpy.random
while display.loop_running():
  square.draw()
  #letters.draw()
  xaxis.draw()
  yaxis.draw()
  do_rotation=0

  q=keys.read()
  if q==27:
    keys.close()
    display.destroy()
  
  
  rand=numpy.random.randint(0,len(choices))
  k=choices[rand]

  
  
  if k=='w':
    t_mat[1][2]+=5.0
  elif k=='s':
    t_mat[1][2]-=5.0
  elif k=='a':
    t_mat[0][2]-=5.0
  elif k=='d':
    t_mat[0][2]+=5.0
  elif k=='c':
    s_mat[0][0]=s_mat[1][1]=s_mat[0][0]*1.05
  elif k=='v':
    s_mat[0][0]=s_mat[1][1]=s_mat[0][0]/1.05
  elif k=='z':
    do_rotation=1
    angle+=2.5*np.pi/180
  elif k=='x':
    do_rotation=1
    angle-=2.5*np.pi/180
  if do_rotation:
    r_mat=np.array([[np.cos(angle),-np.sin(angle),0],
                              [np.sin(angle),np.cos(angle),0],
                              [0,0,1]])
  
  print_matrices()
  refresh_vertices(square,vertices)

  
  
