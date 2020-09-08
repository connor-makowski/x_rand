import random

class utils:
    """
    Utilities to support the main x_rand functions
    """
    def __init__(self, anonymous_student_id=None, upseed=0, infinite_random=False):
        """
        Attempts to pull the anonymous_student_id if it exists and set it as the random seed

        Takes in:
        
        - `anonymous_student_id`:
            - Type: hex int
            - What: edX AID
            - Default: 0
        - `upseed`:
            - Type: int
            - What: incremental value to increase the anonymous_student_id hash by
            - Default: 0
        - `infinite_random`:
            - Type: bool
            - What: Flag to generate a random upseed on every initialization of the problem
            - Default: False
            - Note: Overwrites any specified upseed

        EGs:

        ```
        data=[
          ['a','b'],
          [1,2],
          [2,4]
        ]

        x=x_rand(anonymous_student_id, upseed=1)
        globals().update(x.select_random(data))
        print(a, b)
        ```

        ```
        data=[
          ['a','b'],
          [1,2],
          [2,4]
        ]

        x=x_rand(infinite_random=True)
        globals().update(x.select_random(data))
        print(a, b)
        ```
        """
        try:
            self.anonymous_student_id = anonymous_student_id
        except:
            self.anonymous_student_id = None
        if infinite_random:
            upseed=random.uniform(1,1000000)
        self.reseed(anonymous_student_id=self.anonymous_student_id, upseed=upseed)

    def reseed(self, anonymous_student_id=None, upseed=0):
        """
        Reseed the random seed to a specific value (used to recreate student data sets)
        """
        try:
            randomseed = int(anonymous_student_id, 16)+upseed
        except:
            randomseed = 1+upseed
        random.seed(randomseed)

    def formatter(self, input):
        """
        Takes in:

        - `input`:
            - Type: a (list | tuple) of (lists | tuples | dictionaries)
            - What: data to format

        Checks if the first element of a data set is a list or a tuple and if so, converts it to a list of dictionaries that use the headers in the first row as assigned values

        The following inputs give equivalent outputs:

        ```
        e1=[
        ['a','b'],
        [1,2],
        [3,4]
        ]

        e1=(
        ('a','b'),
        (1,2),
        (3,4)
        )

        e1=[
        {'a':1, 'b':2},
        {'a':3, 'b':4}
        ]
        ```

        All of the above examples are returned as:

        ```
        e1=[
        {'a':1, 'b':2},
        {'a':3, 'b':4}
        ]
        ```
        """
        # Note: __builtins__(py3) and __builtin__(py2) not accessable in edX
        # Possible errors if users create variable named `list` or `tuple`
        # Ideal: if isinstance(input[0], (__builtins__.list, __builtins__.tuple)):
        if isinstance(input[0], (list, tuple)):
            return [dict(zip(input[0],row)) for row in input[1:]]
        else:
            return input

    def sample_if(self, input, variable, string, sample_size):
        """
        Returns `sample_size` items from a subset of `input` items where a `string` is contained in a given `variable`

        Takes in:

        - input:
            - Type: list | tuple (as specified by self.formatter)
            - What: Input to select random choices from
        - variable:
            - Type: string
            - What: Variable name to check for existence of `string`
        - string:
            - Type: string
            - What: String to check if exists in `variable` and create a subset to sample from
        - sample_size:
            - Type:int
            - What: The number of results to return
        """
        return random.sample([input[i] for i in range(len(input)) if (string in input[i][variable])], sample_size)

    def shuffle_and_stack_dicts_numerically(self, dict_list, n_digits=2):
        """
        Returns a single dictionary with stacked (numerically with n_digits starting at all zeros) renamed values.

        Takes in:

        - `dict_list`:
            - Type: list of dictionaries (output of self.formatter)
            - What: The list of dictionaries to shuffle in place
        - `n_digits`:
            - Type: int
            - What: The number of digits to name returned variables with
            - Default: 2

        EG:
        ```
        e1=[
        {'a':1, 'b':2},
        {'a':3, 'b':4}
        ]

        self.shuffle_and_stack_dicts_numerically(e1, n_digits=2)
        ```

        Would return (possible variations depending on seed during random.shuffle):
        ```
        {'a_00':1, 'b_00':2, 'a_01':3, 'b_01':4}
        ```
        """
        random_state=random.getstate()
        self.reseed(self.anonymous_student_id, upseed=self.hash(str(dict_list)))
        random.shuffle(dict_list) # Note: Random shuffle happens in place
        random.setstate(random_state)
        return {str(key)+'_'+str(i).zfill(n_digits): dict_list[i][key] for i in range(len(dict_list)) for key in dict_list[i]}

    def hash(self, string):
        """
        Returns a consistent hash like (positive integer) of an object given a string.

        Used to access a non random hash like function since none are available in edX by default

        EG:

        ```
        x=str({'a':1})
        ```

        Would consistently return:
        ```
        3843346
        ```
        """
        return sum([int(format(ord(x), 'b')) for x in string])

class x_rand(utils):
    """
    Randomization class with functions to enable randomization in edX
    """
    def select_random(self, input):
        """
        Returns a single row chosen randomly from the formatted data set

        Takes in:

        - input:
            - Type: list | tuple (as specified by self.formatter)
            - What: Input to select random choices from

        EG:

        ```
        data=[
          ['a','b'],
          [1,2],
          [2,4]
        ]

        x=x_rand()
        globals().update(x.select_random(data))
        print(a, b)
        ```
        """
        input=self.formatter(input)
        return random.choice(input)

    def choices_random(self, input, correct_indicator, n_true=1, n_total=4):
        """
        Returns `n_total` answers where `n_true` answers are true (specified as the `correct` column with `correct_indicator`)

        Takes in:

        - input:
            - Type: list | tuple (as specified by self.formatter)
            - What: Input to select random choices from
        - correct_indicator:
            - Type: string
            - What: variable name to check if values are true when selecting `n_true` answers
        - n_true:
            - Type: int
            - What: Number of true answers to return
        - n_total:
            - Type: int
            - What: Number of total answers to return

        EG:

        ```
        data= [
            ["text", "correct"],
            ["A", "True"],
            ["B", "True"],
            ["1", "False"],
            ["2", "False"],
            ["3", "False"],
            ["4", "False"]
        ]

        x=x_rand()
        globals().update(x.choices_random(data, correct_indicator='correct', n_true=1, n_total=4))
        print (text_00, correct_00)
        print (text_01, correct_01)
        print (text_02, correct_02)
        print (text_03, correct_03)
        ```
        """
        input=self.formatter(input)
        choices=self.sample_if(input, correct_indicator, 'True', n_true)+self.sample_if(input, correct_indicator, 'False', n_total-n_true)
        return self.shuffle_and_stack_dicts_numerically(choices)

    def fingerprint(self, input, n_total):
        """
        Returns `n_total` results from a list of inputs

        Takes in:

        - input:
            - Type: list | tuple (as specified by self.formatter)
            - What: Input to select random choices from
        - n_total:
            - Type: int
            - What: Number of total answers to return

        EG:

        ```
        males = [
            ["male"],
            ["Carter"],
            ["John"],
            ["Jose"],
            ["Luke"],
            ["Adam"],
            ["Ahmed"]
        ]

        x=x_rand()
        globals().update(x.fingerprint(males, n_total=2))
        print(male_00, male_01)
        ```
        """
        input=self.formatter(input)
        choices=random.sample(input, n_total)
        return self.shuffle_and_stack_dicts_numerically(choices)

class x_rand_admin:
    def extended_functor(self, functor, x, aid, upseed):
        """
        Internal function to allow list comprehension code to apply more complex operations like reseeding
        """
        x.reseed(anonymous_student_id=aid, upseed=upseed)
        return functor(x, aid)

    def recreate(self, functor, aids, upseed=0):
        """
        Given a `functor` and list of `aids` (anonymous_student_ids), returns a list of all student outputs

        Requires:

            - `functor`
                - Type: function
                - What: A function of any name that takes in two args of any name where:
                    - the first arg represents an x_rand instnace to be used for recreating data
                    - the second arg represents an anonymous_student_id to store
                    - returns a dictionary of relevant output to be stored in a list and returned by this `recreate` function
                    - Note: Order of randomization is important because of how random seeds
                    - This function must match the randomization order as it was coded in edX
            - `aids`
                - Type: list of strings
                - What: A list of anonymous_student_ids (16 digit string of hex characters) to recreate data with

        Optional:

            - `upseed`:
                - Type: int
                - What: The upseed used when generating the problem in edX
                - Default: 0

        Example:

        ```
        # DATA HERE

        # Functor
        def randomization_process(x, aid):
            return {
                'aid': aid,
                'e1': x.select_random(e1),
                'e2': x.choices_random(e2, correct_indicator='correct'),
                'e3': x.fingerprint(e3, n_total=3),
            }

        aids=['staff','0123456789abcdef','0123456789abcde0']
        output=x_rand_admin().recreate(functor=randomization_process, aids=aids)

        ```
        """
        x=x_rand()
        return [self.extended_functor(functor=functor, x=x, aid=aid, upseed=upseed) for aid in aids]
