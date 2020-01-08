# x_rand
Randomization package for [edX] courses

## Features

- Users can:
  - Randomize mathematical problems on edX
  - Randomize multiple choice problems on edX
  - Randomize checkbox problems on edX

## Setup

Make sure you have Python 3.6.x (or higher) or Python2.7.x (or higher) installed on your system. You can download it from [python].

<br/><hr/>

### Installation

```
pip install x_rand
```
<br/><hr/>

### Example Random mathematical problem
1) Initialize an `x_rand` variable:
  ```
  x=x_rand()
  ```

2) Input data:
  ```
  data=[
    ['a','b'],
    [1,2],
    [2,4]
  ]
  ```

3) To use the variables in edX problems, you have to make the create relevant variables and make them global:
    - To do this use a simple `globalize` function `globalize=lambda x: globals().update(x)`
    - Then randomly select a row out of that data
  ```
  globalize=lambda x: globals().update(x)
  globalize(x.select_random(data))
  ```
  - Note: Column headers from your data are now available to be called as variables globally. If the first row of data was selected:
  ```
  print (a)
  > 1
  print (b)
  > 2
  ```

5) These can be called into edX scripts as `$a` and `$b` respectively. An example `Blank Advanced Problem` script is below:
```
<problem>
<script type="text/python">
<![CDATA[

data=[
  ['a','b'],
  [1,2],
  [2,4]
]

globalize=lambda x: globals().update(x)
x=x_rand()
globalize(x.select_random(data))

]]>
</script>
<numericalresponse answer="$b">
<label>What is $a x 2?</label>
<description>Enter your answer below.</description>
<responseparam type="tolerance" default=".1"/>
<formulaequationinput/>
</numericalresponse>
</problem>
```


<br/><hr/>

### Example Random multiple choice or checkbox problem
1) Initialize an `x_rand` variable:
  ```
  x=x_rand()
  ```

2) Input data:
  ```
  data = [
    ["text", "correct"],
    ["A", "True"],
    ["B", "True"],
    ["1", "False"],
    ["2", "False"],
    ["3", "False"],
    ["4", "False"]
  ]
  ```
3) To use the variables in edX problems, you have to make the create relevant variables and make them global:
    - To do this use a simple `globalize` function `globalize=lambda x: globals().update(x)`
  Randomly select four (`n_out=4`) answers where one (`n_true=1`) answer is true (specified as the `correct` column by `correct_indicator='correct'`):
  ```
  globalize=lambda x: globals().update(x)
  globalize(x.choices_random(data, correct_indicator='correct', n_true=1, n_out=4))
  ```
  - Note: You can now call each of your column headers in the order in which they were randomly selected from `00` to `n_out-1`:
  ```
  print (text_00, correct_00)
  > 2, False
  print (text_01, correct_01)
  > A, True
  print (text_02, correct_02)
  > 3, False
  print (text_03, correct_03)
  > 1, False
  print (text_04, correct_04)
  > NameError: name 'text_04' is not defined
  ```

5) These can be called into edX scripts as `$text_XX` and `$correct__XX` respectively. Similarly, all columns added can be called as `mycol_XX`. An example `Blank Advanced Problem` script is below:
```
<problem>
<script type="text/python">
<![CDATA[

data= [
    ["text", "correct"],
    ["A", "True"],
    ["B", "True"],
    ["1", "False"],
    ["2", "False"],
    ["3", "False"],
    ["4", "False"]
]

globalize=lambda x: globals().update(x)
x=x_rand()
globalize(x.choices_random(data, correct_indicator='correct', n_true=1, n_out=4))

]]>
</script>
<choiceresponse>
<label> Which of the following are Letters? </label>
<description>Select all that apply.</description>
<checkboxgroup>
<choice correct="$correct_00">$text_00</choice>
<choice correct="$correct_01">$text_01</choice>
<choice correct="$correct_02">$text_02</choice>
<choice correct="$correct_03">$text_03</choice>
<choice correct="False">None of the above</choice>
</checkboxgroup>
</choiceresponse>
</problem>
```




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

[edX]: <https://www.edx.org/>
[python]: <https://www.python.org/downloads/>
