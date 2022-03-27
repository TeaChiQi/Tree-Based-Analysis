class SegmentTree:
	"""
	Segment tree to store numbers and their segment summation.
	The storage is 2n (first half for summation, second half for original numbers).
	update/sumrange takes log(n)
	"""

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.num_size = len(nums)
        # second half of the tree is the original num list
        self.tree_nodes = [0]*len(nums) + self.nums
        # iteration to fill in the first half
        for i_ in range(1, len(nums))[::-1]:
            # sum the children 2i, 2i+1
            self.tree_nodes[i_] = self.tree_nodes[i_<<1] + self.tree_nodes[i_<<1|1]
        print(self.tree_nodes)
		

    def update(self, index: int, val: int) -> None:
        n = self.num_size + index
        diff = val - self.tree_nodes[n]
        # update all parents
        while n:
            self.tree_nodes[n] += diff
            n >>= 1
            

    def sumRange(self, left: int, right: int) -> int:
        left += self.num_size
        right += self.num_size
        sum_range = 0
        while left <= right:
            # if l is right child, add, then one level up
            if (left%2==1):
                sum_range += self.tree_nodes[left]
                left += 1
            # if r is left child, add, then one level up
            if (right%2==0):
                sum_range += self.tree_nodes[right]
                right -= 1
            # parent is cur//2
            left >>= 1
            right >>= 1
        return sum_range


