import numpy as np

island_map = [[1, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]

m, n = np.array(island_map).shape

undicovered_map = [(x, y) for y in range(n) for x in range (m)]

cur_adjancent = []

islands = 0

while undicovered_map:
	
	und_x, und_y = undicovered_map.pop(0)
	if (island_map[und_x][und_y]):
		cur_adjancent.append((und_x, und_y))
		islands += 1

	while(cur_adjancent):
		cur_x, cur_y = cur_adjancent.pop(0)
		
		# North 
		north = (cur_x, cur_y + 1)
		if north in undicovered_map:
			if island_map[cur_x][cur_y + 1]:
				cur_adjancent.append(north)
				undicovered_map.remove(north)
		# East
		east = (cur_x + 1, cur_y)
		if east in undicovered_map:
			if island_map[cur_x + 1][cur_y]:
				cur_adjancent.append(east)
				undicovered_map.remove(east)
		# South
		south = (cur_x, cur_y - 1)
		if south in undicovered_map:
			if island_map[cur_x][cur_y - 1]:
				cur_adjancent.append(south)
				undicovered_map.remove(south)
		# West
		west = (cur_x - 1, cur_y)
		if west in undicovered_map:
			if island_map[cur_x -1][cur_y]:
				cur_adjancent.append(west)
				undicovered_map.remove(west)

print(islands)


