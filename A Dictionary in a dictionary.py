users = {
    "Arsalan":{
    "first":"Arsalan Sabir",
    "last" : "Abbasi",
    "location":"Karachi",
    },
    "Arbaz":{
    "first":"Arbaz Sabir",
    "last" : "Abbasi",
    "location":"Karachi",
    }
}

for username,user_info in users.items():
    print ("\n Username:" + username)
    full_Name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print ("\tFullname:" + full_Name.title())
    print("\tLocation:"+location.title())
