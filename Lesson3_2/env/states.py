import json


# with open('underground.json', 'r') as p:
#     stations_input = p.read()
#     stations_data = list(json.loads(stations_input))
#
# for station in stations_data:
#     if len(station['RepairOfEscalators']) != 0:
#         print(station['Name'])


# print(stations_data[13])

# with open('./policy_new.json', 'w') as p:
#      new_text = 'Новое имя'
#      policy['SubjectName'] = new_text
#      policy_to_output = json.dumps(policy, ensure_ascii=False)
#      print(policy_to_output)
#      p.write(str(policy_to_output))

streets = {}
streets_sorted = []
max_state_count = []


def swap(t):
    return

with open('./streets.json', 'r') as p:
    state_input = p.read()
    states = json.loads(state_input)

for state in states:
    street = state['Street']
    state_count = int(streets.get(street, 0))
    streets[street] = state_count + 1
    if (len(max_state_count) > 1 and state_count + 1 > max_state_count[1]) or len(max_state_count) == 0:
        max_state_count = [street, state_count + 1]


print(max_state_count)

# sorted(streets, key=streets.values())
# streets_sorted = [(c, s) for c, s in streets.items()]
# print(sorted(streets_sorted, key=lambda street: street[1], reverse=True))
