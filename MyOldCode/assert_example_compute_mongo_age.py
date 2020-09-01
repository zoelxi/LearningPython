def compute_mongo_age(birthYear, birthMonth, birthDay, currentYear, currentMonth, currentDay):
    assert 0 <= birthMonth & birthMonth < 15, 'birthMonth: illegal argument'
    ageInYears = (currentYear-birthYear) + (currentMonth-birthMonth)/15 + (currentDay-birthDay)/(15*26) # computes the age of the Mongo resident in years
    return ageInYears

print(compute_mongo_age(2879, 16, 11, 2892, 2, 21))
