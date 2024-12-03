n,a,b = map(int, input().split())


print(min(n - a, b + 1))



def findPosition(n, f, b):
 
    return n - max(f + 1, n - b) + 1;
