# -*- coding: utf-8 -*-
# (C) 2013-2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
from ngram.Corpus import Corpus
from ngram import LetterModels, WordModels

import tamil.utf8 as utf8

class WordsNGram(unittest.TestCase):
    def test_basic(self):
        word = u"அருஞ்சொற்பொருள்"
        self.assertEqual( WordModels.get_ngram_groups( word, 1), tamil.utf8.get_letters(word) )
        self.assertEqual( WordModels.get_ngram_groups( word, 2), [u"அரு",u"ருஞ்", u"ஞ்சொ", u"சொற்", u"ற்பொ", u"பொரு",u"ருள்"] )
        self.assertEqual( WordModels.get_ngram_groups( word, 3), [u"அருஞ்",u"ருஞ்சொ",u"ஞ்சொற்", u"சொற்பொ",u"ற்பொரு",u"பொருள்"] )
        self.assertEqual( WordModels.get_ngram_groups( word, 8), [ word ])
        self.assertEqual( WordModels.get_ngram_groups( word, 9), [ word ])

class Letters(unittest.TestCase):
    def test_basic_unigram_counts(self):
        z = Corpus("data/ex.unicode")
        for letter in z.next_tamil_letter():
            if ( LINUX ): print(letter)
        
        q = LetterModels.Unigram( "data/ex.unicode" )
        q.frequency_model( )
        if not PYTHON3:
            if ( LINUX ): print(unicode(q))
        else:
            if ( LINUX ): print( q )
        assert( q.letter[u"ஷை"] + q.letter[u"சி"] == q.letter[u"ந"] )
        del z, q

    def test_bigram_counts(self):
        q=LetterModels.Bigram("data/ex.unicode")
        q.language_model(verbose=LINUX) #suppress output
        assert( q.letter2[u"த்"][u"து"] == 7 )
        assert( q.letter2[u"சி"][u"சி"] == 0 )        
    
if __name__ == '__main__':    
    unittest.main()
