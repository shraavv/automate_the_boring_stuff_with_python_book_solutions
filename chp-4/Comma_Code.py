def comma(lst):
    if len(lst)==0:
        return ''
    elif len(lst)==1:
        return str(lst[0])
    else:
        string=''
        for i in lst:
            if lst.index(i)==len(lst)-1:
                string=string+' and '+str(i)
            elif lst.index(i)==0:
                string+=str(i)
            else:
                string=string+', '+str(i)
        return string

lst=['apples', 'bananas', 'tofu', 'cats']
print(comma(lst))
