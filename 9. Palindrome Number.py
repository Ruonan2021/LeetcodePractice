
# my solution
# def isPalindrome(x: int) -> bool:
#     x = str(x)  # convert int to str, to use len()
#     for i in range(0, len(x)):
#         if x[i] != x[-(1+i)]:
#             return False
#     return True


# A more brilliant way
# xample, if x = 15951, then let's create reverse of x in loop. Initially,
# x = 15951, revX = 0
# x = 1595, revX = 1
# x = 159, revX = 15
# x = 15, revX = 159
def isPalindrome(x: int) -> bool:

    result = 0
    while x > result:
        result = result * 10 + x % 10
        x = x // 10

    return True if (x == result or x == result // 10) else False

if __name__ == '__main__':
    print(isPalindrome(121))
