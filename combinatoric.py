import math
import scipy.stats as st
# Ah, shit, here we go again


def combination(n, k):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n - k))

n = 1000
ans1 = 1 - (combination(n, n)  *  (2 /(2**10))**0  *  (1 - 2/(2**10))**(n))
ans2 = 1 - (combination(n, n)  *  (2 /(2**8))**0   *  (1 - 2/(2**8))**(n))
ans3 = (combination(n, 3) * (2 / 2**10)**3 * (1 - 2/2**10)**(n - 3))

print("Хотя бы у одного человека 10 раз подряд выпала одна сторона: " + str(ans1))
print("Хотя бы у одного человека 8 раз подряд выпала одна сторона: " + str(ans2))
print("Ровно у троих человек выпало 10 раз подряд одна сторона: " + str(ans3))