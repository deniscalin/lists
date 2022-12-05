file = open("/Users/deniscalin/Downloads/members.txt", 'r')
members = file.readlines()
file.close()

new_member = input("Add a new member: ") + "\n "
members.append(new_member)
file = open("/Users/deniscalin/Downloads/members.txt", 'w')
file.writelines(members)
file.close()