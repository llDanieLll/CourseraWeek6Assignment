def count_char(str1):
    dict_0 ={}
    for n in str1:
        keys = dict_0.keys()
        if n in keys:
            dict_0[n] += 1
        else:
            dict_0[n]   =1
    return dict_0

       
#main
print (count_char('google'))
