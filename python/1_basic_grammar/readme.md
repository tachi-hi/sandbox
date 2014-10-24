文法メモ
========

### リスト 
#### append と extend
    lst=["a","b","c"]
    lst.append(["d","e"])
    # lst = ["a", "b", "c", ["d", "e"]]
    lst.extend(["f","g"])
    # lst = ["a", "b", "c", ["d", "e"], "f", "g"]
    
### import
#### サブディレクトリ
サブディレクトリにあるファイルをインポートするにはサブディレクトリに`__init__.py`（中身は空でよい）を作成した上で

    import subdir.myPackage

#### 任意ディレクトリ
sys.path.appendで任意のディレクトリからimportできる。

    sys.path.append("/home/hoge/src")
    import myPackage

`os.pardir`, `os.path.abspath(__file__)` などを使ってpwdや親ディレクトリを取得して`sys.path.append`の引数を適当に書き換える。
