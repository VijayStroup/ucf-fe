import os
import re
from PyPDF2 import PdfFileReader

path = os.path.abspath(os.path.dirname(__name__)) + '/static/'
raw_dir = path + 'raw_tests/'
question_dir = path + 'question/'
answer_dir = path + 'answer/'
info_dir = path + 'info/'

input1 = PdfFileReader(open(raw_dir + 'FE-Aug20.pdf', 'rb'))
input2 = PdfFileReader(open(raw_dir + 'FE-Aug15.pdf', 'rb'))
input3 = PdfFileReader(open(raw_dir + 'FE-May18.pdf', 'rb'))
text = input3.getPage(1).extractText().splitlines()
print(text)
rec = re.compile('([1-9])\)')
for i in text:
    res = re.search(rec, i)
    if res is not None:
        print(res.group(0))