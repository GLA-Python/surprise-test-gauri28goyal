x=eval(input())
d={}
for g in range(len(x)):
    for i in x:
        
        if type(x[i])!= dict:
              d[i]=x[i]
    else:
        for q in range(len(x[i])):
            for w in x[i]:
                if type(x[i][w])!=dict:
                    r=i+"."+w
                    d[r]=x[i][w]
    
                
                else:
                    for u in x[i][w]:
                    
                
                        e=i+"."+w+"."+u
                        d[e]=x[i][w][u]
                    
                       
       
print(d)
            
        
        
    

