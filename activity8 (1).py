import numpy as np
array = np.random.randint(1,21,size=(3,3))
print("Original 3*3 Array:\n",array)

mean_value =np.mean(array)
print("\nMean of the array:"mean_value)

array[array<10] = 0
print("\nModified Array (Elements < 10 with 0):\n",array)
