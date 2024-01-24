# Create a function that counts the key-value pair (dictionary)
# and counts a certain value. In this case, count the number of 
# online people.
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(parameter):
    status = 0
    for key in parameter:
        if parameter[key] == "online":
            status+= 1
    return status