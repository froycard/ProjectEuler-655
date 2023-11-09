import time

def flip(n): return int(str(n)[::-1])
def is_pal(n):  return n == flip(n)
def rev(n,m): return flip(n)*10**(m-len(str(n)))

mod=10000019


def gen(n):
    e={0:[0],1:[0,1,2,3,4,5,6,7,8,9]}
    e1=[0]
    for i in range(10,100):
        if is_pal(i):
            e1.append(i)
    e[2]=e1
    e2=[0,10,20,30,40,50,60,70,80,90]
    for i in range(100,1000):
        if is_pal(i):
            e2.append(i)
    e[3]=e2
    ad = ((i*10**(n-n//4)+flip(i))%mod for i in range(10**(n//4-1),10**(n//4)))
    bc = (((rev(i,n//4)*10**(n//4+n%4)+i+j*10**(n//4))*10**(n//4))%mod for i in range(10**(n//4)) for j in e[n%4])
    AD={}
    BC={}
    for i in ad:  
        if i in AD:   
            AD[i]+=1  
        else:   
            AD[i]=1   
    for i in bc:  
        if i in BC:   
            BC[i]+=1
        else:   
            BC[i]=1
    counter=0
    for i in AD:
        #tmp=mod-i
        tmp=(mod-i)%mod
        if tmp in BC: counter+=AD[i]*BC[tmp]
    print(n,':',counter)
    return counter
count=[]
start=time.time()
for i in range(16,33):
    count.append(gen(i))
print("***************************")
print("SOL:",sum(count))
print("done")
print("elapsed time:",time.time()-start)