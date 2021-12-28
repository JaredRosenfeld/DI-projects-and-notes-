# from collections import Counter, defaultdict,OrderedDict
#
# li = [1,2,3,4,5,6,7,7]
# print(Counter(li))
# default dict uses whatever is in the first section as the default factor if it is not in there
# dict1 = defaultdict(lambda : 5,{
#     'a' : 1,
#     'b' : 2
# })
#
# print(dict1['c'])

# ordered dict states that when putting data in to a dict that the dict will always remain in order, of what you put it in since there is no real order in a dict
# d = OrderedDict()
# d['a'] = 1
# d['b'] = 2
#
#
# d2 = OrderedDict()
# d2['b'] = 2
# d2['a'] = 1
#
# print(d == d2)

from array import array
arr = array('i', [1,2,3])
print(arr[2])
