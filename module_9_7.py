def is_prime(func):
    def wrapper(x,y,z):
        orig = int(func(x,y,z))
        prime_f = True
        for d in range(2,orig//2+1):
            if orig % d == 0:
                prime_f = False
        if prime_f:
            modif = f'Простое\n{orig}'
        else:
            modif = f'Составное\n{orig}'
        return modif
    return wrapper

@is_prime
def sum_three(a,b,c):
    return str(a+b+c)

result = sum_three(2, 3, 7)
print(result)
