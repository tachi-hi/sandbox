import numpy as np

L = 10
# 重複あり
a = np.random.choice(np.arange(L), 8, replace=True)
print(a)

a = np.random.choice(np.arange(L), 10, replace=True)
print(a)

a = np.random.choice(np.arange(L), 20, replace=True)
print(a)

# 重複なし
a = np.random.choice(np.arange(L), 8, replace=False)
print(a)

a = np.random.choice(np.arange(L), 10, replace=False)
print(a)

a = np.random.choice(np.arange(L), 20, replace=False) # error
print(a)
