
# Solution - 1 (Dont' use)
class MKAverage:

    def __init__(self, m: int, k: int):
        
        from queue import PriorityQueue
        import queue
        import heapq
        
        self.m = m
        self.k = k
        self.q = []
        self.sum = 0
        self.counter = 0
        
        

    def addElement(self, num: int) -> None:
        
        self.q.append(num)
        self.sum += num
        self.counter += 1

    def calculateMKAverage(self) -> int:
        
        
        if self.counter < self.m:
            return -1
        
        q_m = self.q[-self.m:][:]
        q_m = sorted(q_m)
        
        return floor(sum(q_m[self.k:-self.k]) / (self.m - 2 * self.k))
        
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()








# Solution -2 
class MKAverage:

    def __init__(self, m: int, k: int):
        
        from sortedcontainers import SortedList
        self.m = m
        self.k = k
        self.sl = SortedList()
        self.q = deque()
        
        

    def addElement(self, num: int) -> None:
        self.sl.add(num)
        self.q.append(num)
        
        if len(self.sl)>self.m:
            lr = self.q.popleft()
            self.sl.remove(lr)
            

    def calculateMKAverage(self) -> int:
        
        if len(self.sl) < self.m:
            return -1
        return sum(self.sl[self.k:-self.k]) // (self.m - 2 * self.k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()




# Solution - 3
class MKAverage:

    def __init__(self, m: int, k: int):
        from sortedcontainers import SortedList
        self.m, self.k = m, k
        self.queue = deque()
        self.sl = SortedList()
        self.total = self.left_k = self.right_k = 0
        

    def addElement(self, num: int) -> None:
        
        if len(self.sl) < self.m-1:
            self.sl.add(num)
            self.queue.append(num)
            self.total += num
        elif len(self.sl) == self.m-1:
            self.sl.add(num)
            self.queue.append(num)
            self.total += num
            self.left_k = sum(self.sl[:self.k])
            self.right_k = sum(self.sl[-self.k:])
        else:
            
            # add element, update left_k, right_k
            index = self.sl.bisect_left(num)
            if index < self.k:
                self.left_k += num
                self.left_k -= self.sl[self.k-1]

            if index > len(self.sl) - self.k:
                self.right_k += num
                self.right_k -= self.sl[len(self.sl) - self.k]

            self.sl.add(num)
            self.total += num
            self.queue.append(num)
            
            
            
            if len(self.sl) > self.m:
                
                num = self.queue.popleft()
                index = self.sl.index(num)
                print(num, index)
                
                if index < self.k:
                    self.left_k -= num
                    self.left_k += self.sl[self.k]
                    
                if index > self.m - self.k:
                    self.right_k -= num
                    self.right_k += self.sl[self.m - self.k]
                
                self.total -= num
                self.sl.remove(num)            
        
        

    def calculateMKAverage(self) -> int:
        if len(self.sl) < self.m:
            return -1
        return (self.total - self.left_k - self.right_k) // (self.m - 2 * self.k)
    
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
