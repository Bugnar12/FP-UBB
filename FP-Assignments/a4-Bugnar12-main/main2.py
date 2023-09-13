"""
I will solve the second problem statement from dynamic programming which states :
Given the set of positive integers S and the natural number k, display one of the subsets of S which sum to k.
For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14.

->we take each value in order and determine whether it is worth adding into the sum or not.
->if by adding a certain number the current_sum exccedes k, that means the subset of S which sums
to k is situated before the respective number (considering the list is sorted)
"""

def sum_subset_dp(arr, k):
    n = len(arr)

    T = ([[None for i in range(k + 1)]
          for i in range(n + 1)])

    for i in range(n + 1):
        T[i][0] = True
    for j in range(1, n + 1):
        T[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, k+1):
            if j - arr[i-1] < 0:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i-1][j-arr[i-1]]

    if T[n][k]:
        m = n
        b = k
        sol = list()

        while b > 0:
            if T[m-1][b]:
                m = m - 1
            else:
                m = m - 1
                sol.append(arr[m])
                b = b - arr[m]

    sol.reverse()
    print("The subset of k-sum is :", sol)
    return T[n][k]

def subsetsum(numbers, target):
   size = 1
   subsets = []
   while size <= len(numbers):
      for combination in combinations(numbers, size):
         if sum(combination) == target:
            subsets.append(combination)
            break
      size = size + 1
   return subsets


def combinations(numbers, size):
   if len(numbers) <= 0 or size <= 0:
      yield []
   else:
      for index, number in enumerate(numbers):
         for combination in combinations(numbers[index+1:], size-1):
            yield [number]+combination

arr = [2, 3, 5, 7, 8]
k = 14
sum_subset_dp(arr, k)
print(subsetsum(arr, k))