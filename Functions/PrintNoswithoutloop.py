def printnos_without_loop(n):
    if n > 0:
        printnos_without_loop(n - 1)
        print(n)


printnos_without_loop(5)