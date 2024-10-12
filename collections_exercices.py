from collections import Counter,OrderedDict,namedtuple,defaultdict,deque

# s="aaaaaaaabbbbbbcccccdddddffff"
# my_counter=Counter(s)
# # print(my_counter)
# # print(my_counter.keys())
# # print(my_counter.values())
# print(my_counter.most_common(1)[0][1])

# Point=namedtuple('Point','x,y')
# pt=Point(1,-4)
# print(pt)
# print(pt.x, pt.y)

# ordered_dict=OrderedDict()
# ordered_dict['a']=1
# ordered_dict['b']=2
# ordered_dict['c']=3
# ordered_dict['d']=4
# print(ordered_dict)

# d=defaultdict(float)
# d['a']=1
# d['b']=2
# print(d)
# print(d['c'])

d=deque()
d.append(1)
d.append(2)
d.appendleft(3)

d.pop()
d.popleft()
d.extend([4,5,6])
d.extendleft([-2,-1,0])
print(d)