# MLB Baseball Quiz Game

categories = {
    "MLB History": [
        {
            "question": "What year was the first MLB game played?",
            "options": ["A) 1869", "B) 1876", "C) 1901", "D) 1920"],
            "answer": "B",
            "hint": ["C", "D"]
        },
        {
            "question": "Which team has won the most World Series titles?",
            "options": ["A) Boston Red Sox", "B) New York Yankees", "C) St. Louis Cardinals", "D) Los Angeles Dodgers"],
            "answer": "B",
            "hint": ["A", "D"]
        },
        {
            "question": "What year did Jackie Robinson break the color barrier?",
            "options": ["A) 1942", "B) 1947", "C) 1950", "D) 1955"],
            "answer": "B",
            "hint": ["A", "D"]
        },
        {
            "question": "Which team was originally called the Highlanders?",
            "options": ["A) Boston Red Sox", "B) Chicago Cubs", "C) New York Yankees", "D) Detroit Tigers"],
            "answer": "C",
            "hint": ["B", "D"]
        },
        {
            "question": "In what year was the designated hitter rule adopted by the AL?",
            "options": ["A) 1969", "B) 1973", "C) 1980", "D) 1985"],
            "answer": "B",
            "hint": ["C", "D"]
        }
    ],
    "Player Stats": [
        {
            "question": "Who holds the all-time home run record?",
            "options": ["A) Babe Ruth", "B) Hank Aaron", "C) Barry Bonds", "D) Alex Rodriguez"],
            "answer": "C",
            "hint": ["A", "D"]
        },
        {
            "question": "Which player was nicknamed 'The Kid'?",
            "options": ["A) Mike Trout", "B) Derek Jeter", "C) Ken Griffey Jr.", "D) Manny Ramirez"],
            "answer": "C",
            "hint": ["B", "D"]
        },
        {
            "question": "Who has the most career hits in MLB history?",
            "options": ["A) Ty Cobb", "B) Pete Rose", "C) Hank Aaron", "D) Derek Jeter"],
            "answer": "B",
            "hint": ["C", "D"]
        },
        {
            "question": "Which pitcher has the most career strikeouts?",
            "options": ["A) Roger Clemens", "B) Randy Johnson", "C) Nolan Ryan", "D) Greg Maddux"],
            "answer": "C",
            "hint": ["A", "D"]
        },
        {
            "question": "Who holds the single-season batting average record (.440)?",
            "options": ["A) Ted Williams", "B) Ty Cobb", "C) Hugh Duffy", "D) Rogers Hornsby"],
            "answer": "C",
            "hint": ["A", "D"]
        }
    ],
    "World Series": [
        {
            "question": "How many innings are in a standard MLB game?",
            "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
            "answer": "C",
            "hint": ["A", "B"]
        },
        {
            "question": "Which team broke an 86-year World Series drought in 2004?",
            "options": ["A) Chicago Cubs", "B) Cleveland Indians", "C) Boston Red Sox", "D) Houston Astros"],
            "answer": "C",
            "hint": ["A", "D"]
        },
        {
            "question": "Which team won the 2016 World Series after a 108-year wait?",
            "options": ["A) Chicago Cubs", "B) Cleveland Indians", "C) Texas Rangers", "D) San Francisco Giants"],
            "answer": "A",
            "hint": ["C", "D"]
        },
        {
            "question": "How many games are in a World Series?",
            "options": ["A) 5", "B) 7", "C) 9", "D) 3"],
            "answer": "B",
            "hint": ["C", "D"]
        },
        {
            "question": "Which team won back-to-back World Series in 1992 and 1993?",
            "options": ["A) Atlanta Braves", "B) Toronto Blue Jays", "C) Minnesota Twins", "D) Oakland Athletics"],
            "answer": "B",
            "hint": ["C", "D"]
        }
    ]
}

# NEW - let the player pick a category
print("Welcome to the MLB Baseball Quiz!")
print("==================================")
print()
print("Choose a category:")
print()

category_names = list(categories.keys())

for i, name in enumerate(category_names):
    print(f"  {i + 1}) {name}")

print()
choice = input("Enter the number of your choice: ").strip()

while not choice.isdigit() or int(choice) < 1 or int(choice) > len(category_names):
    choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

selected_category = category_names[int(choice) - 1]
questions = categories[selected_category]

print()
print(f"You picked: {selected_category}")
print("==================================")
print()

score = 0
hints_left = 3

for i, q in enumerate(questions):
    print(f"Question {i + 1}: {q['question']}")
    for option in q["options"]:
        print(f"  {option}")

    if hints_left > 0:
        print(f"  Type H for a hint ({hints_left} remaining)")

    player_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if player_answer == "H" and hints_left > 0:
        hints_left -= 1
        print("Two wrong answers eliminated:")
        for option in q["options"]:
            if option[0] not in q["hint"]:
                print(f"  {option}")
        player_answer = input("Your answer: ").strip().upper()

    if player_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer was {q['answer']}")

    print()

print("==================================")
print(f"Final Score: {score} out of {len(questions)}")