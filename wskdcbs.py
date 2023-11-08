def minimum(string):
    s=[]
    count=0
    for char in string:
        if char =="{" :
            s.append(char)
        elif (char=="}" and (len(s)==0 or s[-1]=="}")):
            s.append(char)
            c1=s.pop()
            c2=s.pop()
            print(c1)
            print(c2)
            if c1!=c2:
                count+=2
            else:
                count+=1
        elif (char=="}" and s[-1]=="{"):
            s.pop()
            print(s)
        
    return count
n=input()
print(minimum(n))
                
            
        
