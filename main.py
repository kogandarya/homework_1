my_name = 'Darya'
my_age = 18
print('My name is ', my_name, ", i'm ", my_age)

x = my_name * 4 + my_name
print(x)

user_name = input("Enter your name: ")
if " " in user_name:
    print("Only name is required!")
    exit()
user_age = input("Enter your age: ")
print( user_name, 'hello!', user_age, 'is a great age!')
try:
    user_age = int(user_age)
except ValueError:
    print("Age entered incorrectly: it should be number")
    exit()
if (user_age <= 0) or (user_age > 150):
    print("Age entered incorrectly: it should be strictly between 0 and 150")
    exit()
if user_age <= 22:
    print("How are things at the university?")
elif user_age <= 65:
    print("How are things at work?")
else:
    print("How are things in retirement?")

print(user_name[1:-1])
print(user_name[::-1])
print(user_name[-3])
print(user_name[:5])

x = map(int, list(str(user_age)))
mult = 1
for i in x:
    mult = mult * i
x = map(int, list(str(user_age)))
print(len(user_name), sum(x), mult)

print(user_name.lower())
print(user_name.upper())
print(user_name.capitalize())
print(user_name.capitalize().swapcase())

result = int(input("What is 3+3*3? "))
if result == 12:
    print("It is correct")
else:
    print("It's incorrect")

