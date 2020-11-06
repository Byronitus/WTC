import string

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """Converts a string into a list with only characters"""
    return (' '.join(split('.,;? ',text.lower()))).split()


def words_longer_than(length, text):
    """retuns words that are of length greater than the int parameter"""
    return list(filter(lambda x: (len(x) > length),convert_to_word_list(text)))


def words_lengths_map(text):
    """Maps the amount of each length of the words into a dictionary"""
    dictionary = {}
    listtext = convert_to_word_list(text)
    for x in listtext:
        count = 0
        count = [count + 1 for y in listtext if len(x) == len(y)]
        if not len(x) in dictionary:
            dictionary[len(x)] = len(count)
    return dict(sorted(dictionary.items()))


def letters_count_map(text):
    """maps the amount of each character into a dictionary"""
    word = ''.join(convert_to_word_list(text))
    dictionary = {}
    for x in string.ascii_lowercase:
        count = 0
        count = [count + 1 for y in word if x == y]
        if not x in dictionary:
            dictionary[x] = len(count)
    return dict(sorted(dictionary.items()))


def most_used_character(text):
    """returns the most used character in a string"""
    if ''.join(convert_to_word_list(text)).isalpha():
        return max(letters_count_map(text),key=letters_count_map(text).get)
    return None