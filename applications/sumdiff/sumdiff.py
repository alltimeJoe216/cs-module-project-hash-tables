"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
q = set(range(1, 200))

#

def f(x):
    return x * 4 + 6

"""
iterate through q, get sum of pairs, store in dictionary

iterate through q, get diff each pair, return if match, or return nil

"""

def find_matches(l):
    result = []
    additions = {}
    subtractions = {}
  
    for key, value in enumerate(l):
        for next_key, next_value in enumerate(l): # not very efficient...
            if (key, next_key) not in additions.keys():
                additions[(key, next_key)] = value + next_value
            
            if (next_key, key) not in subtractions.keys():
                sub_val = next_value - value
                subtractions[(next_key, key)] = sub_val

    for v in additions:
        for v2 in subtractions:
            if additions[v] == subtractions[v2]:
                result.append((v, v2))
    return result

print(find_matches(q))
