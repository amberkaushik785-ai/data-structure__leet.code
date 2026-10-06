# brute-force method
class solution:
  def maxavgslidingwindow(self,nums,k):
    max_sum=float('-inf')

    for i in range(len(nums)-k+1):
      current_sum=0
      for j in range(i,i+k):
        current_sum=current_sum+nums[j]

      if current_sum > max_sum:
        max_sum = current_sum

    return max_sum/k 

nums=[1,12,-5,-6,50,3]
k=4
s=solution()
print(s.maxavgslidingwindow(nums,k))
