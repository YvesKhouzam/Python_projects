import json

with open('questions_answers.json', 'w') as file:
    json.dump(
        [
            {
                "question": "Quel est ton prénom?",
                "answer": "Yves"
            },
            {
                "question": "Une figure à trois côtés s\'appelle: ",
                "answer": "Triangle"
            },
            {
                "question": "Une figure à six côtés s\'appelle:",
                "answer": "Hexagone"
            },
            {
                "question": "Les figures à quatre côtés s\'appelle:\n a) Triangles\n b) Heptagones\n "
                            "c) Quadrilatères\n d) Hendécagones\n",
                "answer": "c"
            },
            {
                "question": "Une figure à cinq côtés s\'appelle: ",
                "answer": "Pentagone"
            },
            {
                "question": "Une figure à huit côtés s\'appelle: ",
                "answer": "Octogone"
            },
            {
                "question": "Vrai ou faux? \n Un énnéagone est une figure géométrique à 11 côtés?",
                "answer": "Faux"
            }

        ]
        , file, sort_keys=False, indent=4)


with open('questions_answers.json', 'r') as file:
    user_data = json.load(file)
    print(user_data)

'''
def read_json(path, key):
    values = []
    with open(path, 'r') as file2:
        data = json.load(file2)
        for i in data:
            values.append(i[key])
        return values


print(read_json("questions_answers.json", "question"))

'''
