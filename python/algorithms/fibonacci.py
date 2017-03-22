import sys


def fibonnaci_recursive(n):
    if n <= 1:
        return n

    return fibonnaci_recursive(n - 1) + fibonnaci_recursive(n - 2)

def fibonnaci_list(n):
    values_list = [0,1]

    for i in range(2, n):
        values_list.append(values_list[i-1] + values_list[i-2])

    return values_list


n = int(raw_input().strip())
# print fibonnaci_recursive(n)
print fibonnaci_list(n)[-1]