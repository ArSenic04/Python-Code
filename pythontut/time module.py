"""Time Module"""
import time
# ini = time.time()
# k = 0
# while k < 45:
#     print(k)
#     k += 1
# print(time.time() - ini)
# ini2 = time.time()
# for i in range(45):
#     print(i)
# print(time.time() - ini2)
localtime=time.asctime(time.localtime(time.time()))
print(localtime)