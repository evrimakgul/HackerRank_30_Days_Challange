# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = dict()
for i in range(n):
    data = input()
    name = data[:-9]
    number = data[-8:]
    phone_book[name] = number


while True:
    try:
        query = input()
        if query in phone_book:
            print(query + "=" + phone_book[query])
        else:
            print('Not found')
    except:
        break
