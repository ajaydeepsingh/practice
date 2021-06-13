import heapq
class Solution:


	def minCostToConnectSticks(sticks):
		heapq.heapify(sticks)

		res = 0

		while len(sticks)  > 1:
			first = heapq.heappop(sticks)
			second = heapq.heappop(sticks)

			res += first + second
			heapq.heapppush(sticks, first + second)


		return res