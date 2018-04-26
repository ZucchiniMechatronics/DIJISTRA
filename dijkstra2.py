from collections import defaultdict
from heapq import *

def dijkstra(f, t):
	edges = [
			('a1', 'b1', 1),
            ('a2', 'a1', 1),
            ('a3', 'b3', 1),
            ('a3', 'a2', 1),
            ('a4', 'a3', 1),
            ('b1', 'c1', 1),
            ('b2', 'a2', 1),
            ('b3', 'c3', 1),
            ('b4', 'a4', 1),
            ('c1', 'd1', 1),
            ('c1', 'f1', 1),
            ('c2', 'b2', 1),
            ('c3', 'd3', 1),
            ('c3', 'f3', 1),
            ('c4', 'b4', 1),
            ('d1', 'd2', 1),
            ('d1', 'f1', 1),
            ('d2', 'd3', 1),
            ('d2', 'f3', 1),
            ('d3', 'd4', 1),
            ('d4', 'c4', 1),
            ('e1', 'f1', 1),
            ('e2', 'e1', 1),
            ('e3', 'e2', 1),
            ('e3', 'f3', 1),
            ('e3', 'c2', 1),
            ('e4', 'e3', 1),
            ('f1', 'g1', 1),
            ('f2', 'd3', 1),
            ('f2', 'c2', 1), 
            ('f2', 'e2', 1),
            ('f3', 'g3', 1),
            ('f4', 'e4', 1),
            ('f4', 'c4', 1),
            ('g1', 'i1', 1),
            ('g2', 'f2', 1),
            ('g3', 'h2', 1),
            ('g3', 'i3', 1),
            ('g4', 'f4', 1),
            ('h1', 'i4', 1),
            ('h2', 'h1', 1),
            ('h3', 'h2', 1),
            ('h3', 'i3', 1),
            ('h4', 'h3', 1),
            ('i1', 'j1', 1),
            ('i2', 'g2', 1),
            ('i2', 'h2', 1),
            ('i3', 'j3', 1),
            ('i4', 'h4', 1),
            ('i4', 'g4', 1),
            ('j1', 'k1', 1),
            ('j2', 'i2', 1),
            ('j3', 'k3', 1),
            ('j4', 'i4', 1),
            ('k1', 'k2', 1),
            ('k2', 'j2', 1),
            ('k2', 'k3', 1),
            ('k3', 'k4', 1),
            ('k4', 'j4', 1)
             ]
             
	g = defaultdict(list)
	for l,r,c in edges:
		g[l].append((c,r))

	q, seen = [(0,f,())], set()
	while q:
		(cost,v1,path) = heappop(q)
		if v1 not in seen:
			seen.add(v1)
			path = (v1, path)
			
			if v1 == t: 
				return (path)

			for c, v2 in g.get(v1, ()):
				if v2 not in seen:
					heappush(q, (cost+c, v2, path))

	return float("inf")

def pathdata(start,end):
	
	out = dijkstra(start, end)
	print(out)
	data = {}
	aux=[]
	while len(out)>1:
		aux.append(out[0])
		out = out[1]
	
	aux.reverse()
	data['path']=aux
	path=aux
	return path

   

