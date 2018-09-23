# def a_new_decorator(a_func):
#
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
#
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")
#
#
# a_function_requiring_decoration()
# # outputs: "I am the function which needs some decoration to remove my foul smell"
#
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# # now a_function_requiring_decoration is wrapped by wrapTheFunction()
#
# a_function_requiring_decoration()
# # outputs:I am doing some boring work before executing a_func()
# #        I am the function which needs some decoration to remove my foul smell
# #        I am doing some boring work after executing a_func()
#
#
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
#
# a_function_requiring_decoration()
# # outputs: I am doing some boring work before executing a_func()
# #         I am the function which needs some decoration to remove my foul smell
# #         I am doing some boring work after executing a_func()
#
# # the @a_new_decorator is just a short way of saying:
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

#
# from functools import wraps
#
# def logit(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#     return with_logging
#
# @logit
# def addition_func(x):
#    """Do some math."""
#    return x + x
#
#
# result = addition_func(4)
# # Output: addition_func was called


# from collections import Counter
#
# #
# # with open('', 'rb') as f:
# #     line_count = Counter(f)
# # print(line_count)
#
#
# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
#
# favs = Counter(name for name, colour in colours)
# print(favs)



   
