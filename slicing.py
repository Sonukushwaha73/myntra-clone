
# Slicing (cut)/ Subset nikalna)

# Slicing ka matlab hai list/string ke ek range of elements nikalna.

# Syntax:

# sequence[start : end : step]


# start → slice start ka index (inclusive)

# end → slice end ka index (exclusive)

# step → kitne-kitne index skip kar ke nikalna (optional)

#: ka matlab hai poora range select karo.


import numpy as np
arr = np.array([10, 20, 30, 40, 50])

print(arr[0:3])
print(arr[::2]) #step start hota hai
print(arr[:])
print(arr[:2:2])
print(arr[-4: :])


