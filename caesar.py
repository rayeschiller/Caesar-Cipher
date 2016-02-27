#
# coding: utf-8

#
# The Caesar Cipher
#
# Name: Rina Schiller
#
#

#encipher functions
def rot1( let ):
    """ returns the letter AFTER let in the alphabet
    """
    ALL_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
   
    if let not in ALL_LETTERS:
        return let  # does not change if not a letter!

    # special case for 'Z'
    if let == 'Z':
        return 'A'
    # special case for 'z':
    if let == 'z':
        return 'a'
    # for other letters, we add one to its ascii value...
    ascii_value = ord(let)
    new_ascii_value = ascii_value + 1
    # then convert back
    new_letter = chr( new_ascii_value )
    return new_letter

def rot(c,n):
    """returns the nth letter after c in the alphabet"""
    if c == '':
        return ''
    elif n == 0:
        return c
    else:
        return rot(rot1(c),n-1)

def encipher(S,n):
    if S == '':
        return ''
    else:
        return rot(S[0],n) + encipher(S[1:],n)

#decipher functions
def letterScore(let):
    """ input: single character string
        output: Scrabble value of character 
        action: determines scrabble letter values 
    """

    if let in 'AaEeIiOoUuLlNnSsTtRr':
        return 1
    elif let in 'DdGg':
        return 2
    elif let in 'BbCcMmPp':
        return 3
    elif let in 'FfHhVvWwYy':
        return 4
    elif let in 'Kk':
        return 5
    elif let in 'JjXx':
        return 8
    elif let in 'QqZz':
        return 10
    else:
        return 0 

def scrabbleScore(s):
    """ input: string
        output: scrabble score of the string 
        action : adds up scrabble letters in string 
    """
    if s == '':
        return 0
    else:
        return letterScore(s[0]) + scrabbleScore(s[1:])
# table of probabilities for each letter...

def decipher(S):
    L = [ encipher(S,n) for n in range(26)]
    LoL = [ [scrabbleScore(x),x] for x in L ]
    n = min(LoL)
    print n[1]
