def compute_mongo_age(birthYear, birthMonth, birthDay, currentYear, currentMonth, currentDay):
    ageInYears = (currentYear-birthYear) + (currentMonth-birthMonth)/15 + (currentDay-birthDay)/(15*26)
    return ageInYears

print(compute_mongo_age(2879,8,11,2892,2,21))
