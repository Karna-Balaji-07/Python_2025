# Panagram

def panagram(s):
    s = s.lower()
    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in s:
            return False
    return True

s =  "Bawds jog, flick quartz, vex nymph"
print(panagram(s))