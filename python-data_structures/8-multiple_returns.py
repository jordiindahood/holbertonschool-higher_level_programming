#!/usr/bin/python3
def multiple_returns(sentence):
    string = None
    length = 0
    if sentence:
        length = len(sentence)
        string = sentence[0]
    return (length, string)
