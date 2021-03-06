import bitarray
def sieve(n):
    """This bitarray sieve uses a strange new pattern in the composites"""
    b=bitarray.bitarray([1]*(n+1))
    x=int(n**.5)+1
    for k in range(2,x):
        if b[k]:
            f=k+1 #this line is indexing error
            e=n//k +1 
            for g in range(f,e):
                if b[g]:
                    b[g*k]=0    
    return sorted(list(to_numbs(b)-squares_set(b)))

def squares_set(ba):
    """this returns a set of all primes**2.
note 0**2==0, 1**2==1"""
    return {i**2 for i in range(int(len(ba)**.5)+1) if ba[i]}

def to_numbs(b_ar):
    """converts the bit array to a set of numbers"""
    return {i for i in range(len(b_ar)) if b_ar[i]}
if __name__=="__main__":
    print(sieve(100))

def normal_sieve(n):
    """This is your standard sieve of eratosthense"""
	s=bitarray.bitarray([1]*(n+1)) #alternatively s=set()
	for i in range(2,n//2):
		for d in range(i**2,n,i):
			s[d]=0 #alternatively set.add(d)
	return to_numbs(s) #alternatively return filter(lambda x: not s.__contains__(x),range(n+1))
