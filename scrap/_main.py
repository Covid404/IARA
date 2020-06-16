import requests
import lxml.html as lh
import pandas as pd



url = 'https://www.sistemas.pa.gov.br/compraspara/public/licitacao_list.xhtml'

page = requests.get(url)

doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

print(tr_elements[0])
print([len(T) for T in tr_elements[:12]])

i=0
col = []
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print(i, name)
    col.append((name, []))
