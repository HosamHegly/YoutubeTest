def have_common_word(str1, str2):
    # Split each string into a set of words
    set1 = set(str1.split())
    set2 = set(str2.split())

    # Find the intersection of the two sets
    common_words = set1.intersection(set2)

    # Check if there are any common words
    return len(common_words) > 0

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

