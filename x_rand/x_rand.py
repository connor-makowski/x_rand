import random

class utils:
    """
    Utilities to support the main x_rand functions
    """
    def __init__(self):
        """
        Attempts to pull the anonymous_student_id if it exists and set it as the random seed

        If the `anonymous_student_id` fails for some reason (eg: In testing or while staff) sets the random seed to 1
        """
        try:
            randomseed = int(anonymous_student_id, 16)
        except:
            randomseed = 1
        random.seed(randomseed)

    def reseed(self, anonymous_student_id=None):
        """
        Reseed the random seed to a specific value (used to recreate student data sets)
        """
        try:
            randomseed = int(anonymous_student_id, 16)
        except:
            randomseed = 1
        random.seed(randomseed)

    def formatter(self, input):
        """
        Takes in:

            `input`:
                Type: a (list | tuple) of (lists | tuples | dictionaries)
                What: data to format

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
        random.shuffle(dict_list) # Note: Random shuffle happens in place
        return {str(key)+'_'+str(i).zfill(n_digits): dict_list[i][key] for i in range(len(dict_list)) for key in dict_list[i]}

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
        """
        input=self.formatter(input)
        choices=random.sample(input, n_total)
        return self.shuffle_and_stack_dicts_numerically(choices)

class x_rand_admin:
    def extended_functor(self, functor, x, aid):
        """
        Internal function to allow list comprehension code to apply more complex operations like reseeding
        """
        x.reseed(anonymous_student_id=aid)
        return functor(x, aid)

    def recreate(self, functor, aids):
        """
        Given a `functor` and list of `aids` (anonymous_student_ids), returns a list of all student outputs

        Requires:

            - `functor`
                Type: function
                What: A function of any name that takes in two args of any name where:
                    - the first arg represents an x_rand instnace to be used for recreating data
                    - the second arg represents an anonymous_student_id to store
                    - returns a dictionary of relevant output to be stored in a list and returned by this `recreate` function
                    - Note: Order of randomization is important because of how random seeds
                    - This function must match the randomization order as it was coded in edX
            - `aids`
                - Type: list of strings 
                - What: A list of anonymous_student_ids (16 digit string of hex characters) to recreate data with

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
        return [self.extended_functor(functor=functor, x=x, aid=aid) for aid in aids]
