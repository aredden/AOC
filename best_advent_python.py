l = [int(x)for x in open("x").readlines()];calc = lambda x:sum(a<b for a,b in zip(l,l[x:]));print(calc(1),calc(3))