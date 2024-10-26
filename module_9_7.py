def is_prime(func):
    def wrapper(*args):
        j = func(*args)
        for i in range(2, int(j / 2) + 1):
            if j % i == 0:
                print('Составное')
                return j
            print('Простое')
            return j
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)