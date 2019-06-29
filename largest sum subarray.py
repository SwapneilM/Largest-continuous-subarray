''''l=["Delhi", "GOA"]

l1=["Goa","Delhi"]
l1.sort()
print(l1)
print(l)
print("Hell")'''

l=[-12,-3,5,6,-6,-9,10]

#print(len(l))
#for
print(__file__)
exit()
def find_pos(l1,i1):

    for k in range(i1,len(l1)):
        #print("find pos in k=",k)
        if l1[k]>0:
            return k
        

i=find_pos(l, 0)
if i is None:
    print("largest sum of  sub-array",max(l))
    print("It start with: "+str(l.index(max(l)))+" and ends with: "+str(l.index(max(l))))
    print("It starting indexis: "+str(max(l))+" and ending index is: "+str(max(l)))
    exit()
  



#exit()

max=l[i]
sum=l[i]
start=i
end=i

j=i
skip=0

while j<len(l)-1:
    print("sum=",sum)
    print("l[j+1]=",l[j+1])
    sum1=sum+l[j+1]
    print("after sum1",sum1)
    if sum1<0 :
        #print("before j=",j)
        j=find_pos(l, j+1)
        #print("after j=",j)
        start1=j
        skip+=1
        if j is None:
            print("largest sum of  sub-array",sum)
            print("It start with: "+str(l[start])+" and ends with: "+str(l[end]))
            print("It starting index is: "+str(start)+" and ending index is: "+str(end))
            exit()
        #changed info after skip
        max=l[j]
        sum=l[j]
        start=j
        end=j
        
        continue
    
    if sum1>max:
        print("lololololololo")
        print(sum1)
        print(max)
        print(skip)
        if skip>0: 
            sum=sum1
            end=j+1
            start=start1
            max=sum
            skip=0
        else:
            sum=sum1
            end=j+1
            max=sum
            
            
    j+=1    
        
print("largest sum of  sub-array",sum)
print("It start with: "+str(l[start])+" and ends with: "+str(l[end]))
print("It starting index is: "+str(start)+" and ending index is: "+str(end))


