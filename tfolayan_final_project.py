#Tofarati Folayan
#COMP112-01
#Final Project

import math
import turtle
from turtle import *

screen = turtle.Screen()
screen.bgpic('C:/Users/user/Pictures/space.gif')
screen.setup(1366,768)

#The gravitational constant, G
G = 6.67428*(10**-11)

AU = (149.6*10**9) # represents 149.6 million km, in meters. Average distance from Sun to Earth.
scale = 250/AU #Assumed scale, as the animation will be massive without it, so I set one AU = 100 pixels.

class Body(Turtle):
    #sig: (Body) ->
    #I can use this to create a new type, Body, using Turtle as a subclass.
    #Here, I can create a planetary body with the attributes below.

    #Extra attributes:
    #mass: in kg
    #vx, vy: x, y velocities in m/s
    #px, py: x,y positions in m

    def __init__(self,name,mass,vy,vx,px,py):
        super().__init__(visible=True)
        self.name = name
        self.mass = mass
        self.vx = vx
        self.vy = vy
        self.px = px
        self.py = py

    def attraction(self,other):
        #sig: (body),(body) -> int, int
        #Returns the force exerted upon this body by the other body.

        #Firstly, I must compute the distance of the other body.
        sx = self.px
        sy = self.py
        ox = other.px #setting up the initial positions of both bodies.
        oy = other.py
        dx = (ox-sx)
        dy = (oy-sy)  #getting the direction in both the x and y directions.
        r = math.sqrt(dx**2 + dy**2) # magnitude of distance between them.

        #Report if the distance is zero, to avoid ZeroDivisionError
        if r == 0:
            raise ValueError("Collision between objects", self.name, "and", other.name)

        #Now, I can compute the gravitational force of attraction.
        F = G*self.mass*other.mass/(r**2)

        #Compute the direction of the force.
        theta = math.atan2(dy, dx)
        Fx = math.cos(theta)*F
        Fy = math.sin(theta)*F

        return Fx,Fy #returns the individual sections of the force





def orbit(bodies):
    #sig: list(Body)-> loop
    #This function never returns; it loops through the simulation.

    timestep = 24*3600 # seconds in one day; the loop moves per each day

    for body in bodies:
        body.penup()


        while True:  #infinite loop

            force = {} #to store force values
            for body in bodies:
                #to loop over the planets in the list
                total_Fx=0.0 #initialise forces
                total_Fy=0.0
                for other in bodies:
                    #loop through the list of bodies and continuously calculates the force on each body.
                    #Not calculating the body's attraction to itself.
                    if body is other:
                        continue
                    Fx,Fy = body.attraction(other) #getting the values of fx and fy from the attraction fxn.
                    total_Fx+=Fx #now the magnitude and direction of the force can always change
                    total_Fy+=Fy

                force[body]=(total_Fx,total_Fy) #this is the total force exerted in a dictionary; the planets are the keys and the force values are the values.


            #Update their velocities based on the force, since they must accelerate.
            for body in bodies:
                Fx,Fy = force[body] #bringing out the force values from the dictionary
                body.vx+=(Fx/body.mass)*timestep #v final = (F*t)/m when v initial is zero
                body.vy+=(Fy/body.mass)*timestep

                #Update their positions as well, since they are in motion
                body.px+=body.vx*timestep # distance = speed * time
                body.py+=body.vy*timestep
                body.goto(body.px*scale, body.py*scale)#actually moves the planet there using the vectors
                #body.speed(10)#in case i need to speed it up



#Instantiation of the planets
Sun = Body('Sun',1.98892*10**30,0.0,0.0,0.0,0.0)
Mercury = Body('Mercury',3.285*10**23,47360,0.0,-0.39*AU,0.0) #velocity all in the y direction as the initial positions of all the planets are on the x-axis.
Venus = Body('Venus',4.86685*10**24,35020,0.0,-0.723*AU,0.0)
Earth = Body('Earth',5.9742*10**24,29783,0.0,-1*AU,0.0)
Mars = Body('Mars',6.4171*10**23,24070,0.0,-1.524*AU,0.0)

#replacing the turtles for these images
image = ('C:/Users/user/Downloads/Sun.gif')
screen.register_shape(image)
screen.addshape(image)
Sun.shape(image)

image2 = ('C:/Users/user/Pictures/Mercury.gif')
screen.register_shape(image2)
screen.addshape(image2)
Mercury.shape(image2)

image3 = ('C:/Users/user/Downloads/Venus.gif')
screen.register_shape(image3)
screen.addshape(image3)
Venus.shape(image3)

image4 = ('C:/Users/user/Downloads/Earth.gif')
screen.register_shape(image4)
screen.addshape(image4)
Earth.shape(image4)

image5 = ('C:/Users/user/Downloads/Mars.gif')
screen.register_shape(image5)
screen.addshape(image5)
Mars.shape(image5)

planets = [Sun,Mercury,Venus,Earth,Mars] #list of the planets so far

orbit(planets)


#Can't add any more planets because it cannot fit in the diagram
#Can't create an elliptical orbit because I don't know how to use numpy :(
