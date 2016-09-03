Numpy メモ
-----------


#### 長い array を省略させない

    a = arange(10000)
    a
    numpy.set_printoptions(threshold='nan')
    a

#### ndarray のサイズを取得

2次元配列なら

    n, m = a.shape
で取得できる

