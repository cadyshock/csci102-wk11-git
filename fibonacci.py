# fibonacci.py

def fib():
    fibs=[1,2]
    for i in range(1,9):
        doop=fibs[i-1]+fibs[i]
        fibs.append(doop)
        
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
