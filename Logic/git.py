def switch_index(num, index, k):
    i=0
    y = 1
    before_index = 0
    while i < index:

        before_index +=int((num%10 * y))
        num = int(num/10)
        i+= 1
        y=y*10


    num = num - num%10

    num = num + k
    num = num * y
    num = num + before_index
    return num




print(switch_index(234544,2,7))

