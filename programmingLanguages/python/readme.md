Learning Python
===============
Memorandum for me.


History
-------
- Day1: Basic Grammar
- Day2: Class
- Day3: Basics on List and Tuple and String
- Day4: Basics on List


To do
-----
* Numpy
* Scipy
* NLTK
* etc.

メモ (import関連)
-----------------
- 数字から始まるファイル名は import できない。
- ファイルを編集したあと再読み込みするときには reload(pkg) などとする。（import pkgname as pkg とした場合）

メモ
-----

perl の chomp 相当の処理には

    for i in lst:
      i = i.rstrip()

ファイル名の注意
----------------

Numpyの練習用に`numpy.py`というファイルを作って

    import numpy as np
    np.ndarray(...)
    
などと書き始めると、1行目のimportで自分自身を読もうとしてしまって本来のnumpyがimportできない。同じディレクトリに`numpy.pyc`などが残っていても同じ問題が起きる。

## Python2用のスクリプトをPython3で使いたい

- 「dict には has_key はない」などと言われて動かないとき
- `2to3`を試してみる


## favorites

+ [optparse](http://docs.python.jp/2.6/library/optparse.html)
+ [HTMLParse](http://docs.python.jp/2/library/htmlparser.html)
