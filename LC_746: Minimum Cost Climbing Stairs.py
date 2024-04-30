"""You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost,
you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Explanation: This program uses Dynamic Programming concept. Please refer to program 2 of the video:
https://www.youtube.com/watch?v=_i4Yxeh5ceQ&ab_channel=NeetCode"""


def minCostClimbingStairs(cost_func):
    """
    :type cost_func: List[int]
    :rtype: int
    """
    cost_func.append(0)

    for i in range(len(cost_func) - 3, -1, -1):
        cost_func[i] += min(cost_func[i + 1], cost_func[i + 2])

    return min(cost_func[0], cost_func[1])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))
