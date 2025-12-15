# Find the maximum number of vowels in a substring og given length


def solution1(arr,k):
    count = 0
    left = 0
    vowels = 'aeiou'
    result = 0
    for right in range(len(arr)):
        print(f'Current element : {arr[right]}')
        if arr[right] in vowels:
            count += 1
            print(f'Count for {arr[right]} : {count}')
        if right - left == k:
            if arr[left] in vowels:
                count -= 1
            left+= 1

        result = max(count, result)
        print(f'Result : {result}')
    return result

def solution2(arr,k):
    count = 0
    result = 0
    vowels = 'aeiou'
    for i in range(len(arr)):
        if arr[i] in vowels:
            count += 1
        if i >= k:
            if arr[i-k] in vowels:
                count  -= 1

        result = max(count, result)

    return result

s = "abciiidef"; k = 3
print(solution1(s,k))
s = "aeiou"; k = 2
print(solution1(s,k))