import numpy as np
from time import time

m = np.matrix([[ 23.4,  5.86,  3.65,  8.56,  5.54 ],
               [ 3.23, -3.4,   3.21,  4.23,  5.66 ],
               [ 3.42,  4.33, -4.32,  4.32, -4.32 ],
               [ 4.32,  3.43,  3.32,  4.32,  8.90 ],
               [ -6.6,  7.66, -5.67, -6.75,  6.67 ],
              ])

n = np.matrix([[ -3.4,   3.21,  5.66,  4.43,  4.32 ],
               [  4.33, -4.32, -4.32, -4.32,  4.32 ],
               [  7.66, -5.67,  6.67,  7.76,  4.32 ],
               [  5.75,  7.65,  0.75,  2.35,  4.32 ],
               [  1.11,  2.34,  5.43,  3.53,  4.32 ]
              ])

start_time = time()
result = m * n
end_time = time()
print(result)
eleapse_time = end_time - start_time
print("Elapsed time: %0.10f seconds." % eleapse_time)
print()