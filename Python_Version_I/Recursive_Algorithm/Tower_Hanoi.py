# Tower of Hanoi

def solution(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return 
    solution(n-1, from_rod,aux_rod,to_rod)
    print(f'Move disk {n} from {from_rod} to {to_rod}')
    solution(n-1, aux_rod,to_rod,from_rod)

n = 3
solution(n,'A','B','C')