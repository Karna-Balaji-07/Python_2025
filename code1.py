import sys
sys.setrecursionlimit(300000)
MOD = 10**9 + 7

class LinearBasis:
    LOG = 60
    def __init__(self):
        self.a = [0] * self.LOG
        self.sz = 0

    def insert(self, x: int):
        for i in reversed(range(self.LOG)):
            if not (x >> i) & 1:
                continue
            if self.a[i] == 0:
                self.a[i] = x
                self.sz += 1
                return
            x ^= self.a[i]

    def can_toggle_bit(self, b: int) -> bool:
        for i in range(b, self.LOG):
            if self.a[i] and ((self.a[i] >> b) & 1):
                return True
        return False


def dfs(u: int, graph, xorDist, vis):
    vals = []
    basis = LinearBasis()
    stack = [u]
    vis[u] = True

    while stack:
        x = stack.pop()
        vals.append(xorDist[x])
        for y, w in graph[x]:
            if not vis[y]:
                vis[y] = True
                xorDist[y] = xorDist[x] ^ w
                stack.append(y)
            else:
                cyc = xorDist[x] ^ xorDist[y] ^ w
                basis.insert(cyc)
    return vals, basis


def solve():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    xorDist = [0] * (n + 1)
    vis = [False] * (n + 1)
    ans = 0

    for i in range(1, n + 1):
        if vis[i]:
            continue
        vals, basis = dfs(i, graph, xorDist, vis)
        sz = len(vals)
        k = basis.sz

        pow2k = pow(2, k, MOD)
        half = (MOD + 1) // 2  # modular inverse of 2

        for b in range(60):
            cnt1 = sum((x >> b) & 1 for x in vals)
            cnt0 = sz - cnt1
            bitVal = (1 << b) % MOD

            if basis.can_toggle_bit(b):
                pairCount = sz * (sz - 1) // 2 % MOD
                add = pairCount * pow2k % MOD * bitVal % MOD * half % MOD
            else:
                pairCount = cnt0 * cnt1 % MOD
                add = pairCount * pow2k % MOD * bitVal % MOD
            ans = (ans + add) % MOD

    print(ans % MOD)


if __name__ == "__main__":
    solve()
