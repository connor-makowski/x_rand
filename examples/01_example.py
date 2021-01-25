from x_rand2 import x_rand

e1=[
['a','b'],
[1,2],
[3,4]
]

e2 = [
    ["text", "correct"],
    ["A", "True"],
    ["B", "True"],
    ["1", "False"],
    ["2", "False"],
    ["3", "False"],
    ["4", "False"]
]

e3 = [
    ["female"],
    ["Jenny"],
    ["Carla"],
    ["Mary"],
    ["Jin"],
    ["Marta"],
    ["Sadef"]
]

# Note: edX automatically uses the current student's aid so you should not set this in edX.
anonymous_student_id='0123456789abcdef'

x=x_rand(anonymous_student_id, upseed=23145)

globals().update(x.select_random(e1))
globals().update(x.choices_random(e2, correct_indicator='correct'))
globals().update(x.fingerprint(e3, n_total=3))
print(a, b)
print (text_00, correct_00)
print (text_01, correct_01)
print (text_02, correct_02)
print (text_03, correct_03)
print (female_00, female_01, female_02)
