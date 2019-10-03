n = int(input())
phone_book = {}
for i in range(n):
    phone = input().split()
    phone_book[phone[0]] = phone[1]
try:
    while True:
        name = input()
        if name in phone_book:
            print(f'{name}={phone_book[name]}')
        else:
            print('Not found')
except EOFError:
    pass
