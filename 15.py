def walk(current, visited, n):
	if current == (n-1,n-1):
		return 1
	routes = 0
	directions = [(1,0), (0,1)]
	for dirs in directions:
		next = (current[0] + dirs[0], current[1] + dirs[1])
		if next[0] >=n or next[1] >=n:
			continue
		if next in visited:
			routes += visited[next]
		else:
			routes += walk(next, visited, n)
	
	visited[current] = routes
	return routes

if __name__=="__main__":
	print(walk((0,0), {}, 20 + 1))
