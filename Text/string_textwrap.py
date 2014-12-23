#textwrap - fill function

import textwrap
from textwrap_example import sample_text

print 'Raw Text:\n'
print sample_text

print 'No dedent"\n' #i.e not removing existing indentations in the raw text
print textwrap.fill(sample_text,width=8)

#preparing dedented text using the textwrap module
dedent_text = textwrap.dedent(sample_text)

print textwrap.fill(dedent_text,width=8)


