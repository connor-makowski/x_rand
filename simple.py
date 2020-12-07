from x_rand.x_rand import x_rand

data=[
  ['a','b'],
  [1,2],
  [2,4]
]

globalize=lambda x: globals().update(x)
x=x_rand()
globalize(x.select_random(data))

print('a: ', a)
print('b: ', b)
