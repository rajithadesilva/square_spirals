__author__ = "Rajitha de Silva"
__copyright__ = "Copyright (C) 2022 rajitha@ieee.org"
__license__ = "CC"
__version__ = "1.0"

from turtle import *
from random import randint
import math
import spirals 


if __name__ == "__main__":
    #Create a spiral with a side length of 10 and separation of 1
    side_length = 10
    separation = 1
    square_spiral = spirals.sqspiral(side_length,separation)

    #Visualize the spiral using python Turtle Graphics
    square_spiral.visualize()

    #Get the total length of the spiral
    square_spiral.tot_length()

    #Get the segment ID of the spiral given the elapsed length along the spiral upto a given input distance (ex:20)
    elapsed_distance = 20
    square_spiral.get_segment(elapsed_distance)

    #Get cartesian coordinates of the spiral (x,y) given the elapsed length along the spiral upto a given input distance (ex:20)
    square_spiral.get_x(elapsed_distance)
    square_spiral.get_y(elapsed_distance)
    x,y = square_spiral.get_xy(elapsed_distance)

    #Get the elapsed length along the spiral upto a given input cartesian coordinates (x,y)
    square_spiral.xy_to_pos(x,y)




