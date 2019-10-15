# Gavin Howard
# 10/14/19
# Wick Bakery

from statistics import mean

cookies = []
candies = []

for cookie_values in range(0, 6):
    print("Please enter each amount of cookies one by one.")
    cookie_input = int(input())
    cookies.append(cookie_input)
    print(cookies)


def cookies_avg():
    return mean(cookies)


def cookies_max():
    cookies.sort()


def cookies_min():
    cookies.sort()


print(f"The average amount of cookies sold is: {cookies_avg()}")
print("The maximum number of cookies sold is: ", cookies[-1])
print("The minimum number of cookies sold is: ", *cookies[:1])

for candy_values in range(0, 6):
    print("Please enter each amount of candies one by one.")
    candy_input = int(input())
    candies.append(candy_input)
    print(candies)


def candies_avg():
    return mean(candies)


def candies_max():
    candies.sort()


def candies_min():
    candies.sort()


print(f"The average amount of candies sold is: {candies_avg()}")
print("The maximum number of candies sold is: ", candies[-1])
print("The minimum number of candies sold is: ", *candies[:1])

if cookies_avg() > candies_avg():
    print("Cookies are more popular at the Hartwick Bakery")
else:
    print("Candies are more popular at the Hartwick Bakery")
