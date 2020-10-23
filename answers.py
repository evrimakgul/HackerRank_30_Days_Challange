# Day 1

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
i2 = int(input())
d2 = float(input())
s2 = str(input())
# Print the sum of both integer variables on a new line.
print(i + i2)
# Print the sum of the double variables on a new line.
print(d + d2)
# Concatenate and print the String variables on a new line
print(s + s2)
# The 's' variable above should be printed first.

# ==========

# Day 2

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total_cost = (meal_cost) + (meal_cost * tip_percent / 100) + (meal_cost * tax_percent / 100)
    print(round(total_cost))
    
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

# ==========
    
# Day 3

if __name__ == '__main__':
    N = int(input())

    if N % 2 == 1:
        print('Weird')
    elif N % 2 == 0 and N in [2,3,4,5]:
        print('Not Weird')
    elif N % 2 == 0 and N in [_ for _ in range(6,21)]:
        print('Weird')
    elif N % 2 == 0 and N > 20:
        print('Not Weird')
