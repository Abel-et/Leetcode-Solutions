from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.queue = deque()
        

    def consec(self, num: int) -> bool:
        if self.val != num:
            self.queue.clear()
            return False
        else:
            self.queue.append(num)
            if len(self.queue) > self.k:
                self.queue.popleft()
            if len(self.queue) == self.k:
                return True
        return False
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)