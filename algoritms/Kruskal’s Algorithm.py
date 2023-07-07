#Kruskal’s Algorithm

# A class to represent a disjoint set
class DisjointSet:
	parent = {}

	# perform MakeSet operation
	def makeSet(self, n):
		# create `n` disjoint sets (one for each vertex)
		for i in range(n):
			self.parent[i] = i

	# Find the root of the set in which element `k` belongs
	def find(self, k):
		# if `k` is root
		if self.parent[k] == k:
			return k

		# recur for the parent until we find the root
		return self.find(self.parent[k])

	# Perform Union of two subsets
	def union(self, a, b):
		# find the root of the sets in which elements `x` and `y` belongs
		x = self.find(a)
		y = self.find(b)

		self.parent[x] = y


# Function to construct MST using Kruskal’s algorithm
def runKruskalAlgorithm(edges, n):

	# stores the edges present in MST
	MST = []

	# Initialize `DisjointSet` class.
	# Create a singleton set for each element of the universe.
	ds = DisjointSet()
	ds.makeSet(n)

	index = 0

	# sort edges by increasing weight
	edges.sort(key=lambda x: x[2])

	# MST contains exactly `V-1` edges
	while len(MST) != n - 1:

		# consider the next edge with minimum weight from the graph
		(src, dest, weight) = edges[index]
		index = index + 1

		# find the root of the sets to which two endpoints
		# vertices of the next edge belongs
		x = ds.find(src)
		y = ds.find(dest)

		# if both endpoints have different parents, they belong to
		# different connected components and can be included in MST
		if x != y:
			MST.append((src, dest, weight))
			ds.union(x, y)

	return MST


if __name__ == '__main__':

	# (u, v, w) triplet represent undirected edge from
	# vertex `u` to vertex `v` having weight `w`
	edges = [
		(0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
		(3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
	]

	# total number of nodes in the graph (labelled from 0 to 6)
	n = 7

	# construct graph
	e = runKruskalAlgorithm(edges, n)

	print(e)
