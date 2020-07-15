#!/usr/bin/python3
# -*- coding: utf-8 -*-

from data import words

def words_with_length(length):
    return [word for word in words if len(word) == length]

def words_containing_string(s):
    return [word for word in words if s in word]

def words_starting_with_character(c):
    return [word for word in words if word[0] == c]

def alphabet():
    return "".join([chr(i) for i in range(ord('a'),ord('z')+1)])

def dictionary():
    return {i: words_starting_with_character(i) for i in alphabet()}

def censored_words(s):
    return ["x"*len(word) if s in word else word for word in words]


print(alphabet())
