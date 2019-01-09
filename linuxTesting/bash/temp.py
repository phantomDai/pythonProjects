import math


class temp(object):

    def cal(m, x, y, h):
        step1 = 1 / (2 * x)
        step2 = 1 / (2 * y)
        step3 = (step2 - step1) * h
        step4 = step1 + step3
        step5 = step4 * m - 1
        result = m / step5
        print(result)

    def callog(c,x):
        a = math.log(c,x)
        print(a)


t = temp
t.callog(304 ,100)
