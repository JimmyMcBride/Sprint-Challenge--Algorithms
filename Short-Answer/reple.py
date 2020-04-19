def first(n):
    a = 0
    while a < n * n * n:
        a = a + n * n
        print(a)
    # return a


def second(n):
    sum = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            sum += 1
            print(sum)


def bunnyEars(bunnies):
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies - 1)


n = 48

# first(n)
# print(n ** 3)
# second(n)
print(bunnyEars(n))
