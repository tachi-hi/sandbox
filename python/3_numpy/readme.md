Numpy メモ
-----------


#### 長い array を省略させない
    a = arange(10000)
    a
    numpy.set_printoptions(threshold='nan')
    a
