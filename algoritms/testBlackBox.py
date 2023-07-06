
#
# """
# This is a sample Python script.
#
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# """
import heapq
from collections import defaultdict
import sys
import heapq

def shortest_path(graph):
    num_vertices = len(graph)
    dist = [sys.maxsize] * num_vertices
    dist[0] = 0
    pq = [(0, 0)]
    while pq:
        weight, vertex = heapq.heappop(pq)
        if dist[vertex] < weight:
            continue
        for neighbor, edge_weight in graph[vertex]:
            new_dist = dist[vertex] + edge_weight
            if dist[neighbor] > new_dist:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist




