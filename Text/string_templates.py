#Understanding String Templates[${}] and Interpolation[%()] 
import string

values = { 'var' : 'foo'}

t = string.Template("""
        Variable : $var
        Escape   : $$
        Variable in text : ${var}bar
""")

print 'TEMPLATE: ',t.substitute(values)

s = """
    Variable : %(var)s
    Escape : %%
    Variable in text: %(var)siable
        """
print 'INTERPOLATION:', s % values


