import sys
# For python 3
if sys.version_info[0] == 3:
    from x_rand.x_rand import x_rand, x_rand_admin
# For python 2
elif sys.version_info[0] < 3:
    from x_rand import x_rand, x_rand_admin
