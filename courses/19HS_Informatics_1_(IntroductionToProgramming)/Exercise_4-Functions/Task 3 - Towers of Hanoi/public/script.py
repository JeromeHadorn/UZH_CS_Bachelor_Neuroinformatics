# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def req_steps(num_disks):
    if num_disks == 0:
        return 0
    # implement this function
    return 1 + req_steps(num_disks - 1) + req_steps(num_disks - 1)


# You can play around with your solution from within this block.
if __name__ == '__main__':
    print("For moving {} disks, {} steps are required.".format(3, req_steps(3)))
