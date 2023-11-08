def minimum(s,e,count,mini) :
    
    if len(s)==0 and len(e)==0:
        return count
    
    while(len(s)!=0):
        print(s)
        count+=1 
        if s[0]==mini :
            s.pop(0)
            mini+=1
            
        else:
            x=s.pop(0)
            e.append(x)
    minimum(s,e,count,mini)

    while(len(e)!=0):
        count+=1
        if e[-1]==mini:
            e.pop()
            mini+=1
        else:
            x=e.pop()
            s.append(x)
    minimum(s,e,count,mini)
    
            
            
            
        

n=int(input())
s=[]
e=[]
for i in range(n):
    x=int(input())
    s.append(x)

print(minimum(s,e,0,1))







    
    
