import sys
if sys.version_info[0] == 3:
    from x_rand.x_rand import x_rand, x_rand_admin
elif sys.version_info[0] < 3:
    from x_rand import x_rand, x_rand_admin
