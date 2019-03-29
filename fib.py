def fib(n):
  if n <= 1: return n
  else: return fib(n-1)+fib(n-2)

if __name__ == '__main__':
  print(f'f({0})={fib(0)}')
  print(f'f({1})={fib(1)}')
  print('f(%d)=%d' %(2, fib(2)))
  print('f(%d)=%d' %(5, fib(5)))
  print('f({})={}'.format(12, fib(12)))
  print('f({})={}'.format(19, fib(19)))
