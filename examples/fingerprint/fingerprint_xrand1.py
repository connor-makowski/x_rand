from x_rand import x_rand_admin, x_rand
import csv
# Download anonymous_student_ids as data/aids.csv
# Download profile_info as data/profile_info.csv
with open('data/aids.csv', 'r') as f:
    aids_data={i['User ID']:i for i in csv.DictReader(f)}
with open('data/profile_info.csv', 'r') as f:
    profile_data={aids_data[i['id']]['Anonymized User ID']:i for i in csv.DictReader(f)}
aids=profile_data.keys()
# Your Problem Data Goes Here
# Note: Do not put your randomization code here. This is just for data. See the randomization_process below.
alphanum = [
    ["alphanum"],
    ["0"],["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["A"],["B"],["C"],["D"],["E"],["F"],["G"],["H"],["I"],["J"],["K"],["L"],["M"],["N"],["O"],["P"],["Q"],["R"],["S"],["T"],["U"],["V"],["W"],["X"],["Y"],["Z"],
]
# Put your randomization process in the following def
# Make sure
def randomization_process(x, aid):
    # Don't mess with this. It is just for getting aids and profile data in the output.
    out={
        'aid':aid,
        'profile_data':profile_data[aid]
    }
    # All of your randomization code used in `globals.update` should go below.
    # Note: replace each globals.update with out.update
    out.update(x.fingerprint(alphanum, n_total=5))
    return out

# Remember: Update your upseed
output=x_rand_admin().recreate(functor=randomization_process, aids=aids, upseed=0)

with open('data/output.csv', 'w') as f:
    fieldnames = output[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in output:
        writer.writerow(i)
