#Using advanced templates
#The default behaviour of string template can be changed by writing custom regEx pattern and choosing new delimiters.

import string

template_text = """
    Delimiter : %%
    Replaced  : %with_underscore
    Ignored   : %notunderscored     
"""

d = {
        'with_underscore' : 'replaced',
        'notunderscored'   :  'not replaced'   #this will not be mateched by pattern
    }

class MyTemplate(string.Template): # We enhance/modify string template here
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

t = MyTemplate(template_text)
print t.safe_substitute(d)

# For a more complex tinkering , we can override the pattern attribute , and define
# an entirely new regexp

print 'The current pattern is'
print t.pattern.pattern # t.pattern is a compiled regular Expression



