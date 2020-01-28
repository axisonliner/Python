def solution(n):
    d = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    r = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for x in range(len(d)):
        count = n // d[x]
        result.append(r[x] * count)
        n -= d[x] * count
    return ''.join(result)
    # return ''.join((n // d[x]) * r[x] for x in range(len(d)))



# def solution(number): 
#     num = [1, 4, 5, 9, 10, 40, 50, 90,  
#            100, 400, 500, 900, 1000] 
#     sym = ["I", "IV", "V", "IX", "X", "XL",  
#            "L", "XC", "C", "CD", "D", "CM", "M"] 
#     r = ''
#     i = 12
#     while number: 
#         div = number // num[i] 
#         number %= num[i]   
#         while div:
#             r += sym[i]
#             div -= 1
#         i -= 1
#     return r
     # ''.join([x for x in n if r[x] in r])

if __name__ == "__main__":
    print solution(1)#,'I', "solution(1),'I'")
    print solution(4)#,'IV', "solution(4),'IV'")
    print solution(6)#,'VI', "solution(6),'VI'")
    print solution(14)#,'XIV', "solution(14),'XIV")
    print solution(21)#,'XXI', "solution(21),'XXI'")
    print solution(89)#,'LXXXIX', "solution(89),'LXXXIX'")
    print solution(91)#,'XCI', "solution(91),'XCI'")
    print solution(984)#,'CMLXXXIV', "solution(984),'CMLXXXIV'")
    print solution(1000)#, 'M', 'solution(1000), M')
    print solution(1889)#,'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
    print solution(1989)#,'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")