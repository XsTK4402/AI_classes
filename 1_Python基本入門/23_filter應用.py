a = [1, 2, 3, 4]
b = ["1", "2", "3", "4"]


def is_even(n: list[int]) -> bool:
    "判斷書入是否為偶數"
    return n % 2 == 0

print(is_even(a))

print(list(filter(lambda n: n % 2 == 0,a)))
