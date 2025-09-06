
# Filtering me condition specify karna compulsory hai.

# Ye original array ka copy return karta hai.

# 2D array me bhi same rules apply hote hain.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Condition: values greater than 25
filtered = arr[arr > 25]
print(filtered)  # [30 40 50]

# Condition: values less than or equal to 30
filtered = arr[arr <= 30]
print(filtered)  # [10 20 30]




import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr[arr>40])# 40 upar element ko lata hai

print(arr[arr<40])#40 niche element ko lata hai