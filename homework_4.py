numbers_1 = [3, 1]
numbers_2 = [3, 2, -1, 4]
numbers_3 = [5, 3, 2, 8, 1, 4]

def smart_sorting(number):
  sort_1 = list(sorted(number))
  for index, item in enumerate(sort_1):
      if not sort_1[index] % 2:
        sort_1.pop(index)

  for index, item in enumerate(number):
    if item % 2 == 0:
      sort_1.insert(index, item)
  return(sort_1)

EXEMPLES = (
   ([3 , 1], [1, 3]),
   ([3, 2, -1, 4], [-1, 2, 3, 4]),
   ([5,3,2,8,1,4], [1,3,2,8,5,4])
)
for exempl in EXEMPLES:
  request = exempl[0]
  answer = exempl[1]
  assert smart_sorting (request) == answer

print(smart_sorting(numbers_1))
print(smart_sorting(numbers_2))
print(smart_sorting(numbers_3))