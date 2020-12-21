import sys
if sys.version_info[0] == 3:
    from x_rand2.x_rand import x_rand, x_rand_admin
elif sys.version_info[0] < 3:
    from x_rand2 import x_rand, x_rand_admin
