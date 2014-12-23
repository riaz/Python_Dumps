# maketrans - used to create a translation table , to encode characters

import string

leet = string.maketrans('abegiloprstz','434123678934')
s = 'The quick brown fox jumps over the lazy dog'

print s
print s.translate(leet)
