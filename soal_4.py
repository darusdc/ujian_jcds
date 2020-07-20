def hollowTriangle(x):
    a = 0
    c=''
    for i in range(1,x) :
        for j in range(i,x) : 
            c+="_" 
        while (a != (2 * i - 1)) : 
            if (a == 0 or a == 2 * i - 2) : 
                c+="#" 
            else : 
                c+='_' 
            a = a + 1
        for j in range(i,x) : 
            c+="_"
        a = 0; 
        c+='\n'  
    for i in range(0, (x * 2)-1) : 
        c+="#" 
    return c
print(hollowTriangle(4))