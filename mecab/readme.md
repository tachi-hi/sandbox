Learning MeCab
==============
Memo for me how to use mecab.

Links
-----
* http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html

Setup Memo
----------
MeCab is easily set up by using `apt-get`.

Basic: 
------
 > mecab textSamples/JapaneseConstitutionPreface.txt

Then the result is output to stdout. Then filtering commands such as `grep` works.

 > mecab textSamples/JapaneseConstitutionPreface.txt | grep "名詞"
 
mecab receives input from stdin.

 > echo これは例文です | mecab

N-best solutions. Following is "3-best"

 > mecab textSamples/takasebune.txt -N3

Command Line Options
--------------------

To do


