class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    m = {}

    for n in nums:
      if n not in m:
        m[n] = 1
      m[n] += 1

    heap = []
    for n in m.keys():
      heapq.heappush(heap, (m[n], n))
      if len(heap)>k:
        heapq.heappop(heap)

    res=[]
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res
