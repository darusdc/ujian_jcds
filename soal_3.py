def Sort_odd_even(x=list):
    odd=list(sorted(filter(lambda a: a%2==0 ,x),reverse=True))
    even=list(sorted(filter(lambda a: a%2!=0 ,x)))
    even_list=[i for i in range(1,len(x)+1,2) if i>3]
    odd_list=[i for i in range(0,len(x)+1,2) if i>2]
    result=[]
    print(even_list)
    print(odd_list)
    print(odd)
    for i in range(len(x)+1):
        if i==0 or i==1:
            result.append(even[0])
            even.pop(0)
        elif i==2 or i==3:
            result.append(odd[0])
            odd.pop(0)
        if len(even_list)!=0:
            if i==even_list[0]:   
                if len(even)==0:
                    result.append('ganjil')
                else:    
                    result.append(even[0])
                    even.pop(0)
                    even_list.pop(0)
        if len(odd_list)!=0:
            if i==odd_list[0]:
                if len(odd)==0:
                    result.append('genap')
                else:
                    result.append(odd[0])
                    odd.pop(0)
                    odd_list.pop(0)
    return result
print(Sort_odd_even([5,3,2,8,1,4]))