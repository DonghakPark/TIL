if __name__=="__main__":
    N = 400
    e = 0.01
    ans = []
    x = -400
    while (x <= 4):
        if abs(x - x ** 2) < e:
            print(x/100)
        x += 1