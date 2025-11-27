# Print names N times using recursion

def func1(n, name):
    if n == 0:
        return
    print(name)
    func1(n-1,name)

n = 5
name = "Hello"
func1(n,name)