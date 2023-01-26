__author__ = "Rajitha de Silva"
__copyright__ = "Copyright (C) 2022 rajitha@ieee.org"
__license__ = "CC"
__version__ = "1.0"

from turtle import *
from random import randint
import math

class sqspiral(object):
    def __init__(self, width, separation):                             #                   ⟵------------- 𝗱 ------------⟶
        self.d = width #Side length of the Square Spiral (Even Number)                     __________________________________
        self.s = separation #Space between 2 rows                                          |                ➁                |
        self.n = int((self.d/self.s)+1) #Number of vertical rows in the spiral(Odd Number) |                                |
        self.color = "green" #Colour of the spiral drawing                                 |                                |    
        self.stroke_size = 4 #Size of the pen stroke of spiral drawing                     |       __________________       |
        self.size = 20 #Size scale of spiral drawing                                       |       |        ⑥       |       |
                                                               #                           |       |                |       |
    #Generate Visualization of Spiral Crop Pattern                                         |       |                |       |
    def visualize(self):                                       #                           |⟵𝘀⟶    |        |       |       |       ⓝ⟶Line segment ID
        pen = Turtle()                                         #                           |       |        |       |       |       This example has 5 vertical lines
        pen.width(self.stroke_size) #Size of the pen stroke                             ➀  |       |⑤      |⑨       | ⑦    |➂        (n=5)                   
        pen.pencolor(self.color) #Spiral Colour                                            |       |        |       |       |
                                                               #                           |       |        |_______|       |
        pen2 = Turtle()                                        #                           |       |            ⑧            |
        pen2.penup()                                           #                           |       |                        |
        pen2.goto(400, -350)                                   #                           |       |                        |
        pen2.pendown()                                         #                           |       |________________________|
        pen2.width(self.stroke_size) #Size of the pen stroke                                                 ④
        colormode(255)
        pen2.color(randint(0,255),randint(0,255),randint(0,255)) #Line map colour

        pen.right(90)
        pen.backward(self.size)  
        pen2.backward(self.size/5)

        for i in range((int(self.n/2) * 4)+2):
            pen.left(90)
            pen.backward(i * self.size)
            pen2.backward(i * (self.size/5))
            pen2.color(randint(0,255),randint(0,255),randint(0,255))
        done()
        return 0

    #Return the total length of the spiral
    def tot_length(self):
        tot = ((2*self.n -1)*self.d) - ((2*self.s)*sum(range(1,(self.n-1))))#Note: Summing upto n-2 is n-1 in range function
        print('Spiral length:',tot)
        return tot

    #Return current line segment ID from elapsed distance (pos) in spiral
    def get_segment(self, pos):
        pos = math.ceil(pos) #Continous pos values must be fed through ceil function
        n_seg = 2*self.n - 1 #Toatal number of line segments making up the spiral
        if pos<=3*self.d:
            seg = math.ceil(pos/self.d)
            lower=0
            if seg==1:
                lower= -self.s #Set to facilitate 0 intercept in segment 1 y curve
            elif seg==2:
                lower = self.d #Set to facilitate d intercept in segment 2 x curve
            upper=3*self.d #Set to facilitate 3*d intercept in segment 3 y curve

        elif pos<=self.tot_length():
            seg_len = self.d-self.s
            lower = 3*self.d
            upper = lower+seg_len
            seg = 3 #Note: set to 3 to be incremented at the begining of the for loop
            for i in range(4,n_seg):
                seg = seg + 1
                if lower < pos <= upper:
                    break
                lower = upper
                upper = upper + seg_len

                seg = seg + 1
                if lower < pos <= upper:
                    break
                seg_len=seg_len - self.s
                lower = upper
                upper = upper + seg_len
        else:
            seg = 0
            print("Invalid Position Input for segment getter function")

        print('Current Segment:', seg)
        return seg, lower, upper

    #Return X coordinate of the robot from elapsed distance (pos) in spiral
    def get_x(self, pos):
        seg, lower, upper = self.get_segment(pos)
        if seg%2 == 0:# For upwards or downwards strides
            if seg%4 == 0:#For downward strides of X
                m=-1
                c=upper+(((seg)/4)*self.s)
            else:#For upward strides of X  ####check 2
                m=1
                c=-(lower-(((seg-2)/4)*self.s))
        elif (seg-1)%4 == 0:#Lower flat lines
            m=0
            c=((seg-1)/4)*self.s
        elif (seg+1)%4 == 0:#Upper flat lines
            m=0
            c=self.d-((((seg+1)/4)-1)*self.s)
        else:
            print("Calculation Error: X Position")

        x = m*pos + c
        print('X Position:',x)
        return x

    #Return Y coordinate of the robot from elapsed distance (pos) in spiral
    def get_y(self, pos):
        seg, lower, upper = self.get_segment(pos)
        if seg%2 == 0:# For even numbered segments -> Flat line
            m=0
            if seg%4 == 0:#Upper flat lines
                c=((seg/4)-1)*self.s
            else:#Lower flat lines
                c=self.d-(((seg-2)/4)*self.s)
        elif (seg-1)%4 == 0:#For upward strides of Y
            m=1
            c=-(lower-((((seg-1)/4)-1)*self.s))
        elif (seg+1)%4 == 0:#For downward strides of Y
            m=-1
            c=upper+((((seg+1)/4)-1)*self.s)
        else:
            print("Calculation Error: Y Position")

        y = m*pos + c
        print('Y Position:',y)
        return y

    #Return X,Y coordinate of the robot from elapsed distance (pos) in spiral
    def get_xy(self, pos):
        x = self.get_x(pos)
        y = self.get_y(pos)
        return x,y
    #Return elapsed total distance on spiral given a spiral coordinate
    def xy_to_pos(self, x, y):                                             #   ___________
        m1 = 1 #Limiter function 1 gradient to identify segment zone           |╲     ① ╱| f1(x), f2(x) and f3(x)
        m2 = -1 #Limiter function 2 gradient to identify segment zone          |②╲    ╱  | y > f1(x), f2(x) ⟶ Horizontal Upper Segment
        c2 = self.d #Limiter function 2 intercept to identify segment zone     |   ╲ ╱  ╱| y < f2(x), f3(x) ⟶ Horizontal Lower Segment
        m3 = 1  #Limiter function 3 gradient to identify segment zone          |   ╱ ╲╱③| f3(x) < y < f2(x)⟶ Vertical Left Segment 
        c3 = -self.s #Limiter function 3 intercept to identify segment zone    | ╱   ╱ ╲ | f2(x) < y < f1(x)⟶ Vertical Right Segment 
        pos=0                                                             #    |╱   ╱___╲|
        i = -1                                                             #    ←s→  

        y1 = m1*x
        y2 = m2*x + c2
        y3 = m3*x + c3

        if y >= y1 and y > y2: #On a horizontal line at top
            for i in range(int((self.d-y)/self.s)):
                pos = pos + 4*(self.d-(2*i*self.s))
            pos = pos + (self.d-(2*(i+1)*self.s)) + x - ((i+1)*self.s)
            print("HT")

        elif y < y2 and y <= y3: #On a horizontal line at bottom
            for i in range(int(y/self.s)):
                pos = pos + 4*(self.d-(2*i*self.s))
            pos = pos + 3*(self.d-(2*(i+1)*self.s)) + self.d - x - ((i+1)*self.s)
            print("HB")

        elif y2 <= y < y1: #On a vertical line to the right
            for i in range(int((self.d-x)/self.s)):
                pos = pos + 4*(self.d-(2*i*self.s))
            pos = pos + 2*(self.d-(2*(i+1)*self.s)) + self.d - y - ((i+1)*self.s)
            print("VR")

        elif y3 < y <=y2: #On a vertical line to the left
            for i in range(int(x/self.s)):
                pos = pos + 4*(self.d-(2*i*self.s))
            pos = pos + y - ((i+1)*self.s)
            print("VL")

        else:
            print("Error: Given point is not within the spiral")

        print('Linear Position:',pos)
        return pos




