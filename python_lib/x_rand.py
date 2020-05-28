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
        if isinstance(input[0], (list, tuple)):
            return [dict(zip(input[0],row)) for row in input[1:]]
        else:
            return input

    def select_random(self, input):
        input=self.formatter(input)
        return random.choice(input)

    def sample_if(self, input, variable, string, sample_size):
        return random.sample([input[i] for i in range(len(input)) if (string in input[i][variable])], sample_size)

    def shuffle_and_stack_dicts_numerically(self, dict_list, n_digits=2):
        random.shuffle(dict_list)
        return {str(key)+'_'+str(i).zfill(n_digits): dict_list[i][key] for i in range(len(dict_list)) for key in dict_list[i]}

    def choices_random(self, input, correct_indicator, n_true=1, n_total=4):
        input=self.formatter(input)
        choices=self.sample_if(input, correct_indicator, 'True', n_true)+self.sample_if(input, correct_indicator, 'False', n_total-n_true)
        return self.shuffle_and_stack_dicts_numerically(choices)

    def fingerprint(self, input, n_total):
        input=self.formatter(input)
        choices=random.sample(input, n_total)
        return self.shuffle_and_stack_dicts_numerically(choices)
