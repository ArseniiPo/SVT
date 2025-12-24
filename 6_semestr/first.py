from math import sin

class RightSide:
    def __init__(self, n, a, b, f):
        self.n = n
        self.h = 1/(n * 1.0)
        self.a = a
        self.b = b
        self.f = f

    def __call__(self, k):
        add = 0
        if k == 0:
            add = self.a
        elif k == self.n - 1:
            add = self.b
        return self.f(k*self.h) * self.h * self.h + add



def TDMA(f):

    alpha = [0.5]
    beta = [f(0) * 0.5]
    n = f.n
    x = [0] * n 

    for i in range(1, n):
        alpha.append(1/(2 - alpha[i-1]))
        beta.append((f(i) + beta[i-1])/(2 - alpha[i-1]))

    x[n - 1] = beta[n - 1]

    for i in range(n - 1, 0, -1):
        x[i - 1] = alpha[i - 1] * x[i] + beta[i - 1]

    x.insert(0, f.a)
    x[n] = f.b
    return x

def func(x):
    return x + sin(x)

def main():
    n = 10
    cnt = 1
    while cnt < 8:
        ans = TDMA(RightSide(n, 0, 1 + sin(1), sin))
        step = 1 / (1.0 * n)
        max_norm = 0
        l2_norm = 0
        for i in range(n + 1):
            # print(ans[i], " : ", func(step * i))
            cur = abs(ans[i] - func(step * i))
            l2_norm += cur**2
            if cur > max_norm:
                max_norm = cur
        print("10^", cnt, " MAXNorm : ", max_norm, sep="")
        print("10^", cnt, " L2 NORM : ", l2_norm, sep="")
        n *= 10
        cnt += 1
    return 0

if __name__ == "__main__":
    main()
