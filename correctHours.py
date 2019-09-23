def correctHours(A,B,C,D):
    count=0
    myList=[]
    s=str(A)+str(B)+str(C)+str(D)
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if i!=j: 
               for k in range(0,len(s)):
                   if j!=k and i!=k:
                      for l in range(0,len(s)):
                           if k!=l and j!=l and i!=l:
                           
                             combinedString=s[i]+s[j]+s[k]+s[l]
                            #  print(strin)
                             if(s[i]+s[j] <=str(23) and s[k]+s[l]<=str(60) and (combinedString not in myList)):
                                  myList.append(combinedString) 
                                  count=count+1
                             if(s[i]+s[j] == '24'  and   s[k]+s[l] == '00' and (combinedString not in myList)):
                                   count=count+1
                                   myList.append(combinedString) 
                                    
    return count                             
# print(correctHours(6,2,4,7))