# sets

lists = [1,2,4,6,8,9,3,5,6,7,3,4,5,6,7,5,4,3]
seta = set(lists)
print(seta)

setb = set()
setb.add(10)
setb.add((20,30,40,50,60,70,80))
print(setb)

setc = set()
for i in range(10):
    setc.add(i)
print(setc)
setc.update([11,12,13,14,15])
print(setc)

setc.discard(11)
print(setc)
setc.remove(12)
print(setc)
setc.pop()
print(setc)
