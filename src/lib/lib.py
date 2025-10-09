def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    try:
        return tuple([min(nums), max(nums)])
    except ValueError:
        return 'ValueError'

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    a = sorted(list(set(nums)))
    return a

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    a = sorted(list(set(nums)))
    return a