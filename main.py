from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 240, 255, 4 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )
#for script right now I have Milan's image. I will create my own too I just needed something to test if my code was working
