from x_rand import x_rand_admin

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

def randomization_process(x, aid):
    return {
        'aid': aid,
        'e1': x.select_random(e1),
        'e2': x.choices_random(e2, correct_indicator='correct'),
        'e3': x.fingerprint(e3, n_out=3),
    }

print(x_rand_admin().recreate(randomization_process, aids=['staff','0123456789abcdef','0123456789abcde0']))
