from math import cos, factorial, floor, pi

n = 3

# formula = 1 + sum(
#     floor(
#         (
#             n / sum(
#                 floor(
#                     cos(
#                         pi * (
#                             (
#                                 factorial(j-1) + 1
#                             ) / j
#                         )
#                     ) ** 2
#                 ) for j in range(1, i)
#             )
#         ) ** (1/n)
#     ) for i in range(1, 2**n)
# )

# print(formula)

outer_sum = 0
for i in range(1, 2**n):
    denominator_sum = 0
    for j in range(1, i):
        cosine_inner = (factorial(j-1) + 1) / j
        cosine = cos(pi * cosine_inner)
        denominator_sum_inner = floor(cosine * cosine)
        denominator_sum += denominator_sum_inner

    power_inner = n / denominator_sum
    power = power_inner ** (1/n)

    outer_sum += floor(power)

result =  1 + outer_sum

print(result)
