class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = []
        
        
        
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])
        
        return window_sum / float(min(len(queue), size))
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)