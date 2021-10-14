def comb(N, M, arr_gl):
    if M == 0:
        print(*arr_gl)
        return

    for i in range(1, N+1):

        if len(arr_gl) == 0:
            arr_gl.append(i)
            comb(N, M-1, arr_gl)
            arr_gl.pop()
        elif arr_gl[-1] <= i:
            arr_gl.append(i)
            comb(N, M-1, arr_gl)
            arr_gl.pop()
        else:
            pass

if __name__ == "__main__":

    N, M = map(int, input().split())
    comb(N, M, [])