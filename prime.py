r=100  
li=[]
start_with= []
total=0

for a in range(2,r+1):  
    k=0  
    for i in range(2,a//2+1):  
        if(a%i==0):  
            k=k+1  
    if(k<=0):  
        li.append(a) 

for i in li:
   if i%10==7:
      start_with.append(i)

for t in start_with:
   total+=t
print(total)

