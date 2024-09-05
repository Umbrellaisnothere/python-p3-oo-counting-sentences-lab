#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value = ""):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value 
    
    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        sentences = re.split(r'[.!?]\s*', self._value.strip())
        return len([s for s in sentences if s])
    
    def count_words(self):
        words = self._value.split()
        return len(words)
    


value = MyString("This is a string! It has three sentences. Right?")
print(value.count_sentences())
print(value.count_words())
  # pass
