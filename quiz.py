# MLB Baseball Quiz Game

questions = [
    {
        "question": "Which team has won the most World Series titles?",
        "options": ["A) Boston Red Sox", "B) New York Yankees", "C) St. Louis Cardinals", "D) Los Angeles Dodgers"],
        "answer": "B",
        "hint": ["A", "D"]  # NEW - wrong answers to eliminate
    },
    {
        "question": "Who holds the all-time home run record?",
        "options": ["A) Babe Ruth", "B) Hank Aaron", "C) Barry Bonds", "D) Alex Rodriguez"],
        "answer": "C",
        "hint": ["A", "D"]
    },
    {
        "question": "How many innings are in a standard MLB game?",
        "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
        "answer": "C",
        "hint": ["A", "B"]
    },
    {
        "question": "Which player was nicknamed 'The Kid'?",
        "options": ["A) Mike Trout", "B) Derek Jeter", "C) Ken Griffey Jr.", "D) Manny Ramirez"],
        "answer": "C",
        "hint": ["B", "D"]
    },
    {
        "question": "What year was the first MLB game played?",
        "options": ["A) 1869", "B) 1876", "C) 1901", "D) 1920"],
        "answer": "B",
        "hint": ["C", "D"]
    }
]

score = 0
hints_left = 3  # NEW - player gets 3 hints total

print("Welcome to the MLB Baseball Quiz!")
print("==================================")
print()

for i, q in enumerate(questions):
    print(f"Question {i + 1}: {q['question']}")
    for option in q["options"]:
        print(f"  {option}")

    # NEW - show hint option if they have hints left
    if hints_left > 0:
        print(f"  Type H for a hint ({hints_left} remaining)")

    player_answer = input("Your answer (A/B/C/D): ").strip().upper()

    # NEW - handle hint request
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
for i, q in enumerate(questions):
    print(f"Question {i + 1}: {q['question']}")
    for option in q["options"]:
        print(f"  {option}")
    
    player_answer = input("Your answer (A/B/C/D): ").strip().upper()
    
    if player_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer was {q['answer']}")
    
    print()

print("==================================")
print(f"Final Score: {score} out of {len(questions)}")