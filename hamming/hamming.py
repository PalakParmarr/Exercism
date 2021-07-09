
def distance(strand_a, strand_b):
    d=0
    
    if len(strand_a)!= len(strand_b):
        raise ValueError("not same")
    elif len(strand_a)==0:
        return 0
    else:
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                d = d+1
        return d
    
 