from x_rand2 import x_rand

data=[
  ['a','b'],
  [1,2],
  [2,4]
]

# Note: edX automatically uses the current student's aid so you should not set this in edX.
anonymous_student_id='0123456789abcdef'

x=x_rand(anonymous_student_id, upseed=28)
globals().update(x.select_random(data))

print('a: ', a)
print('b: ', b)
