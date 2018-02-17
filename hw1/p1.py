#This is the 1st try of hw1
import snap

# I
# 1) The number of nodes in the network
g1 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
cnt = 0
for node in g1.Nodes():
	cnt += 1
print "1)There are totally %d nodes here!!!" % (cnt)

# 2) Number of self-edge
g2 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
cnt = 0
for edge in g2.Edges():
	#print "Src Node ID is %d" %(edge.GetSrcNId())
	#print "Dst Node ID is %d" %(edge.GetDstNId())
	if (edge.GetSrcNId() == edge.GetDstNId()):
		print "Gooooooooooooooooooooooooooooooooooooooood"
		cnt += 1
print "2)There are totally %d self-edges here!!!" % (cnt)


# 3) Travel all the directed edges
g3 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
cnt = 0

for e in g3.Edges():
    #print "(%d, %d)" % (e.GetSrcNId(), e.GetDstNId())
    cnt += 1
    
print "3)There are totally %d edges here!!!" %(cnt)

# 4) number of undirected edges
g4 = snap.LoadEdgeList(snap.PUNGraph, "wiki-Vote.txt", 0, 1)
cnt = 0

for e in g4.Edges():
    #print "(%d, %d)" % (e.GetSrcNId(), e.GetDstNId())
    cnt += 1
    
print "4)There are totally %d undirected edges here!!!" %(cnt)

# 5) The number of reciprocated edges
'''
Problem here is, if use snap.PUNGraph(undirected graph), each 
temp is not in All_edges set. Need to find out the reason

'''
g5 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
All_edges = set()
cnt = 0

for edge in g5.Edges():
	temp = (edge.GetSrcNId(), edge.GetDstNId())
	All_edges.add(temp)

for edge in g5.Edges():
	temp = (edge.GetDstNId(), edge.GetSrcNId())
	# print(temp in All_edges)
	if temp in All_edges:
		cnt += 1

print "5)The number of reciprocated edges: %d" %(cnt/2)

# 6)The number of nodes of zero out-degree
g6 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
cnt = 0

for node in g6.Nodes():
	if node.GetOutDeg() == 0:
		cnt += 1
print "6)The number of nodes of zero out-degree: %d" % (cnt)

# 7) The number of nodes of zero in-degree
g7 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
cnt = 0

for node in g7.Nodes():
	if node.GetInDeg() == 0:
		cnt += 1
print "7)The number of nodes of zero in-degree: %d" % (cnt)

# 8) The number of nodes with more than 10 outgoing edges
g8 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
cnt = 0

for node in g8.Nodes():
	if node.GetOutDeg() > 10:
		cnt += 1
print "8)The number of nodes with more than 10 outgoing edges: %d" % (cnt)

# 9) The number of nodes with fewer than 10 incoming edges
g9 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
cnt = 0

for node in g9.Nodes():
	if node.GetInDeg() < 10:
		cnt += 1
print "9)The number of nodes with fewer than 10 incoming edges: %d" % (cnt)

print ""

# II
# Plotting
G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)

#snap.PlotInDegDistr(G, "Stack-Java.png", "Stack-Java In Degree")
#snap.DrawGViz(G, snap.gvlDot, "G.png", "G", NIdName)

