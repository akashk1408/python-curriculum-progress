def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter target: "))
    print("Indices:", two_sum(nums, target))
