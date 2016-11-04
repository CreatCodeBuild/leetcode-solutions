def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    track = []
    track.append([1]*len(nums))
    j = 0   # index over nums
    i = 1   # max increasing subsequence length
            # track[i][j]
    while i < len(nums):
        track.append([None]*len(nums))
        track[i][0] = 1
        for j in range(1, len(nums)):
            if nums[j] > nums[j-1]:
                track[i][j] = track[i-1][j-1] + 1
            else:
                track[i][j] = track[i][j-1]
        if track[i][-1] < i+1:
            break
        i += 1
    for row in track:
        print(row)

    # backtrack, retrive the sequence
    ret = []
    j = len(nums) - 1
    i = len(track) - 1
    print(i, j)
    print(track[i][j])
    while True:
        print(i, j)
        if track[i][j] == track[i][j-1]:
            j -= 1
        elif track[i][j] == track[i-1][j]:
            i -= 1
        elif track[i][j] == track[i-1][j-1] + 1:
            ret.append(nums[j])
            i -= 1; j -= 1
        if i == 0:
            ret.append(nums[j])
            break

    return ret

print(lengthOfLIS([1,6,1,2,3,4]))
