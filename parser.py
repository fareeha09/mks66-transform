from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
	fd = open(fname,"r")
	line = fd.readlines()
	
	i=0
	while (i < len(line)):
		val = line[i].strip("\n").strip("\r")
		print val
		
		if (val == "line"):
			c = line[i+1].strip("\n").strip("\r").split(" ")
			add_edge(points, int(c[0]), int(c[1]), int(c[2]), int(c[3]), int(c[4]), int(c[5]))
			i+=2
			
		elif (val == "ident"):
			ident(transform)
			i+=1

		elif (val == "scale"):
			c = line[i+1].strip("\n").split(" ")
			m = make_scale(int(c[0]), int(c[1]), int(c[2]))
			matrix_mult(m, transform)
			i+=2
		
		elif (val == "translate"):
			c = line[i+1].strip("\n").split(" ")
			m = make_translate(int(c[0]), int(c[1]), int(c[2]))
			matrix_mult(m, transform)
			i+=2
			
		elif (val == "rotate"):
			c = line[i+1].strip("\n").split(" ")
			                                                           
			if ([0] == "x"):
				m = make_rotX(int(c[1]))
			if (c[0] == "y"):
				m = make_rotY(int(c[1]))
			if (c[0] == "z"):
				m = make_rotZ(int(c[1]))
				
			matrix_mult(m,transform)
			i+=2
			
		elif (val == "apply"):
			matrix_mult(transform, points)
			i+=1
			
		elif (val == "display"):
			clear_screen( screen )
			draw_lines(points, screen, color )
			display(screen)
			i+=1
			
		elif (val == "save"):
			c = line[i+1].strip("\n").split(" ")
			clear_screen(screen)
			for l in range(len(points)):
				for p in range(len(points[l])):
					points[l][p]= int(points[l][p])
			draw_lines(points, screen, color )
			save_extension(screen, c[0])
			i += 2
			
		elif (val == "quit"):
			i = len(line)
			
		else:
			print(val)
			i+=2
			
			
