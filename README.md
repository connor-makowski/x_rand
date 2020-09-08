# x_rand
Randomization package for [edX] courses

## Features

- Users can:
  - Randomize mathematical problems on edX
  - Randomize multiple choice problems on edX
  - Randomize checkbox problems on edX

## API Documentation
The [full api documentation](https://connor-makowski.github.io/x_rand/x_rand.html) can be found [here](https://connor-makowski.github.io/x_rand/x_rand.html).

### Installation For use in edX
Upload the `python_lib.zip` file to your edX course.
  - WARNING: This will overwrite your current `python_lib.zip` if you already have it.
  - NOTE: If you already have a `python_lib.zip`, you can add the x_rand.py file from `python_lib` directly to your `python_lib` folder, re-zip it and re-upload it.


### Installation For testing and admin use
Make sure you have Python 3.x.x (or higher) installed on your system. You can download it from [python].

```
pip install x_rand
```


### Example Random mathematical problem
1) Initialize an `x_rand` variable with the current student AID:
  ```
  x=x_rand(anonymous_student_id)
  ```

2) Input data:
  ```
  data=[
    ['a','b'],
    [1,2],
    [2,4]
  ]
  ```

3) To use the variables in edX problems, you have to create relevant variables and make them global:
  - To do this use the `globals().update()` function
  - Then randomly select a row out of that data
  ```
  globals().update(x.select_random(data))
  ```
  - Note: Column headers from your data are now available to be called as variables globally. If the first row of data was selected:
  ```
  print (a)
  > 1
  print (b)
  > 2
  ```

4) These can be called into edX scripts as `$a` and `$b` respectively. An example `Blank Advanced Problem` script is below:
```
<problem>
<script type="text/python">
<![CDATA[
from python_lib.x_rand import x_rand

data=[
  ['a','b'],
  [1,2],
  [2,4]
]

x=x_rand(anonymous_student_id)
globals().update(x.select_random(data))

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


### Example Random multiple choice or checkbox problem
1) Initialize an `x_rand` variable with the current student AID:
  ```
  x=x_rand(anonymous_student_id)
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
3) To use the variables in edX problems, you have to create relevant variables and make them global:
  - To do this use a the `globals().update()` function
  - Randomly select four (`n_total=4`) answers where one (`n_true=1`) answer is true (specified as the `correct` column by `correct_indicator='correct'`):
  ```

  globals().update(x.choices_random(data, correct_indicator='correct', n_true=1, n_total=4))
  ```
  - Note: You can now call each of your column headers in the order in which they were randomly selected from `00` to `n_total-1`:
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
from python_lib.x_rand import x_rand

data= [
    ["text", "correct"],
    ["A", "True"],
    ["B", "True"],
    ["1", "False"],
    ["2", "False"],
    ["3", "False"],
    ["4", "False"]
]

x=x_rand(anonymous_student_id)
globals().update(x.choices_random(data, correct_indicator='correct', n_true=1, n_total=4))

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

### Example Fingerprinting problem
This can be used to identify students that post exam problems to outside websites.

While not guaranteed to be unique, large enough lists with sufficient numbers of selected values can almost guarantee a unique result per student.

To fingerprint a problem.
1) Initialize an `x_rand` variable with the current student AID:
  ```
  x=x_rand(anonymous_student_id)
  ```

2) Input data:
  ```
  females = [
      ["female"],
      ["Jenny"],
      ["Carla"],
      ["Mary"],
      ["Jin"],
      ["Marta"],
      ["Sadef"]
  ]
  males = [
      ["male"],
      ["Carter"],
      ["John"],
      ["Jose"],
      ["Luke"],
      ["Adam"],
      ["Ahmed"]
  ]
  ```
3) To use the variables in edX problems, you have to create relevant variables and make them global:
  - To do this, use a simple `globals().update()` function
  - Randomly select and shuffle four (`n_total=4`) female names and four (`n_total=4`) male names:
  ```
  globals().update(x.fingerprint(females, n_total=4))
  globals().update(x.fingerprint(males, n_total=4))
  ```
  - Note: You can now call each of your column headers in the order in which they were randomly selected from `00` to `n_total-1`:
  ```
  print (female_00, male_03)
  > Jenny Carter
  ```

5) These can be called into edX scripts as `$female_XX` and `$male_XX` respectively. Similarly, all columns added can be called as `mycol_XX`. An example `Blank Advanced Problem` script is below:
```
<problem>
 <script type="text/python">
<![CDATA[
from python_lib.x_rand import x_rand

females = [
    ["female"],
    ["Jenny"],
    ["Carla"],
    ["Mary"],
    ["Jin"],
    ["Marta"],
    ["Sadef"]
]

males = [
    ["male"],
    ["Carter"],
    ["John"],
    ["Jose"],
    ["Luke"],
    ["Adam"],
    ["Ahmed"]
]

x=x_rand(anonymous_student_id)
globals().update(x.fingerprint(females, n_total=4))
globals().update(x.fingerprint(males, n_total=4))

]]>
</script>
<multiplechoiceresponse>
<label>$female_00, $female_01, $female_02, $female_03, $male_00, $male_01, $male_02 and $male_03 all walk into a bar. One of them should have seen it.<br/>Is this a funny joke?</label>
<description>Select a response below</description>
<choicegroup type="MultipleChoice">
    <choice correct="false">No</choice>
    <choice correct="true">Yes</choice>
  </choicegroup>
</multiplechoiceresponse>
</problem>
```

### Recreating Student data
See `./example.py` and `./admin_example.py` for an example on how to recreate student data on your local machine.


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

[edX]: <https://www.edx.org/>
[python]: <https://www.python.org/downloads/>
