def fibonacci(stop: int) -> bool:
    last = 0
    current = 0
    next = 1
    
    while True:
        if (current == stop): 
            return True
        if (current > stop):
            return False

        last = current
        current = next
        next = current + last

stop = int(input())
print(fibonacci(stop))