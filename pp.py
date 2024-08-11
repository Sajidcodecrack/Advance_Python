nums = [-1, 0, 1, 2, -1, -4]
pointer2 = len(nums) - 1
output = []
p = []

nums.sort()

for i in range(len(nums) - 2):
   
    # Reset korte hbe pointer iteration e 
    pointer1 = i + 1
    pointer2 = len(nums) - 1

    while pointer1 < pointer2:
        total_sum = nums[i] + nums[pointer1] + nums[pointer2]

        if total_sum < 0:
            pointer1 += 1
        elif total_sum > 0:
            pointer2 -= 1
        else:
            output.append([nums[i], nums[pointer1], nums[pointer2]])

            
            pointer1 += 1
            pointer2 -= 1

# Remove duplicate korte bol output e 
for i in output:
    if i not in p:
        p.append(i)

print(p)
