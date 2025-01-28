import itertools
for _ in range(int(input())):
    n = int(input())
    ds = [str(i) for i in range(n,0,-1)]
    ds_new = list(itertools.permutations(ds))
    print(len(ds_new))
    for j in ds_new:
        print(''.join(j),end = ' ')
    print()
    
