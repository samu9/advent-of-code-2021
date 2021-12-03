from functools import reduce

with open("aoc/day_3/input.txt") as fp:
    input_ = fp.read().splitlines()

def find(criteria, position=0, list_=input_):
    avg = len(list_)/2
    pos_sum = reduce(lambda x, y: x + int(y[position]), list_, 0)
    bit = (int( pos_sum >= avg)
    if criteria == 'most common'
    else int( pos_sum < avg))

    list_=list(filter(lambda i: int(i[position])==bit, list_))
    if len(list_)==1:
        return list_[0] 
    return find(criteria, position + 1, list_)

oxygen_generator_rating = int(find("most common"),2)
co2_scrubber_rating = int(find("least common"), 2)

print(oxygen_generator_rating, co2_scrubber_rating)
print(oxygen_generator_rating * co2_scrubber_rating)