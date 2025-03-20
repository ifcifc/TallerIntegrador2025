from stream import Stream

vector_original = list(range(101))

stream_original = Stream(vector_original)

# Filter Test
filter_1 = stream_original.copy().filter(lambda v: v%20==0).to_tuple()
print("Filter Test:", filter_1 == (0,20,40,60,80,100))

# All test
all_test_1 = stream_original.copy().all(lambda v: v%3==0)
all_test_2 = stream_original.copy().all(lambda v: v%2==0)
all_test_3 = stream_original.copy().filter(lambda v: v%3==0).all(lambda v: v%3==0)
all_result = not(all_test_1 or all_test_2) and all_test_3
print("All Test:", all_result)
if not all_result:
    print("Results:", all_test_1, all_test_2, all_test_3)

# Any test
any_test_1 = stream_original.copy().any(lambda v: v%3==0)
any_test_2 = stream_original.copy().any(lambda v: v%2==0)
any_test_3 = stream_original.copy().filter(lambda v: v%2!=0).any(lambda v: v%2==0)
any_result = any_test_1 and any_test_2 and not any_test_3
print("Any Test:", any_result)
if not any_result:
    print("Results:", any_test_1, any_test_2, any_test_3)

# Peek test
peek_test_1 = stream_original.copy().filter(lambda v: v%15).to_list()
stream_original.peek(lambda v: peek_test_1.remove(v) if v in peek_test_1 else None)
print("Peek Test:", len(peek_test_1)==0)

# Reduce test
reduce_test_1 = stream_original.copy().reduce(lambda acc, v: acc + v)
reduce_test_2 = stream_original.copy().filter(lambda v: v % 2 == 0).reduce(lambda acc, v: acc + v)
reduce_result = reduce_test_1 == sum(vector_original) and reduce_test_2 == sum(v for v in vector_original if v % 2 == 0)
print("Reduce Test:", reduce_result)
if not reduce_result:
    print("Results:", reduce_test_1, reduce_test_2)

# Min test
min_test_1 = stream_original.copy().min()
min_test_2 = stream_original.copy().filter(lambda v: v % 2 == 0).min()
min_result = min_test_1 == 0 and min_test_2 == 0
print("Min Test:", min_result)
if not min_result:
    print("Results:", min_test_1, min_test_2)

# Max test
max_test_1 = stream_original.copy().max()
max_test_2 = stream_original.copy().filter(lambda v: v % 2 == 0).max()
max_result = max_test_1 == 100 and max_test_2 == 100
print("Max Test:", max_result)
if not max_result:
    print("Results:", max_test_1, max_test_2)

# First test
first_test_1 = stream_original.copy().first()
first_test_2 = stream_original.copy().filter(lambda v: v % 2 == 0).first()
first_result = first_test_1 == 0 and first_test_2 == 0
print("First Test:", first_result)
if not first_result:
    print("Results:", first_test_1, first_test_2)

# Last test
last_test_1 = stream_original.copy().last()
last_test_2 = stream_original.copy().filter(lambda v: v % 2 == 0).last()
last_result = last_test_1 == 100 and last_test_2 == 100
print("Last Test:", last_result)
if not last_result:
    print("Results:", last_test_1, last_test_2)

# Limit test
limit_test_1 = stream_original.copy().limit(10).to_list()
limit_result = len(limit_test_1)==10
print("Limit Test:", limit_result)
if not limit_result:
    print("Results:", limit_test_1)

# Count test
count_test_1 = stream_original.copy().count()
count_test_2 = stream_original.copy().filter(lambda v: v % 2 == 0).count()
count_result = count_test_1 == len(vector_original) and count_test_2 == len(vector_original)//2+1
print("Count Test:", count_result)
if not count_result:
    print("Results:", count_test_1, count_test_2)

#Map test
map_test_1 = stream_original.copy().filter(lambda v: v%9==0).limit(3).map(lambda v: v//3)
map_result = map_test_1.to_tuple() == (0, 9//3, 18//3)
print("Map Test:", map_result)

# Reverse test
reverse_test_1 = stream_original.copy().reverse().to_list()
reverse_test_2 = stream_original.copy().reverse().filter(lambda v: v%3==0).limit(3).to_tuple()
reverse_result = reverse_test_1 == list(reversed(vector_original)) and reverse_test_2 == (99, 96, 93)
print("Reverse Test:", reverse_result)
if not reverse_result:
    print("Results:", reverse_test_1, reverse_test_2)

# Sort test
sort_test_1 = stream_original.copy().sort().to_list()
sort_test_2 = stream_original.copy().sort(reverse=True).to_list()
sort_result = sort_test_1 == sorted(vector_original) and sort_test_2 == sorted(vector_original, reverse=True)
print("Sort Test:", sort_result)
if not sort_result:
    print("Results:", sort_test_1, sort_test_2)

# Each test
each_test_1 = []
stream_original.copy().each(each_test_1.append)
each_result = each_test_1 == vector_original
print("Each Test:", each_result)
if not each_result:
    print("Results:", each_test_1)
