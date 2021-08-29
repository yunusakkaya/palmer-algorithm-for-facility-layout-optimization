import numpy as np

m=int(input("kaç makine var?:"))
n=int(input("kaç iş var?:"))

s=[0]*n

tablo=np.array([[0]*m]*n,dtype=int)
tablo=tablo.reshape(n,m)
print("oluşturduğunuz tablo:\n",tablo)

for i in range(0,n):
    for j in range(0,m):
        
        tablo[i,j]=float(input("değer:"))
            
                
print("değer tablosu:\n",tablo)

for i in range(0,n):
    
    for j in range(0,m):        
        k=(m-(2*(j+1)-1))*tablo[i,j]
        s[i]=s[i]+k

    s[i]=s[i]*(-1)   
    print(s)

    
    
    
    
        
    