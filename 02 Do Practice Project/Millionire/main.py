questions = [
    ["Who is Him?", "He is him", "I am him", "She is him", "Why is him?", 4],
    ["Where is Chilika?", "Andaman", "Telangana", "Kerala", "Nepal", 2],
    [
        "What is a dog?",
        "A dog is a dog",
        "A dog is a cat",
        "A dog is a bird",
        "A dog is a fish",
        3,
    ],
    ["What is Money?", "It's Honey", "It's Bunny", "It's Chunny", "It's Spacekraft", 1],
    [
        "What is a cat?",
        "A cat is a cat",
        "A cat is a dog",
        "A cat is a bird",
        "A cat is a fish",
        2,
    ],
    ["Where is mars?", "India", "America", "Russia", "Japan", 1],
    ["Where is neptune?", "India", "America", "Russia", "Japan", 1],
]

prizes = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000]
sum = 0

for question in questions:
    i = 0
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    a = int(input("Enter the number: "))

    if question[5] == a:
        print("Correct")
    else:
        print(f"Wrong, the correct answer was {question[5]}")
        print(f"App {sum} mein khus rahe... bye")
        break
    sum += prizes[i]
    print(f"You own {sum} Rupees")

if sum == 7000000:
    print(f"Congratulations, app jitgaye... 7 Lakh Carod")
