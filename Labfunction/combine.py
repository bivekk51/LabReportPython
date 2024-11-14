# 1) def hello():
#     print("Hello, World!")
# hello()

# 2)def add_numbers(a,b):
#     return a+b
# result=add_numbers(7,3)
# print(result)

# 3)def greet_user(name):
#     print("Hello",name)
# name=greet_user("Alice")

# 4)def greet_user(name="Guest"):
#     print(f"Hello,{name}")
# greet_user()
# greet_user("Alice")

# 5)def calculate_sum(*args):
#     return sum(args)
# result=calculate_sum(1,2,3,4)
# print(sum)

# 6)def print_user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# print_user_info(name="John",age=30,country="USA")

# 7)def show_coordinates(x,y):
#     print(f"x:{x},y:{y}")
# coordinates=(4,5)
# show_coordinates(*coordinates)

# 8)def display_book_info(title,author,year):
#     print(f"Title:{title}")
#     print(f"Author:{author}")
#     print(f"Year:{year}")
# book_info={
#     "title":"Python Programming",
#     "author":"John Doe",
#     "year":2021
# }
# display_book_info(**book_info)

# 9)def square_number(a):
#     return a*a
# result=square_number(8)
# print(result)

# 10)def get_min_max(a):
#     return min(a),max(a)
# min_value,max_value=get_min_max([2,4,1,9,5])
# print(f"minimum:{min_value},maximum:{max_value}")

# 11)def fact(a):
#     if a==0 or a==1:
#         return 1
#     else:
#         return a*fact(a-1)
# result=fact(5)
# print(result)

# 12)def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# result= fibonacci(6)
# print(result)

# 13)multiply_by_3 = lambda x: x * 3
# result = multiply_by_3(7)
# print(result)
