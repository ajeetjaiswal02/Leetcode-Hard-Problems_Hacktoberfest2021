arr = [8,5,2,9,5,6,3]

def heapSort(arr):
    buildMaxheap(arr)
    for endidx in reversed(range(1,len(arr))):
        swap(0,endidx,arr)
        siftDown(0,endidx - 1,arr)
    return arr

def swap(i,j,arr):
    arr[i],arr[j] = arr[j],arr[i]

def buildMaxheap(arr):
    fristParentidx = (len(arr) - 1) // 2
    for currentidx in reversed(range(fristParentidx + 1)):
        siftDown(currentidx , len(arr) - 1, arr)

def siftDown(currentidx,endidx,heap):
    childOneIdx = currentidx * 2 + 1
    while childOneIdx <= endidx:
        childTwoidx = currentidx * 2 + 2 if currentidx * 2 + 2 <= endidx else -1
        if childTwoidx > -1 and heap[childTwoidx] > heap[childOneIdx]:
            idxToSwap = childTwoidx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currentidx]:
            swap(currentidx,idxToSwap,heap)
            currentidx = idxToSwap
            childOneIdx = currentidx * 2 + 1
        else:
            return
print(heapSort(arr))