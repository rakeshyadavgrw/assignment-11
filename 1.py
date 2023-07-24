#****************Q1***********#
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s: 
            if stack and abs(ord(stack[-1]) - ord(c)) == 32: stack.pop() #pop "bad"
            else: stack.append(c) #push "good"
        return "".join(stack)
    
    #********************Q2***********#
    class Solution:
    def removeDuplicates(self, s: str) -> str:
        idx =0
        while(idx+1<len(s)):
            if(s[idx]==s[idx+1]):
                s= s[:idx]+s[idx+2:]
                if idx > 0:
                    idx -= 1
            else:
                idx += 1
        return s
    
    #****************Q3****************#
    class StockSpanner:

    def __init__(self):
        
        # maintain a monotonic stack for stock entry
        
		## definition of stock entry:
        # first parameter is price quote
        # second parameter is price span
        self.monotone_stack = []
              
        
        
    def next(self, price: int) -> int:

        stack = self.monotone_stack
        
        cur_price_quote, cur_price_span = price, 1
        
        # Compute price span in stock data with monotonic stack
        while stack and stack[-1][0] <= cur_price_quote:
            
            prev_price_quote, prev_price_span = stack.pop()
            
            # update current price span with history data in stack
            cur_price_span += prev_price_span
        
        # Update latest price quote and price span
        stack.append( (cur_price_quote, cur_price_span) )
        
        return cur_price_span
    
    #****************Q4***********#
    class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        return sum(min(v, t[k] if i <= k else t[k] - 1) for i, v in enumerate(t))
    
    #****************Q5************#
    class ProductOfNumbers:
    def __init__(self):
        self.data = []
        self.product = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.product *= num
            self.data.append(self.product)
        else:
            self.data = []
            self.product = 1

    def getProduct(self, k: int) -> int:
        if len(self.data) < k:
            return 0
        if len(self.data) == k:
            return self.data[-1]
        else:
            return int(self.data[-1] / self.data[-1-k])
        
        #*******************Q6*************#
        def largestRectangleArea(self, bars: List[int]) -> int:
	st, res = [], 0
	for bar in bars + [-1]: # add -1 to have an additional iteration
		step = 0
		while st and st[-1][1] >= bar:
			w, h = st.pop()
			step += w
			res = max(res, step * h)

		st.append((step + 1, bar))

	return res
        
        #*****************Q7************#
        class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque() # stores *indices*
        res = []
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)
            # remove first element if it's outside the window
            if q[0] == i - k:
                q.popleft()
            # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

        #*****************Q8***************#
        class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.maxSize = k
        self.head = 0
        self.tail = -1
    def enQueue(self, val: int) -> bool:
        if self.isFull(): return False
        self.tail = (self.tail + 1) % self.maxSize
        self.data[self.tail] = val
        return True
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail: self.head, self.tail = 0, -1
        else: self.head = (self.head + 1) % self.maxSize
        return True
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.tail]
    def isEmpty(self) -> bool:
        return self.tail == -1
    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail + 1) % self.maxSize == self.head
