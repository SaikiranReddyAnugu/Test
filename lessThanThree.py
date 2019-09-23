def lovelyNumbers(A,B):
    count=0
    if(A==0 and B==0):
        return 1
    for x in range(A,B+1):
        a=str(x)
        if(len(a)<3):
            count=count+1
        else:
            inc=0
            for i in range(10):
                if(a.count(str(i))>=3):
                   break
                else :
                  inc=inc+1
            if(inc==10):
                count=count+1
    return count               
                
        

print(lovelyNumbers(0,10000))