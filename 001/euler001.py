def f(n): return n%3==0 or n%5==0

print sum(filter(f,range(1000)))