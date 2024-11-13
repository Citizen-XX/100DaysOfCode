# def add(*args):
#     print(sum(args[0]))

# one_to_hundred = [*range(1,101)]
# add(one_to_hundred)

def add(*args):
    print(f'The args type is: {type(args)}')
    print(f'The positional arg at index 2: {args[2]}')
    total = 0
    for i in args:
        total += i
    print(f'The sum of the args is: {total}')

# add(10,11,12,13,14,15)

def calculate(n,**kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2,add=3,multiply=5)
