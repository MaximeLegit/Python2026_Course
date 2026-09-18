speakers = ["Anna", "Max", "Eren", "Lola", "Jean"]
rooms = ["alpha", "beta", "gamma", "delta"]
participants = ["Annie", "Bobby", "Clara", "Damon", "Eren", "Fanny", "Grace", "Holly", "Inde", "Jolene"]
topics = ["Intro", "Applying principles in real life", "Identifying sketchyness", "Data theft prevention", "Advanced"]

sessions = [{"session title":"Privacy", "speaker": speakers[0], "room": rooms[0], "start time":"08.00","duration":50, "topic" : "Intro", "nr_of_participants" : participants[0:8]},
            {"session title":"Cryptography", "speaker": speakers[1], "room": rooms[1], "start time":"09.00","duration":45, "topic" : "elyptic curve", "nr_of_participants" : participants[0:5]},
            {"session title":"Security", "speaker": speakers[2], "room": rooms[2], "start time":"10.00","duration":50, "topic" : "Data theft", "nr_of_participants" : participants[2:6]},
            {"session title":"Obfuscation", "speaker": speakers[3], "room": rooms[3], "start time":"11.00","Yedurationar":45, "topic" : "how to", "nr_of_participants" : participants[4:9]},
            {"session title":"Encryption", "speaker": speakers[4], "room":rooms[0], "start time":"13.00","duration":55, "topic" : "AES256", "nr_of_participants" : participants[0:8]},
            {"session title":"Sniffing", "speaker": speakers[0], "room": rooms[1], "start time":"14.00","duration":50, "topic" : "tools", "nr_of_participants" : participants[1:3]},
            {"session title":"Packet Capture", "speaker": speakers[1], "room": rooms[2], "start time":"15.00","duration":40, "topic" : "tools",  "nr_of_participants" : participants[5:8]},
            {"session title":"User Sessions", "speaker": speakers[2], "room": rooms[3], "start time":"15.45","duration":45, "topic" : "Beginner's guide", "nr_of_participants" : participants[1:4]}]

conference = {"Session" : sessions,  "Speakers" : speakers,  "Rooms:" : rooms, "Participants:" : participants, "Topics:" : topics}
#print(conference)


# Part 2 Working with schedule


#print("First Session:", sessions[0]["session title"], "Speaker of the 3rd session", sessions[2]["speaker"], "Last session Room: ", sessions[-1]["room"])
#print("Information about one selected session: ", sessions[1])
#print(f"First three sessions: \n{sessions[0]} \n{sessions[1]} \n{sessions[2]}")
#print(f"Last two sessions: \n{sessions[-2]} \n{sessions[-1]}")


reversed_schedule = sessions[::-1]
#reversed_schedule = sorted(sessions, key = lambda session : session["start time"], reverse=True)
#print(reversed_schedule)

copied_session = sessions[0:4].copy()
#print("Copied Sessions:\n",copied_session)


# Part 3 Modifications


sessions[0]["room"] = "epsilon"
#print("First Sessions modified room:", sessions[0]["room"])

sessions[1]["speaker"] = "Morgan"
#print("Second Sessions modified speaker:", sessions[1]["speaker"])

new_session = {"session title":"Recap", "speaker": "Devon", "room": "zeta", "start time":"16.00.00","duration":15, "topic" : "Recap", "nr_of_participants" : "3"}
sessions.append(new_session)
#print(sessions)

sessions.pop(2)
#print("Security session should be removed now:\n", sessions)

# As my data structure did not have participants in it, now I am modifying it to add them from my list. 

sessions[0]["participant"] = participants[0]
#print("\n", sessions[0])

sessions[0].pop("participant")
#print("\n", sessions[0])

difficulties = ["Beginner", "Intermediate", "Advanced"]
#print("\nSession 3 untouched:", sessions[2])
sessions[2]["difficulty"] = difficulties[2]

#print("\nSession 3 altered:", sessions[2])


# Part 4 Unique conference information

unique_conference_topics = set(conference["Topics:"])
#print(unique_conference_topics)

unique_technical_skills = conference.get("Unique Skills")
#print("Since unique skills were not present per any teacher nor a requirement, unique skills of teacher are:", unique_technical_skills)
#print("If this had to be done, I would just add a section, then call set(conference[\"Unique Skills\"]) as it would return me a set that I could print")


print("Participants regirestered to both session 1 and 2", set(sessions[0]["nr_of_participants"]) | set(sessions[1]["nr_of_participants"]))

participants_in_both_sessions = set(sessions[0]["nr_of_participants"]) & set(sessions[1]["nr_of_participants"])
if participants_in_both_sessions:
    print("Participants in both session 1 and 2 are: ", participants_in_both_sessions)


print("Participants regirestered to", sessions[0]["session title"], "are", sessions[0]["nr_of_participants"])
print("Whilst participants registere to", sessions[1]["session title"],"are", sessions[1]["nr_of_participants"])


# Part 5 Unique conference information
