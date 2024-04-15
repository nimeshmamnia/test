def solve(ip, op, op_list):

    # Base Condition
    if len(ip) == 0:
        op_list.append(op)
        return

    # Making 2 copies of outputs. One where we chose to include ip, other we do not.
    op1 = op
    op2 = op + ip[0]

    # Reducing ip length by 1 making sure we print output when ip length is 0 (leaf Node)
    ip = ip[1:]

    # Calling out functions on both outputs.
    solve(ip, op1, op_list)
    solve(ip, op2, op_list)
    return


ip_1 = input("Enter string to find its subsets: ")
# Making sure there are no duplicate characters in string. If there are, printing only unique subsets.
lst = list(set(ip_1))
ip_string = ''.join(lst)
op_string = ""
op_lst = []
print("\n Subsets are: ")
solve(ip_string, op_string, op_lst)
sorted_op = sorted(op_lst)
print(sorted_op)
