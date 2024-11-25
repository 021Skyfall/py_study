from math import floor

t = int(input())

for i in range(t):
    n = int(input())

    quarter = n / 25
    n %= 25

    dime = n / 10
    n %= 10

    nickel = n / 5
    n %= 5

    penny = n

    print(floor(quarter), floor(dime), floor(nickel), floor(penny))