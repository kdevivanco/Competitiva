def dados():
    nums = list(map(int, input().split(" ")))

    diff = abs(nums[0] - nums[1])

    menor = min(nums)

    for i in range(menor, menor + diff + 1):
        print(i + 1)

dados()
