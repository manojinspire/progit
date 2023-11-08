def minimum(m,h,g):

    def find(i,j):

        if i==m or j==m:
            return 1e9

        if h[i]==g[j]:

            return find(i+1,j+1)

        else:

            if h[i]<g[j]:
                return 1e9
            else:
                h[i]=h[i]-1
                if i+1<m:
                    h[i+1]=h[i+1]-1

                ans=1+find(i,j)

                h[i]=h[i]+1
                if i+1 < m:
                    h[i+1]=h[i+1]+1
                ans=min(ans,find(i+1,j+1))
                return ans 
                









    return find(0,0)





m=3
h=[2,3,2]
g=[1,1,1]
print(minimum(m,h,g))
