import heapq


def max_to_min_heap(heap):
    
    heapq.heapify(heap)



heap = [100, 50, 30, 20, 40, 10]
print("До:", heap)
max_to_min_heap(heap)
print("После:", heap)
