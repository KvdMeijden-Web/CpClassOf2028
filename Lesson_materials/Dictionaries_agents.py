# import json

# agents = {  "name":"Banana",
#             "country": "Belgium",
#             "level": 9,
#             "skills": ["being yellow","bend","sweet"]
#                 }

# # print(agents)
# #print(agents["country"])
# #print(agents["skills"])
# agents["diet"] = "vegitarian"
# print(agents["diet"])
# agents["Country"] = "Netherlands"


agents = [
    {
        "name": "Shadow",
        "country": "Netherlands",
        "level": 4,
        "skills": ["hacking", "disguise"]
    },

    {
        "name": "Falcon",
        "country": "Japan",
        "level": 5,
        "skills": ["driving", "surveillance"]
    },

    {
        "name": "Ghost",
        "country": "Brazil",
        "level": 3,
        "skills": ["languages", "infiltration"]
    }
]

search = input("what name do you search?")

for agent in agents:
    if agent["name"]== search:
        print (agent)
        break
    print("Not found")

# def open():
#     with open("agent.json", "r") as file:
#         agent = json.load(file)
#     return agent
    
# def close():
#     with open("Agents.json", "w") as file:
#         json.dump(agents, file, indent=4)

# agent_list = open()

