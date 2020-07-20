def Hashtag(x:''):
    c=x.split()
    if len(c)<=1:
        return False
    else:
        return '#'+ "".join(map(lambda a: str(a).capitalize(),c))
print(Hashtag("Hello World    and  good People"))