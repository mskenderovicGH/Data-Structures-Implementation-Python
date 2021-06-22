# Class Heap will implement abt of priority queue
# parent is always greater/smaller than children
capacity = 10
class Heap:

    def __init__(self):
        self.heap_size = 0
        self.heap = [0]*capacity

# after insertion we should check on the parent and swap them if possible
    def insert(self,item):
        if self.heap_size == capacity:
            return

        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size +1

        self.fix_up(self.heap_size-1)

    def fix_up(self, index):
        parent_index = (index-1)//2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    def get_max(self):
        return self.heap[0]

# after removing/moving the item the greater child should take its place
    def poll(self):

        max_item = self.get_max()
        self.heap[0], self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
        self.heap_size = self.heap_size - 1
        self.fix_down(0)

        return max_item

    def fix_down(self, index):

        index_left = 2 * index + 1
        index_right = 2 * index + 2

        largest_index = index

        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            largest_index = index_left

        if index_right<self.heap_size and self.heap[index_right] > self.heap[largest_index]:
            largest_index = index_right

        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap [largest_index], self.heap[index]
            self.fix_down(largest_index)

    def heap_sort(self):
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)

if __name__ == '__main__':

    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    heap.heap_sort()
