from x_rand import x_rand

e1=[
['a','b'],
[1,2],
[3,4]
]

# Equivalent to:
# e1=(
# ('a','b'),
# (1,2),
# (3,4)
# )
#
# Equivalent to:
# e1=[
# {'a':1, 'b':2},
# {'a':3, 'b':4}
# ]

e2 = [
    ["text", "correct"],
    ["A", "True"],
    ["B", "True"],
    ["1", "False"],
    ["2", "False"],
    ["3", "False"],
    ["4", "False"]
]

# Equivalent to
# e2 = (
#     ("text", "correct"),
#     ("A", "True"),
#     ("B", "True"),
#     ("1", "False"),
#     ("2", "False"),
#     ("3", "False"),
#     ("4", "False")
# )
# Equivalent to
# e2 = [
#     {"text":"A", "correct":"True"},
#     {"text":"B", "correct":"True"},
#     {"text":"1", "correct":"False"},
#     {"text":"2", "correct":"False"},
#     {"text":"3", "correct":"False"},
#     {"text":"4", "correct":"False"}
# ]

e3 = [
    ["female"],
    ["Jenny"],
    ["Carla"],
    ["Mary"],
    ["Jin"],
    ["Marta"],
    ["Sadef"]
]
# Equivalent to
# e3 = (
#     ("female"),
#     ("Jenny"),
#     ("Carla"),
#     ("Mary"),
#     ("Jin"),
#     ("Marta"),
#     ("Sadef")
# )
# Equivalent to
# e3 = [
#     {"female":"Jenny"},
#     {"female":"Carla"},
#     {"female":"Mary"},
#     {"female":"Jin"},
#     {"female":"Marta"},
#     {"female":"Sadef"}
# ]



x=x_rand()
globalize=lambda x: globals().update(x)

globalize(x.select_random(e1))
globalize(x.choices_random(e2, correct_indicator='correct'))
globalize(x.fingerprint(e3, n_total=3))
print(a, b)
print (text_00, correct_00)
print (text_01, correct_01)
print (text_02, correct_02)
print (text_03, correct_03)
print (female_00, female_01, female_02)
# Print a variable out of range
# print (text_04, correct_04)
