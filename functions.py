def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    lst2 = []
    for element in lst:
        if element not in lst2:
            lst2.append(element)

    return lst2

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    count_uppercase = 0
    count_lowercase = 0
    for letra in string:
        if letra.islower():
            count_lowercase +=1
        elif letra.isupper():
            count_uppercase +=1
    
    return count_uppercase,count_lowercase

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    sentence2 = ""
    for character in sentence:
        if character.isalpha() or character==' ':
            sentence2 = sentence2 +character
    return sentence2


def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    sentence = remove_punctuation_f(sentence)
    words = sentence.split()
    return len(words)

def addition_f(*args):
    result = 0
    for num in args:
        result += num
    return result

def subtraction_f(*args):
    result = args[0]
    rest = args[1:]
    for num in rest:
        result -=num
    return result

def multiplication_f(*args):
    result = 1
    for num in args:
        result *= num
    return result

def division_f(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

def calculator_f(operator,*args):
    if operator=='+':
        return addition_f(*args)
    elif operator=='-':
        return subtraction_f(*args)
    elif operator=='*':
        return multiplication_f(*args)
    elif operator=='/':
        return division_f(*args)
    else:
        return 0
