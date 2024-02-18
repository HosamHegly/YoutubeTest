def have_common_word(str1, str2):
    # Split each string into a set of words
    set1 = set(str1.split())
    set2 = set(str2.split())

    # Find the intersection of the two sets
    common_words = set1.intersection(set2)

    # Check if there are any common words
    return len(common_words) > 0

