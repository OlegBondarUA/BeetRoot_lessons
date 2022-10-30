
# task 01


def number_of_variables():
    a = 1991
    b = 2022
    c = 'Oleg'
    d = a + b
    return a, b, c, d


print(number_of_variables.__code__.co_nlocals)


# task 02

def access_a_function(number):
    def function(numbers):
        a = 4
        d = 5
        result = a + d * numbers // number
        print(result)

    function(10)


# task 03

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def choose_func(nums, func1, func2):
    for num in nums:
        if num < 1:
            return func2(nums)
    return func1(nums)


def square_nums(nums):
    print([num ** 2 for num in nums])


def remove_negatives(nums):
    print([num for num in nums if num > 0])


def main():

    number_of_variables()
    access_a_function(7)
    choose_func(nums1, square_nums, remove_negatives)
    choose_func(nums2, square_nums, remove_negatives)


if __name__ == '__main__':
    main()
