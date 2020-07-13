# sum nubers and return sum

def sum(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + sum(x[1:])

my_list = [2, 4, 6]

print(sum(my_list))