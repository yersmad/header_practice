team_name = str(input())
member1 = str(input())
member2 = str(input())
member3 = str(input())
members = [member1, member2, member3]
members.sort()
print(team_name, ": ", ", ".join(members), sep="")
