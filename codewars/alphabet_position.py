def alphabet_position(s):
    a = ''.join(map(chr, range(97, 123)))
    return ' '.join(map(str, [a.index(x)+1 for x in s.lower() if x in a]))

    # a = ''.join(map(chr, range(97, 123)))
    # for x in s.lower():
    #   if x in a:
    #       # print a.index(x)+1
    #       ' '.join(a.index(x)+1)


if __name__ == '__main__':
    print alphabet_position("The sunset sets at twelve o' clock.")