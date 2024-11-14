def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_user_info(name="John",age=30,country="USA")