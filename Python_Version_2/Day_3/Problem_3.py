# 151. Reverse A String

def solution1(s):
    arr = s.split()
    return " ".join(arr[::-1])

s = "Hello to the world"
print(solution1(s))

def reverse_words(str):
    stack = []
    word = ""

    # Iterate through the string
    for ch in str:
        
        # If not a dot, build the current word
        if ch != '.':
            word += ch
        
        # If we see a dot, push the word into the stack
        elif word:
            stack.append(word)
            word = ""

    # Last word remaining, push it to stack
    if word:
        stack.append(word)

    # Rebuild the string from the stack
    return ".".join(stack[::-1])

if __name__ == "__main__":
    str = "..geeks..for.geeks."
    print(reverse_words(str))