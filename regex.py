#MATCH SEARCH FINDALL USING WITHOUT (.)

"""
import re

text = 'Hii how are you doing you'
pattern1 = r'Hii'
pattern2 = r'how are'
pattern3 = r'you'
print(f"original text is: {text}")
print()
print(f"Matching for the word is: {re.match(pattern1, text).group()}")
print(f"Searching for the word is: {re.search(pattern2, text).group()}")
print(f"Findall for the word is: {re.findall(pattern3, text)}")
"""
"""
o/p

Matching for the word is: Hii
Searching for the word is: how are
Findall for the word is: ['you', 'you']

"""
#MATCH SEARCH FINDALL USING WITH (.) AT END
"""
import re

text = 'Hii how are you doing you'
pattern1 = r'Hii.'
pattern2 = r'how are.'
pattern3 = r'you.'
print(f"original text is: {text}")
print()
print(f"Matching for the word with using (.) at end is: {re.match(pattern1, text).group()}")
print(f"Searching for the word with using (.) at end is: {re.search(pattern2, text).group()}")
print(f"Findall for the word with using (.) at end is: {re.findall(pattern3, text)}")
"""
"""
o/p

Matching for the word with using (.) at end is: Hii 
Searching for the word with using (.) at end is: how are 
Findall for the word with using (.) at end is: ['you ']


"""

#MATCH SEARCH FINDALL USING WITH (.) AT MIDDLE
"""
import re

text = 'you Hii how are you doing you you'
pattern1 = r'y.u'
pattern2 = r'how.are'
pattern3 = r'you.you'
print(f"original text is: {text}")
print()
print(f"Matching for the word with using (.) at middle is: {re.match(pattern1, text).group()}")
print(f"Searching for the word with using (.) at middle is: {re.search(pattern2, text).group()}")
print(f"Findall for the word with using (.) at middle is: {re.findall(pattern3, text)}")
"""
"""
o/p

original text is: you Hii how are you doing you you

Matching for the word with using (.) at middle is: you
Searching for the word with using (.) at middle is: how are
Findall for the word with using (.) at middle is: ['you you']


#MATCH SEARCH FINDALL USING WITH (.) AT STARTING
"""
"""
import re

text = 'You Hii how are you doing you you'
pattern1 = r'.o'
pattern2 = r'.H'
pattern3 = r'.you'#without space after you
print(f"original text is: {text}")
print()
print(f"Matching for the word with using (.) at starting is: {re.match(pattern1, text).group()}")
print(f"Searching for the word with using (.) at starting is: {re.search(pattern2, text).group()}")
print(f"Findall for the word with using (.) at starting is: {re.findall(pattern3, text)}")
"""
"""
o/p

original text is: You Hii how are you doing you you

Matching for the word with using (.) at starting is: Yo
Searching for the word with using (.) at starting is:  H
Findall for the word with using (.) at starting is: [' you', ' you', ' you']
"""
"""
text = 'You Hii how are you doing you you'
pattern1 = r'.o'
pattern2 = r'.H'
pattern3 = r'.you '#with space after you
print(f"original text is: {text}")
print()
print(f"Matching for the word with using (.) at starting is: {re.match(pattern1, text).group()}")
print(f"Searching for the word with using (.) at starting is: {re.search(pattern2, text).group()}")
print(f"Findall for the word with using (.) at starting is: {re.findall(pattern3, text)}")
"""
"""
o/p

original text is: You Hii how are you doing you you

Matching for the word with using (.) at starting is: Yo
Searching for the word with using (.) at starting is:  H
Findall for the word with using (.) at starting is: [' you ', ' you ']
"""
#MATCH SEARCH FINDALL USING (^) AT STARTING BECAUSE MIDDLE AND LAST WILL GET FAIL
"""
import re

text = 'You Hii how are you doing you you'
pattern1 = r'^Y..'
#pattern2 = r'^H' # This will fail because ^ indicates from starting of the string since H is not starting so it will get failed.
pattern3 = r'^Y................'#without space after Y
print(f"original text is: {text}")
print()
print(f"Matching for the word with using (^) at starting is: {re.match(pattern1, text).group()}")
#print(f"Searching for the word with using (.) at starting is: {re.search(pattern2, text).group()}")
print(f"Findall for the word with using (^) at starting is: {re.findall(pattern3, text)}")
"""
"""
o/p---
original text is: You Hii how are you doing you you

Matching for the word with using (^) at starting is: You
Findall for the word with using (^) at starting is: ['You Hii how are y']


"""

#MATCH SEARCH FINDALL USING ($) AT  LAST BECAUSE IT WILL GET FAIL WHEN WE USED IN STARTING AND MIDDLE

"""
import re

text = 'You Hii how are you doing sir'
#pattern1 = r'sir$'
pattern2 = r'r$'
pattern3 = r'sir$'  #without space after sir
print(f"original text is: {text}")
print()
#print(f"Matching for the word with using ($) at ending is: {re.match(pattern1, text).group()}")
print(f"Searching for the word with using ($) at ending is: {re.search(pattern2, text).group()}")
print(f"Findall for the word with using ($) at ending is: {re.findall(pattern3, text)}")
"""
"""
o/p---
original text is: You Hii how are you doing sir

Searching for the word with using ($) at ending is: r
Findall for the word with using ($) at ending is: ['sir']


"""
#MATCH SEARCH FINDALL USING (*) AT  LAST
"""
import re

text = 'You si12514541r Hii  siiiijfvdsfsbr how are you doing skiiiiir'
#pattern1 = r's.r*'
pattern2 = r's...r*'
pattern3 = r's.r*'
print(f"original text is: {text}")
print()
#print(f"Matching for the word with using (*) at ending is: {re.match(pattern1, text).group()}")
print(f"Searching for the word with using (*) at ending is: {re.search(pattern2, text).group()}")
print(f"Findall for the word with using (*) at ending is: {re.findall(pattern3, text)}")
"""
"""
o/p---

original text is: You si12514541r Hii  siiiijfvdsfsbr how are you doing siiiiir

Searching for the word with using (*) at ending is: si12
Findall for the word with using (*) at ending is: ['si', 'si', 'sf', 'sbr', 'sk']

"""
"""
import re

text = 'You soi12514541r Hii  s.iiiijfvdsfsbr how are you doing skiiiiir'
#pattern1 = r's.r*'
pattern2 = r's...r*'
pattern3 = r's.r*'
print(f"original text is: {text}")
print()
#print(f"Matching for the word with using (*) at ending is: {re.match(pattern1, text).group()}")
print(f"Searching for the word with using (*) at ending is: {re.search(pattern2, text).group()}")
print(f"Findall for the word with using (*) at ending is: {re.findall(pattern3, text)}")

"""
"""
o/p---

original text is: You si12514541r Hii  siiiijfvdsfsbr how are you doing siiiiir

Searching for the word with using (*) at ending is: soi1
Findall for the word with using (*) at ending is: ['so', 's.', 'sf', 'sbr', 'sk']

"""
"""
import re

text = 'You soi12514541r Hii  s.iiiijfvdsfsbr how are you doing skiiiiir'
#pattern1 = r's.r*'
pattern2 = r's...*'
pattern3 = r's*'
print(f"original text is: {text}")
print()
#print(f"Matching for the word with using (*) at ending is: {re.match(pattern1, text).group()}")
print(f"Searching for the word with using (*) at ending is: {re.search(pattern2, text).group()}")
print(f"Findall for the word with using (*) at ending is: {re.findall(pattern3, text)}")
"""
"""
o/p---

original text is: You soi12514541r Hii  s.iiiijfvdsfsbr how are you doing skiiiiir

Searching for the word with using (*) at ending is: soi12514541r Hii  s.iiiijfvdsfsbr how are you doing skiiiiir
Findall for the word with using (*) at ending is: ['', '', '', '', 's', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 's', '', '', '', '', '', '', '', '', '', 's', '', 's', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 's', '', '', '', '', '', '', '', '']
"""

import re

text = 'You soi12514541r Hii  s.iiiijfvdsfsbr how are you doing skiiiiir'
pattern1 = r's.r+'
pattern2 = r's...+'
pattern3 = r'.s+'
pattern4 = r'...s...+'
print(f"original text is: {text}")
print()
print(f"Searching for the word with using (+) at ending is: {re.search(pattern1, text).group()}")
print(f"Searching for the word with using (+) at ending is: {re.search(pattern2, text).group()}")
print(f"Searching for the word with using (+) at ending is: {re.search(pattern4, text).group()}")
print(f"Findall for the word with using (+) at ending is: {re.findall(pattern3, text)}")

"""
o/p---

original text is: You soi12514541r Hii  s.iiiijfvdsfsbr how are you doing skiiiiir

Searching for the word with using (+) at ending is: sbr
Searching for the word with using (+) at ending is: soi12514541r Hii  s.iiiijfvdsfsbr how are you doing skiiiiir
Searching for the word with using (+) at ending is: ou soi12514541r Hii  s.iiiijfvdsfsbr how are you doing skiiiiir
Findall for the word with using (+) at ending is: [' s', ' s', 'ds', 'fs', ' s']

"""

import re
text = "Please visit www.google.com www3yahoo*com www.yahoo.com mail.google.com www."
"""
www.google.com
\w+ - www
\. - .
\w+ -google
\. - .
\w+ - com
"""
pattern = r"\w+\.\w+\.\w+"
matched = re.findall(pattern, text)
print(fr"Matched text is {matched}")
import re
text = "India is a beautiful country to live So VISIT"
abc_pattern = r"[abc]" # Matches with only one char a or b or c
az_pattern = r"[a-z]" # Matches all chars b/w a-z but only one char
AZ_pattern = r"[A-Z]" # Matches all chars b/w A-Z but only one char
abc_matched_text = re.findall(abc_pattern, text)
print(f"Matched Text is {abc_matched_text}")
az_matched_text = re.findall(az_pattern, text)
print(f"Matched a-z text is {az_matched_text}")
AZ_matched_text = re.findall(AZ_pattern, text)
print(f"Matched A-Z text is {AZ_matched_text}")
"""
OUTPUT:
Matched Text is ['a', 'a', 'b', 'a', 'c']
Matched a-z text is ['n', 'd', 'i', 'a', 'i', 's', 'a', 'b', 'e', 'a', 'u', 't', 'i',
Matched A-Z text is ['I', 'S', 'V', 'I', 'S', 'I', 'T']
"""

import re
text = "India 200 is a beautiful5000000000000 country to live 768648682 So VISIT"
pattern = r"\d+" # [0-9]
matched_text = re.findall(pattern, text)
print(f"Matched pattern is {matched_text}")

import re


def extract_emails(text):
    # Define the regex pattern for extracting emails
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to extract all email addresses matching the pattern
    emails = re.findall(pattern, text)

    return emails


# Example usage:
text = """
Here is a list of emails: john@example.com, alice123@gmail.com, 
test.user@yahoo.co.uk, support@company.com, random.email@example
"""

emails_list = extract_emails(text)
print(emails_list)
