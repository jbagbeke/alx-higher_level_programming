#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence.strip() == "":
        return len(sentence), None
    else:
        return len(sentence), sentence[0]
