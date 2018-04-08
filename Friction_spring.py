#Joseph Rice
#2/8/2018
# PY 4 spring program

from __future__ import division
from visual import *
from visual.graph import *
import time
scene.width = 1000
scene.height = 2000
# The base the spring will sit on
floor = box(pos=vector(0,0,0),length=.20,width=.20,height=0.01,color=color.orange,\
            material=materials.wood)


# unit vector for spring force
Force_spring_hat = vector(0,1,0)
print("Unit vector for Force of spring: ", Force_spring_hat)

# Block will sit on top of spring
Block = box(pos=vector(0,.1,0),length=.05,width=.05,height=0.05,color=color.white,\
            material=materials.earth)

# spring that will update
spring = helix(pos=floor.pos,axis=Block.pos-floor.pos,radius=.02,color=color.yellow)

## inital conditions about spring 
K_stiff=8 # N/m
print("Spring constant ",K_stiff,'N/m')
Lo =.20 # m
print('Lo= ',Lo)
Block.mass = 60e-3#Kg
print("Mass of block: ",Block.mass,'kg')
Block.p = Block.mass*vector(0,0,0) # Kg*m/s
print("inital momentum",Block.p,'kg*m/s')
# The force of gravity 
F_g = vector(0,-1*Block.mass*9.8,0) # N
print('Force of gravity ',F_g,'N')

Delta_t =0.1 #s
t = 0

graph = gdisplay(x=0,y=0,width=600,height=400,title="Net Force",xtitle='Time(x)',\
                 ytitle='Force Newtons',foreground=color.green,background=color.black)

func1 = gcurve(gdiplay = graph,color=color.black)               
graph2 = gdisplay(x=0,y=0,width=600,height=400,title="OcillatingSpring",xtitle='Time(x)',\
                 ytitle='Position(m)',foreground=color.green,background=color.black)
func1 = gcurve(gdiplay = graph,color=color.green)
function = gcurve(gdisplay = graph,color=color.green)


## osolation will last of 3 seconds
c = 0.005
while t <=500:
    viscous_friction = c*(-Block.p/Block.mass)
    rate(100)
    #print(spring.axis,Lo)
    F_spring = -1*K_stiff*(mag(spring.axis)-Lo)*Force_spring_hat
    #print(F_spring)
    F_net = F_g + F_spring + viscous_friction 
    function.plot(pos=(t,F_net.y))
##    func2.plot(pos=(t,F_spring.y))
    #print('F_net',F_net)
    Block.p = Block.p + F_net*Delta_t
    spring.axis = spring.axis + Block.p*Delta_t
    Block.pos = spring.axis
    func1.plot(pos=(t,Block.pos.y))
    t = t + Delta_t
    

    
    





    


