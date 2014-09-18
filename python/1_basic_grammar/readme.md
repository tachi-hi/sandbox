文法メモ
========

### リスト 
#### append と extend
    lst=["a","b","c"]
    lst.append(["d","e"])
    # lst = ["a", "b", "c", ["d", "e"]]
    lst.extend(["f","g"])
    # lst = ["a", "b", "c", ["d", "e"], "f", "g"]
    
