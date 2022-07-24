#A simple program that uses a for loop to "count mississippily" to five. Having counted to five, the program prints to the screen the final message "Ready or not, here I come!"

import time

for counter in range(1 , 6):
    print(counter , "Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")
