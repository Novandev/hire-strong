def is_vowel(letter):
    """
    PARAM: Char -letter, a char that will be chcked 
    RETURN: Bool - a boolean that dictates if the letter itself is one of the vowels
    """
    return letter in ['a', 'e', 'i', 'o', 'u','y']

def score_words(words):
    """
    PARAM:  List - words, a list of words to be checked
    RETURN:  Int - word_score, a score of occurences
    This returns a score of w=letters based on an even or an odd number of vowels
    """
    word_score = 0 # Keeping track of score
    for word in words: # iterate over the words in the list 
        #must be in this loop
        vowel_count = 0 #we will be using this for the modules to count evens or odds
        for letter in word: #iterate over ever letter in the word
            if is_vowel(letter): # if this letter is a vowel
                vowel_count +=1 #increase the voweel count
        if vowel_count % 2 ==0: # if the vowl count is an even number increase the amount by 2
            word_score = word_score +2
        else: #increase the score by 1
            word_score = word_score + 1

    return word_score # return the score that weve been tallying up based on even and odd vowels