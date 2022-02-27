"""Working with dictionaries."""

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

#  print(schools["UNCC"])

# example looping over the keys of a dict

for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")