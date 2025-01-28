# group anagrams

MAX_CHAR=26

def hash(s):
    hashlist=[]
    freq = [0]*MAX_CHAR
    for char in s:
        freq[ord(char)-ord('a')] += 1
    for i in range(MAX_CHAR):
        hashlist.append(str(freq[i]))
        hashlist.append('$')
    return ''.join(hashlist)


def group(arr):
    result = []
    dicts = {}
    for i in range(len(arr)):
        key = hash(arr[i])
        if key not in dicts:
            dicts[key]=len(result)
            result.append([])
        result[dicts[key]].append(arr[i])
    return result


def anagrams(arr):
    dicts={}
    for word in arr:
        words = "".join(sorted(word))
        if words not in dicts:
            dicts[words] = []
        dicts[words].append(word)
    return list(dicts.values())

arr = ["act", "god", "cat", "dog", "tac"]
print(group(arr))
print(anagrams(arr))