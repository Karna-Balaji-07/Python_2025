# count vowel strings in ranges


def solution(arr, query):
    prefix = [0]* (len(arr)+1)
    vowels = 'aeiou'
    for i in range(len(arr)):
        count = 1 if arr[i][0] in vowels and arr[i][-1] in vowels else 0
        prefix[i+1] = prefix[i] + count

    result = []
    for left, right in query:
        pos = prefix[right+1] - prefix[left]
        result.append(pos)
    return result

words = ["aba","bcb","ece","aa","e"]; queries = [[0,2],[1,4],[1,1]]
print(solution(words, queries))