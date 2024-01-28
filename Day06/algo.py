sample = [5, 1, 3, 7, 9, 2]

for x in range(0, len(sample)-1) :
    for y in range(x+1, len(sample)) :  
        if sample[x] > sample[y] :
            sample[x],sample[y] = sample[y],sample[x]
print(sample)
    
    