#Understanding String Templates[${}] with safe substitution
# Safe substitution prevents exceptions and handles them automatically

import string

values = { 'var' : 'foo'}

t = string.Template("$var is here but $missing is missing!")

try:
    print 'substitute() :' , t.substitute(values)
except KeyError, err:
    print 'ERROR: ', str(err)

print 'safe_substitute() :',t.safe_substitute(values)

