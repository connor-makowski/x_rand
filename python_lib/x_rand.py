import random

class utils:
    def __init__(self, anonymous_student_id=None, upseed=0, infinite_random=False):
        try:
            self.anonymous_student_id = anonymous_student_id
        except:
            self.anonymous_student_id = None
        if infinite_random:
            upseed=random.uniform(1,1000000)
        self.reseed(anonymous_student_id=self.anonymous_student_id, upseed=upseed)

    def reseed(self, anonymous_student_id=None, upseed=0):
        try:
            randomseed = int(anonymous_student_id, 16)+upseed
        except:
            randomseed = 1+upseed
        random.seed(randomseed)

    def formatter(self, input):
        if isinstance(input[0], (list, tuple)):
            return [dict(zip(input[0],row)) for row in input[1:]]
        else:
            return input

    def sample_if(self, input, variable, string, sample_size):
        return random.sample([input[i] for i in range(len(input)) if (string in input[i][variable])], sample_size)

    def shuffle_and_stack_dicts_numerically(self, dict_list, n_digits=2):
        random_state=random.getstate()
        self.reseed(self.anonymous_student_id, upseed=self.hash(str(dict_list)))
        random.shuffle(dict_list)
        random.setstate(random_state)
        return {str(key)+'_'+str(i).zfill(n_digits): dict_list[i][key] for i in range(len(dict_list)) for key in dict_list[i]}

    def hash(self, string):
        return sum([int(format(ord(x), 'b')) for x in string])

class x_rand(utils):
    def select_random(self, input):
        input=self.formatter(input)
        return random.choice(input)

    def choices_random(self, input, correct_indicator, n_true=1, n_total=4):
        input=self.formatter(input)
        choices=self.sample_if(input, correct_indicator, 'True', n_true)+self.sample_if(input, correct_indicator, 'False', n_total-n_true)
        return self.shuffle_and_stack_dicts_numerically(choices)

    def fingerprint(self, input, n_total):
        input=self.formatter(input)
        choices=random.sample(input, n_total)
        return self.shuffle_and_stack_dicts_numerically(choices)
