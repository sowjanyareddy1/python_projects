# There is an array of  integers.
#  There are also 2 disjoint sets, A  and B, each containing m integers.
# You like all the integers in set A and dislike all the integers in set B.
# Your initial happiness is 0.
# For each i integer in the array, if i belongs to A , you add 1 to your happiness.
# If i belongs to B, you add -1 to your happiness.
# Otherwise, your happiness does not change.
# Output your final happiness at the end.

n,m = input().split()
happiness = 0
array = input().split()
a,b = set(input().split()),set(input().split())
for i in array:
    if i in a and i not in b:
        happiness += 1
    elif i in b and i not in a:
        happiness -= 1
print(happiness)