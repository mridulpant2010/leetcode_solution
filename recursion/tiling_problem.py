def tiling_problem(n):
    if n<=3:
        return 1
    return tiling_problem(n-1)+tiling_problem(n-4)

if __name__ == '__main__':
    a=tiling_problem(4)
    print(a)