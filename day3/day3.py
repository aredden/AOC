import dill as pkl
import numpy as np

arr = pkl.load(open("arr.pkl", "rb"))
def part_one():
    gammas = []
    epsilons = []
    for nerp in range(arr.shape[1]):
        o = np.median(arr[:,nerp])
        gammas.append(int(o))
        epsilons.append(int(abs(1-o)))
    gammas = int("".join([str(i) for i in gammas]), 2)
    epsilons = int("".join([str(i) for i in epsilons]), 2)
    print("Gamma: {}".format(gammas))
    print("Epsilon: {}".format(epsilons))
    print("Product: {}".format(gammas * epsilons))

def part_two():
    oxy = arr.copy()
    scrub = arr.copy()
    
    # OXY
    for nerp in range(arr.shape[1]):
        if len(oxy) <= 1:
            break
        o = 1 if np.sum(oxy[:,nerp]) / oxy.shape[0] >= 0.5 else 0
        oxy = np.array([row for row in oxy if row[nerp] == o])
    
    # SCRUB
    for nerp in range(arr.shape[1]):
        print("Size of list: {}".format(len(scrub)))
        print(scrub)
        
        if len(scrub)  <= 1:
            break

        o = 0 if np.sum(scrub[:,nerp]) / scrub.shape[0] >= 0.5 else 1
        
        scrub = np.array([row for row in scrub if row[nerp] == o])
    
    print("Oxy solution  : {}".format(oxy))
    print("Scrub solution: {}".format(scrub))
        
    oxy = int("".join([str(i) for i in oxy[0]]), 2) if len(oxy) > 0 else 23
    if len(scrub) != 1:
        scrub = 10
    else:
        scrub = int("".join([str(i) for i in scrub[0]]), 2)
    print("Oxy result  : {}".format(oxy))
    print("Scrub result: {}".format(scrub))
    print("Product: {}".format(oxy * scrub))
part_two()