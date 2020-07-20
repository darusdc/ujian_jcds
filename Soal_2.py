def create_phone_number(x):
    c='('
    if len(x)<10 or len(x)>10:
        return 'Number invalid'
    else:
        for i in range(len(x)):  
            if x[i]>=10:
                return 'Number invalid, there is 2 digit number in one index'
            else:
                c+=f'{x[i]}'
                if i==2:
                    c+=f') '
                elif i==5:
                    c+=f'-'
    return c
print(create_phone_number([0,2,5,6,8,4,8,7,8,1]))
