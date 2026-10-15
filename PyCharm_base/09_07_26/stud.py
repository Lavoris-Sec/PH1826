studBirthYear = [2000, 1997, 2002, 1999, 2007, 2009]

studAges = []

studAges = str(list(map(lambda x: 2026 - x, studBirthYear)))

print(studAges)

# stud_ages = [2026 - year for year in studBirthYear]
# print(stud_ages)

stud_ages=list(map(lambda x:2026-x,studBirthYear))
print(stud_ages)