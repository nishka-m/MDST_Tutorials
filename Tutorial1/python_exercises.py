"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if ((x%2) == 0):
        return False
    else:
        return True

def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    length = len(word)
    palindrome = True
    for i in range(int(length/2)):
        if(word[i] != word[length - i - 1]):
            palindrome = False
    
    if(palindrome == True):
        print(word, "is a palindrome.\n")
    else:
        print(word, "is not a palindrome.\n")

def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    oddList = []
    for i in range(0, len(numlist)):
        if(is_odd(i) == True):
            oddList.append(i)
            
    print(oddList)

def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    wordList = text.lower().split()
    wordCount = {}
    for word in wordList:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    