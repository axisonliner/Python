
#  File name: Roman Numerals Decoder.py
#  Developed by Yuriy Kondrashov on 2/2/20 7:46 PM
#  Date last modified: 1/22/20 11:51 PM
#  Copyright (c) 2020. All rights reserved.

# from functools import reduce
# from itertools import zip_longest
# def roman_to_int(n):
#     d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     return reduce(lambda x, y: x + y, 
#         ((-d[x], d[x])[y is '' or d[x] >= d[y]] for x, y in zip_longest(n, n[1:], fillvalue=None)))

def roman_to_int(n):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return reduce(lambda x, y: x + y, 
        ((-d[x], d[x])[y is None or d[x] >= d[y]] for x, y in map(None, n, n[1:])))


# def roman_to_int(n):
#     d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     y = 0
#     for x in range(len(n)): #xrenge(len(n))
#         try:
#             if d[n[x]] < d[n[x+1]]:
#                 y -= d[n[x]]
#             else:
#                 y += d[n[x]]
#         except IndexError:
#             y += d[n[x]]
#     return y

# return reduce(lambda x,y: x+y if x>=y else y-x , (d[c] for c in n)) -- wrong!!!

    # return sum([d[x] for x in n])
    # return [d[x] for x in n]    
    # for x, y in [(x,y) for x in n for y in n[1:]][:len(n)]:
    #     print x, y
    # for x, y in zip(n,n[1:])[::1]:
    #     print x, y
    # return [n[i*2 : (i+1)*2] for i in range(len(n)//2)]
    # return [(x,y) for x in n for y in n[1:]][:len(n)-1]
    # num = reduce(re_n, n)
    # print num
    # return num#a if a > b else b, n)
    # l = {'IV': 4, 'XX': 20, 'CM': 900, 'XC': 90, 'XL': 40, 'CD': 400}
    # d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # sum_list = []
    # for x in l.keys():
    #     if x in n:
    #         n = n.replace(x, '')
    #         sum_list.append(l[x])
    # if n:
    #     for x in d.keys():
    #         if x in n:
    #             n = n.replace(x, '')
    #             sum_list.append(d[x])
    # return sum(sum_list)



if __name__ == '__main__':
    print roman_to_int('MCMXC')
    print roman_to_int('XXI')
    print roman_to_int('I')
    print roman_to_int('IV') #4, 'IV should == 4')
    print roman_to_int('MMVIII') #2008, 'MMVIII should == 2008')
    print roman_to_int('MDCLXVI')# 1666, 'MDCLXVI should == 1666')