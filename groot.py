
ans = []

def find_right_sweet(pies, sweet_so_far, x, sweet_remaining, target):
    ans[x] = 1
    
    if(sweet_so_far + pies[x] == target):
        print(ans)
    if(x < len(ans)-1 and sweet_so_far + pies[x] + pies[x+1] <= target):
        find_right_sweet(pies, sweet_so_far + pies[x], x+1, sweet_remaining-pies[x], target)
    if(x < len(ans)-1 and sweet_so_far + pies[x+1] <= target and sweet_so_far + sweet_remaining - pies[x] >= target):
        ans[x] = 0
        find_right_sweet(pies, sweet_so_far, x+1, sweet_remaining-pies[x], target)

def create_empty_list(n):
    for i in range(n):
        ans.append(0)

def findPies(pies, target):
    create_empty_list(len(pies))
    find_right_sweet(pies, 0, 0, sum(pies), target)
    

findPies([1, 2, 3, 2, 1], 6)

print()

ans.clear()
findPies([8, 4, 3, 2, 6, 5], 6)