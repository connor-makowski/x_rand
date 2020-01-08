import random
class x_rand:
    def __init__(self):
        try:
            randomseed = int(anonymous_student_id, 16)
        except:
            randomseed = 1
        random.seed(randomseed)

    def reseed(self, anonymous_student_id=None):
        try:
            randomseed = int(anonymous_student_id, 16)
        except:
            randomseed = 1
        random.seed(randomseed)

    def formatter(self, input):
        # Note: __builtins__(py3) and __builtin__(py2) not accessable in edX
        # Possible errors if users create variable named `list` or `tuple`
        # Ideal: if isinstance(input[0], (__builtins__.list, __builtins__.tuple)):
        if isinstance(input[0], (list, tuple)):
            return [dict(zip(input[0],row)) for row in input[1:]]
        else:
            return input

    def select_random(self, input):
        input=self.formatter(input)
        return random.choice(input)

    def sample_if(self, input, variable, string, sample_size):
        return random.sample([input[i] for i in range(len(input)) if (string in input[i][variable])], sample_size)

    def shuffle_and_stack_dicts_numerically(self, dict_list):
        random.shuffle(dict_list) # Note: Random shuffle happens in place
        return {str(key)+'_'+str(i).zfill(2): dict_list[i][key] for i in range(len(dict_list)) for key in dict_list[i]}

    def choices_random(self, input, correct_indicator, n_true=1, n_out=4):
        input=self.formatter(input)
        choices=self.sample_if(input, correct_indicator, 'True', n_true)+self.sample_if(input, correct_indicator, 'False', n_out-n_true)
        return self.shuffle_and_stack_dicts_numerically(choices)

    def fingerprint(self, input, n_out):
        input=self.formatter(input)
        choices=random.sample(input, n_out)
        return self.shuffle_and_stack_dicts_numerically(choices)


class x_rand_admin:
    def extended_functor(self, functor, x, aid):
        x.reseed(anonymous_student_id=aid)
        return functor(x, aid)

    def recreate(self, functor, aids):
        x=x_rand()
        return [self.extended_functor(functor=functor, x=x, aid=aid) for aid in aids]
