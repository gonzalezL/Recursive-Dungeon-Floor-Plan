from __future__ import print_function
import random

def printRoomNums(grid):
	for row in grid:
		print(row)

def drawRoom(grid, rows, cols):
	# Top Border
	for x in range(cols+2):
		print(unichr(0x2588), end="")
	print()

	for x in range(cols):
		for y in range(rows):
			# Left Border
			if y==0:
				print(unichr(0x2588), end="")

			# Grid Layout
			if grid[y][x] == 2 or grid[y][x] == 0:
				print(unichr(0x2588), end="")
			else:
				print(" ", end="")
			
			# Right Border
			if y==rows-1:
				print(unichr(0x2588), end="")
		print()
	
	# Bottom Border
	for x in range(cols+2):
		print(unichr(0x2588), end="")
	print("\n")

def addTile(grid, x, y, rows, cols, start):
	if x<0 or x>=cols or y<0 or y>=rows or grid[y][x]==2 or grid[y][x]==1:
		return grid
	if start or random.randint(1,3) != 1:	
		grid[y][x] = 1
	else:
		grid[y][x] = 2
		return grid

	grid = addTile(grid, x-1, y, rows, cols, 0)
	grid = addTile(grid, x+1, y, rows, cols, 0)
	grid = addTile(grid, x, y-1, rows, cols, 0)
	grid = addTile(grid, x, y+1, rows, cols, 0)

	return grid

def generateRoom(rows, cols):
	grid = [[0 for i in range(cols)] for j in range(rows)]
	x, y = random.randint(1,cols-1), random.randint(1,rows-1)

	grid = addTile(grid, x, y, rows, cols, 1)

	print("\n")
	drawRoom(grid, rows, cols)

if __name__ == "__main__":
	rows = input("Define max length: ")
	cols = input("Define max width: ")
	generateRoom(rows, cols)