print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]
len(counties)

counties_tuple = ("Arapahoe", "Denver", "Jefferson")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")

counties_dict['Arapahoe'] 

counties_dict.get("Arapahoe")  

print(counties_dict['Arapahoe'])  

print(counties_dict.get("Arapahoe")) 

voting_data = []
voting_data.append({"county":"Arapahoe", "Registered_voters": 422829})
voting_data.append({"county":"Denver", "Registered_voters": 463353})
voting_data.append({"county":"Jefferson", "Registered_voters": 432438})

voting_data.insert(1,({"county":"El Paso", "Registered_voters": 461149}))
voting_data.pop(0)
voting_data[2] = {"county":"Denver", "Registered_voters": 463353}
voting_data[1] = {"county":"Jefferson", "Registered_voters": 432438}
voting_data.insert(3,({"county":"Arapahoe", "Registered_voters": 422829}))
voting_data

#How many votes did you get?
my_votes = int(input("How many votes did you get in the election?"))
#Total Votes in the election
total_votes = int(input("What is the total votes in the election?"))
#Calculate the percentage of votes you received
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes) + "% of the total votes.")

if counties[1] == "Denver":
    print(counties[1])

temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the window")

if "El Paso" in counties:
    print("El Paso is in the list of Counties")
else:
    print("El Paso not in the list of Counties")
counties
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

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

for key, value in counties_dict.items():
    print(key, value)

for county, value in counties_dict.items():
    print(county, value)

for county, value in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
    # print(str(county) + "county has " , str(value) + " registered voters.")

voting_data

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['Registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {str(candidate_votes/total_votes*100)} % of total votes.")
print(message_to_candidate)

