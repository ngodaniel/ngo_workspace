msg = "Hello World"
print(msg)

def countSetBits(n):
    count=0
    while(n):
        count+=n&1 #count = count + n&1
        print(count)
        n>>=1 #n=n>>1
    return count

print(countSetBits(9))
