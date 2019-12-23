ieltsResults1 = {"Listening":9, "Writing":8, "Speaking":6, "Reading":7}
ieltsResults2 = {"Listening":8, "Writing":8, "Speaking":7, "Reading":7}
ieltsResults3 = {"Listening":9, "Writing":8, "Speaking":8, "Reading":7}

ieltsResultsStudents = {"Ali": ieltsResults1, "J": ieltsResults2, "A": ieltsResults3}
# #print(ieltsResults)
# print(ieltsResultsStudents["Ali"]["Speaking"])

for k, v in ieltsResultsStudents.items():
    print("Key is {}. Value is {}".format(k, v))

