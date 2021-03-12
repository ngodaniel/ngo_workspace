#python3 program to implment direct index mapping with negative values allowed

#searching if X is present in the given array or not
def search(X):
    if X>=0:
        return has[X][0]==1
        
    #if X is negative take the absolute value of X
    X=abs(X)
    return has[X][1]==1
    
def insert(a,n):
    for i in range(0,n):
        print(a[i])
        if a[i]>=0:
            has[a[i]][0]=1
        else:
            has[abs(a[i])][1]=1
            
#Driver code
if __name__=="__main__":
    a=[-1,9,-5,-8,-5,-2]
    n=len(a)    #size of array a
    
    MAX=10
    
    #since array is global, it is initialized as 0
    has=[[0 for i in range(2)]for j in range(MAX+1)]
    insert(a,n)
    X=-5
    print(has)
    if search(X)==True:
        print("Present")
    else:
        print("Not Present")
        