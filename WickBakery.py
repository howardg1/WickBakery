# Gavin Howard
# 10/14/19
# Wick Bakery

from statistics import mean

cookies = []
candies = []


def enter_cookie():
    for cookie_values in range(0, 6):
        print("Please enter each amount of cookies one by one.")
        cookie_input = int(input())
        cookies.append(cookie_input)
        print(cookies)


def cookies_avg():
    return mean(cookies)

# Do not call any functions until after they are all written.  Move this to the end



def cookies_max():
    cookies.sort()
    print("The maximum number of cookies sold is: ", cookies[-1])


def cookies_min():
    cookies.sort()
    print("The minimum number of cookies sold is: ", *cookies[:1])


def enter_candy():
    for candy_values in range(0, 6):
        print("Please enter each amount of candies one by one.")
        candy_input = int(input())
        candies.append(candy_input)
        print(candies)


def candies_avg():
    return mean(candies)

# Do not call any functions until after they are all written.



def candies_max():
    candies.sort()
    print("The maximum number of candies sold is: ", candies[-1])

def candies_min():
    candies.sort()
    print("The minimum number of candies sold is: ", *candies[:1])

# Here is where your calls to the functions should be:
enter_cookie()
enter_candy()
candies_max()
candies_min()
cookies_max()
cookies_min()
print(f"The average amount of cookies sold is: {cookies_avg()}")
print(f"The average amount of candies sold is: {candies_avg()}")
cookie_average = cookies_avg()
candy_average = candies_avg()

if cookie_average > candy_average:
    print("Cookies are more popular at the Hartwick Bakery")
else:
    print("Candies are more popular at the Hartwick Bakery")
