"""  binaryHeapClass 
version 3 - to work with Dijkstra's; 
entries are (priority, label/key) tuples
"""

class binaryHeap():
    def __init__(self):
        self.heapList = [(0,0)]    # (priority, label or key)
        self.currentSize = 0
        
    def percUp(self,i):
        # i is list position of item
        while i > 1:   # while below root
            percValue = self.heapList[i][0]
            parentValue = self.heapList[i //2][0]
            if percValue < parentValue:
                self.heapList[i // 2], self.heapList[i] =       \
                    self.heapList[i], self.heapList[i // 2]
                print('Just swapped in perc up')
                print(self.heapList)
            i = i // 2      # go up to parent's level
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        print('Heap list updated with inserted element:')
        print(self.heapList)
        self.percUp(i = self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:   # not in a leaf
            minChildInd = self.minChild(i)
            if self.heapList[i][0] > self.heapList[minChildInd][0]:
                self.heapList[i],self.heapList[minChildInd] =  \
                    self.heapList[minChildInd], self.heapList[i]
                print('A perc down swap results in:')
                print(self.heapList)
            i = minChildInd
            
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:  # i has only 1 child
            return i * 2
        else:
            if self.heapList[i*2][0] < self.heapList[i*2+1][0] :
                return i * 2
            else :
                return i * 2 + 1
                
    def deleteMin(self):
        if self.currentSize == 0:
            minIndItem = None    
        elif self.currentSize == 1:
            # last item; pop it off
            minIndItem = self.heapList.pop()
            self.currentSize = self.currentSize - 1
        else:
            minIndItem = self.heapList[1]
            # Replace 1st item with last item
            self.heapList[1] = self.heapList.pop()
            self.currentSize = self.currentSize - 1
            # Percolate the new root node downwards
            self.percDown(1)
        return minIndItem
        
    def buildHeap(self,alist):
        i = len(alist) // 2             # start in middle of list
        self.currentSize = len(alist)
        self.heapList = [(0,0)] + alist[:]
        print(self.heapList)
        while (i > 0):
            self.percDown(i)
            i = i - 1
            
    def isEmpty(self):
        return self.currentSize == 0   

    def raisePriority(self,curPri, itemKey, newPri):
        # Raise the priority of an item
        # First, find its location in the heap.
        ind = self.heapList.index((curPri, itemKey))         
        # Set its priority to the new value
        self.heapList[ind] = (newPri, itemKey)
        # Attempt to percolate it up due to new higher priority
        self.percUp(i = ind)
            
def main():
    from string import ascii_lowercase as lowers
    import random
    b = binaryHeap()
    priorities = [9,6,5,2,3]
    b.buildHeap(list(zip(priorities,
                [random.choice(lowers) for _ in range(len(priorities))])))
    print()
    b.insert((4,'hello'))
    print()
    while b.currentSize > 0:
        print('Delete the min item:')
        print(b.deleteMin())

#    b = binaryHeap()
#    b.buildHeap([9,6,5,1,7,2,4,3,8])
#    print(b.heapList)
    
# main()