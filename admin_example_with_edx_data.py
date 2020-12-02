from x_rand import x_rand_admin
import csv

# Download anonymous_student_ids as aids.csv and profile info as profile_info.csv
# Place both in the root of this project.

with open('aids.csv', 'r') as f:
    aids_data={i['User ID']:i for i in csv.DictReader(f)}

with open('profile_info.csv', 'r') as f:
    profile_data={aids_data[i['id']]['Anonymized User ID']:i for i in csv.DictReader(f) if i['enrollment_mode']=='verified'}

aids=profile_data.keys()

data=[
    ['a','b'],
    [1,2],
    [3,4]
]

# Functor
def randomization_process(x, aid):
    out={k:v for k, v in x.select_random(input=data).items()}
    out['aid']=aid
    out['profile_data']=profile_data[aid]
    return out

output=x_rand_admin().recreate(functor=randomization_process, aids=aids)

with open('output.csv', 'w') as f:
    fieldnames = output[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in output_both:
        writer.writerow(i)
