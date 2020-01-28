def find_it(seq):
    # return num % 2 == 0
    # find numbers
    # d = {x:seq.count(x) for x in seq}
    # d = [seq.count(x) for x in seq if x % 2 == 0]
    # for x in seq:
    #   print x , seq.count(x)
    # return len([seq.count(x) for x in seq if seq.count(x) % 2 != 0])
    return [x for x in seq if seq.count(x) % 2][0]

    # print d
    # n = 0
    # for x in seq:
    #   if x % 2 == 0:
    #       print x


if __name__ == '__main__':
    print find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5,5,5])
    print find_it([1,1,2,-2,5,2,4,4,-1,-2,5])
    print find_it([1,1,1,1,1,1,10,1,1,1,1])
    print find_it([7, 7, 7])