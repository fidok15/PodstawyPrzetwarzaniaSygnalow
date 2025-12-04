import math

def delta(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print("brak pierwiastkow")
    elif d == 0:
        x = -b / (2*a)
        print(f"pierwastek: x = {x}")
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"pierwiastki: x1 = {x1}, x2 = {x2}")

def palindrome(str):
    i,j = 0, len(str) - 1  
    is_palindrome = True 
    while i < j:
        if str[i] != str[j]:
            is_palindrome = False
            break
        i += 1
        j -= 1
    if is_palindrome:
        print("tak") 
    else:
        print("nie")

def main():
    a = float(input("podaj a: "))
    b = float(input("podaj b: "))
    c = float(input("podaj c: "))
    ans = delta(a, b, c)

    input_str = input("Slowo: ")
    palindrome(input_str)


if __name__ == "__main__":
    main()
