import snap

# This is the solution from Guo Shan, who is a pretty girl and genius
# Phd student. Her solution helps me a lot to impove my idea!

# 	1)The number of weakly connected components in the network
'''
# load the edge list
# LoadEdgeList(PGraph, InFNm, SrcColId, DstColId, Separator)
	a) PGraph(graph class), one of the following, PNGraph, PNEANet, or PUNGpraph
	b) InFNm(String): input file name, string type
	c) SrcColId(int): column number which contains source vertex
	d) DstColId(int): column number which contains destination vertex
	e) Separator(char): Column separator
'''
G = snap.LoadEdgeList(snap.PNGraph, "stackoverflow-Java.txt", 0, 1)

# TCnComV, a vector of connected components
# A vector of all the communities that are detected by the CNM method. Each 
# community is represented as a vector of node IDs

Components = snap.TCnComV()

'''
GetWccs(Graph, CnComV)
return all weakly connected compontents in Graphs

Parameters:
	Graph: graph (input)
		A Snap.py graph or a network.

	CnComV: TCnComV, a vector of connected components (output)
		Vector of all weakly-connected components. Each component consists of a 
		TIntV vector of node ids.

'''
snap.GetWccs(G, Components)
print "Number of weakly connected components: %d" %(len(Components))

# 2) number of edges and number of nodes in largest weakly connected component

'''
GetMxWcc(Graph)
return a graph representing the largest weakly connected component in Graph

Parameters:
	Graph: graph (input)
		A Snap.py graph or a network

Return value:
	graph
		A Snap.py graph or a network representing the largest weakly connected 
		component in Graph.

'''
MxWcc = snap.GetMxWcc(G)

# GetNodes() return how many nodes(int) 
# GetEdges() return how many edges(int)
print "Number of nodes in the MxWcc:", MxWcc.GetNodes()
print "Number of edges in the MxWcc:", MxWcc.GetEdges()

# 3)  The top 3 most central nodes in the network by PagePank scores

# TIntFltH, a hash table with int keys and float values
PRankH = snap.TIntFltH()
'''
GetPageRank(Graph, PRankH, C=0.85, Eps=1e-4, MaxIter=100)
	Computes the PageRank score of every node in Graph. The scores are stored 
	in PRankH.

Parameters:
	Graph: graph (input)
		A Snap.py graph or a network.

	PRankH: TIntFltH, a hash of int keys and float values (output)
		PageRank scores. Keys are node IDs, values are computed PageRank scores.

	C: float (input)
		Damping factor.

	Eps: float (input)
		Convergence difference.

	MaxIter: int (input)
		Maximum number of iterations.
'''
snap.GetPageRank(G, PRankH)

# SortByDat(): Sorts the hash table based on the values
PRankH.SortByDat(False)

i = 0

# BegI(): Returns an iterator pointing to the first element in the vector
itr = PRankH.BegI()
print "The top 3 most central nodes in the network by PagePank scores:"
while i < 3:
    print "Node", itr.GetKey()
    itr.Next()
    i += 1

NIdHubH = snap.TIntFltH()
NIdAuthH = snap.TIntFltH()
snap.GetHits(G, NIdHubH, NIdAuthH)
NIdHubH.SortByDat(False)
i = 0
itr = NIdHubH.BegI()
print "The top 3 hubs in the network by HITS score:"
while i < 3:
    print "Node", itr.GetKey()
    itr.Next()
    i += 1

NIdAuthH.SortByDat(False)
i = 0
itr = NIdAuthH.BegI()
print "The top 3 authorities in the network by HITS score:"
while i < 3:
    print "Node", itr.GetKey()
    itr.Next()
    i += 1
