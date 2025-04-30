# MaxHeap data structure

class MaxHeap:
    arr = []
    maxSize = 0
    heapSize = 0

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.arr = [None]*maxSize
        self.heapSize = 0

    def maxHeapify(self,i):
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i
        if left < self.heapSize and self.arr[left] > self.arr[i]:
            largest = left
        if right < self.heapSize and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            temp = self[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.maxHeapify(largest)

    def parent(self,i):
        return (i-1)//2
    def left_child(self,i):
        return (2*i+1)
    def right_child(self,i):
        return (2*i+2)
    
    def removeMax(self):
        if self.heapSize <= 0:
            return None
        if self.heapSize  == 1:
            self.heapSize -= 1
            return self.arr[0]
        
        root = self.arr[0]
        self.arr[0] = self.arr[self.heapSize-1]
        self.heapSize -= 1
        self.maxHeapify(0)
        return root
    
    
