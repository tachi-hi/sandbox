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

