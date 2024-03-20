
def fizz_buzz(n):
        for x in range(1, n+1):
         if x % 3 == 0 and x % 5 ==0:
          print("Fizz_Buzz")
         elif x % 3 == 0:
          print("Fizz")
         elif x % 5 == 0:
          print("Buzz")
         else:
            print(x)
        return(n)
n = int(input("введите число: "))
fizz_buzz(n)
