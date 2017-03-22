# Kadane's Algorithm
# https://www.youtube.com/watch?v=86CQq3pKSUw
def maximun_subarray(vector):
    # O (N)
    # check subarrays in ascending looking back, and storing previous subarrays

    max_current = max_global = vector[0] # initialize with the first element

    for index in xrange(len(vector)):
        max_current = max(vector[index], max_current + vector[index])
        if max_current > max_global:
            max_global = max_current

    return max_global


a = [1, -3, 2, 1, -1 ]

print maximun_subarray(a)