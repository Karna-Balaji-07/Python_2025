# Monotonic decreasing stack

def monotonic(data):
    stack = []
    result = []
    for num in data:
        while stack and stack[-1] < num:
            stack.pop()
        if stack:
            result.append(stack[-1])

        stack.append(num)
    return result

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(monotonic(nums))