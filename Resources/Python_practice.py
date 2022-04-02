counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)

counties_tuple = ("Arapahoe","Denver","Jefferson")
print(counties_tuple)

print(counties_tuple[1])

counties.append("El Paso")
print(counties)

counties.insert(2, "El Paso")
print(counties)

counties.remove("El Paso")
print(counties)

counties.pop(3)
print(counties)

counties[2] = "El Paso"
print(counties)

counties_tuple = ("Arapahoe","Denver","Jefferson")
print(counties_tuple)

len(counties_tuple)

print(counties_tuple[1])


counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
len(counties_dict)
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict['Arapahoe'])

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])


for county in counties_dict:
    print(county)


for county in counties_dict.keys():
    print(county)


for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


for county_dict in voting_data:
    print(county_dict['county'])
                