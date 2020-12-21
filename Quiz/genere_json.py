import json

with open('questions_answers.json', 'w') as file:
    json.dump(
        [
            {
                "question": "Prémom",
                "answer": "Yves"
            },
            {
                "question": "Quel est ton nom?",
                "answer": "Khouzam"
            },
            {
                "question": "Ville d'habitation?",
                "answer": "Vaudreuil"
            },
            {
                "question": "Sport préféré?",
                "answer": "Soccer"
            }

        ]
        , file, sort_keys=False, indent=4)

#
with open('questions_answers.json', 'r') as file:
    user_data = json.load(file)
    print(user_data)


def read_json(path, key):
    values = []
    with open(path, 'r') as file2:
        data = json.load(file2)
        for i in data:
            values.append(i[key])
        return values


print(read_json("questions_answers.json", "question"))

