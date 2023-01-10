def for_loop():
    weekday=["monday","tuesday","wednesday","thursday", "friday"]
    weekend=["saturday","sunday"]
    for day in weekday:
        print(day + " 8:30 , go to school")
    for day in weekend:
        if day == "saturday":
            print(day +" rest and do your homewok")
        else:
            print(day +" it's prayer day go to church")

for_loop()