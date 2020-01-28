from itertools import groupby

def unique(s):
    # print len(s)
    # print s
    # print s[1:] + s[-1:]
    # if s == [] or s == '':
    #     return ['A']
    # return [x for x, y in zip(s, s[1:] + s[:1]) if x != y or len(s) == 1]
    # return cmp(s, s[1:] + s[:1])
# -------------------------
    # uniq = None
    # list_symb = []
    # for x in s:
    #     if x != uniq:
    #         list_symb.append(x)
    #         uniq = x
    # return list_symb
    return [x for x, y in groupby(s)]




if __name__ == '__main__':
    print unique('AAAABBBCCDAABBB')
    print unique('ABBCcAD')
    print unique([1,2,2,3,3])
    print unique([1])
    print unique('D')
    print unique([])
    print unique('')
