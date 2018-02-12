# P3 of hw1
import snap
'''
# 1) The number of weakly connected components
g1 = snap.LoadEdgeList(snap.PNGraph, "stackoverflow-Java.txt", 0, 1)
Components = snap.TCnComV()
snap.GetWccs(g1, Components)
cnt = 0

for ele in Components:
	#print "Size of Component: %d" % (ele.Len())
	cnt += 1
print "1) number of weakly connected components: %d" % (cnt)



# 2) The number of edges and the number of nodes
g2 = snap.LoadEdgeList(snap.PNGraph, "stackoverflow-Java.txt", 0, 1)
MxWcc = snap.GetMxWcc(g2)
cnt_edge = 0
cnt_node = 0

for ele in MxWcc.Edges():
	cnt_edge += 1
for ele in MxWcc.Nodes():
	cnt_node += 1
print "2) Edges = %d, Node = %d"%(cnt_edge, cnt_node)

# 3)
g3 = snap.LoadEdgeList(snap.PNGraph, "stackoverflow-Java.txt", 0, 1)
PRankH = snap.TIntFltH()
snap.GetPageRank(g3, PRankH)
max = 0
max_index = [0, 0, 0]

for ele in PRankH:
	if PRankH[ele] > max:
		max = PRankH[ele]
		max_index[0] = ele

print max_index[0]

max = 0
for ele in PRankH:
	if PRankH[ele] > max and ele != max_index[0]:
		max = PRankH[ele]
		max_index[1] = ele

print max_index[1]

max = 0
for ele in PRankH:
	if PRankH[ele] > max and ele != max_index[0] and ele != max_index[1]:
		max = PRankH[ele]
		max_index[2] = ele

print "Top 3 most central nodes by PageRank Score", max_index[2]
'''
# 4)
g4 = snap.LoadEdgeList(snap.PNGraph, "stackoverflow-Java.txt", 0, 1)
hub = snap.TIntFltH()
aut = snap.TIntFltH()
snap.GetHits(g4, hub, aut)

# Hubs
max = 0
max_index_hub = [0, 0, 0]
max_index_aut = [0, 0, 0]

for ele in hub:
	if hub[ele] > max:
		max = hub[ele]
		max_index_hub[0] = ele


max = 0
for ele in hub:
	if hub[ele] > max and ele != max_index_hub[0]:
		max = hub[ele]
		max_index_hub[1] = ele


max = 0
for ele in hub:
	if hub[ele] > max and ele != max_index_hub[0] and ele != max_index_hub[1]:
		max = hub[ele]
		max_index_hub[2] = ele

print "Top 3 Hub Nodes:\t", max_index_hub

# Authorities
max = 0

for ele in aut:
	if aut[ele] > max:
		max = aut[ele]
		max_index_aut[0] = ele

max = 0
for ele in aut:
	if aut[ele] > max and ele != max_index_aut[0]:
		max = aut[ele]
		max_index_aut[1] = ele

max = 0
for ele in aut:
	if aut[ele] > max and ele != max_index_aut[0] and ele != max_index_aut[1]:
		max = aut[ele]
		max_index_aut[2] = ele

print "Top 3 Auth Nodes:\t", max_index_aut

