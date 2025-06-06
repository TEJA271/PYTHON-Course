# 12.Find the number of leap years between two years

start_year = 2000
end_year = 2025

leap_years = []

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years.append(year)

print("Leap years between", start_year, "and", end_year, "are:")
print(leap_years)
print("Total number of leap years:", len(leap_years))
