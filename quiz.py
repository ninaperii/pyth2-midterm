from random import shuffle

def main_menu():
   ## Displays the main menu. Different inputs open different menus.

   print()
   print(r"""################################""")
   print(r"""#                              #""")
   print(r"""#            WELCOME           #""")
   print(r"""#                              #""")
   print(r"""#     1 - Start quiz           #""")
   print(r"""#     2 - View leaderboard     #""")
   print(r"""#     Q - Exit                 #""")
   print(r"""#                              #""")
   print(r"""#                              #""")
   print(r"""################################""")
   print()

   while True:
      n = input("Enter: ").strip().lower()

      if n == "1":
         quiz_questions()
      elif n == "2":
         view_scores()
      elif n == "q":
         leaving()
      else:
         print("\nInvalid input!\n")


def quiz_questions():
   ## Asks for the name. Prints questions one by one and takes the answers. Keeps track of the score. 
   ## For now it's also where all of the questions data is stored
   ## After finishing it sends name and score to another function

   questions = [
    {
        "question": "What is the output of print(2 + 3 * 4)?",
        "options": ("14", "20", "12", "24"),
        "correct_answer": "14"
    },
    {
        "question": "Which of the following is the correct way to declare a variable in Python?",
        "options": ("int x = 5", "x = 5", "var x = 5", "5 = x"),
        "correct_answer": "x = 5"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ("int", "str", "bool", "character"),
        "correct_answer": "character"
    },
    {
        "question": "What will be the output of the following code?\nx = [1, 2, 3]\ny = x\nx.append(4)\nprint(y)\n",
        "options": ("[1, 2, 3]", "[1, 2, 3, 4]", "Error", "[4, 1, 2, 3]"),
        "correct_answer": "[1, 2, 3, 4]"
    },
    {
        "question": "How do you create a function in Python?",
        "options": ("function myFunc():", "def myFunc():", "func myFunc():", "create myFunc():"),
        "correct_answer": "def myFunc():"
    },
    {
        "question": "Which keyword is used to define a class in Python?",
        "options": ("class", "def", "function", "object"),
        "correct_answer": "class"
    },
    {
        "question": "Which of the following is the correct way to write a comment in Python?",
        "options": ("// This is a comment", "# This is a comment", "/* This is a comment */", "<!-- This is a comment -->"),
        "correct_answer": "# This is a comment"
    },
    {
        "question": "What is the purpose of the 'self' keyword in Python classes?",
        "options": ("To refer to the instance of the class", "To refer to a function", "To define a variable", "To define a method"),
        "correct_answer": "To refer to the instance of the class"
    },
    {
        "question": "What does the range function do in Python?",
        "options": ("Generates a list", "Generates a tuple", "Generates a sequence of numbers", "Generates an error"),
        "correct_answer": "Generates a sequence of numbers"
    },
    {
        "question": "Which of the following statements is used to exit a loop in Python?",
        "options": ("exit", "break", "return", "stop"),
        "correct_answer": "break"
    }
]
   
   while True:
      name = input("\nEnter your name: ")

      if name != "":
         name = name.replace(" ", "_")
         break
      else:
         print("\nInvalid input!")

   score = 0
   shuffle(questions)
   answer_options = ["A", "B", "C", "D"]
   
   for question in questions:
      print()
      print(question["question"])

      i = 0

      for option in question["options"]:
         print(f"{answer_options[i]}) {option}")
         i += 1


      while True:
         answer = input("\nEnter answer (A, B, C, D): ").strip().upper()

         if answer in answer_options:
            selected_option = question["options"][answer_options.index(answer)] 
            break
         else:
            print("\nInvalid input!")

      if selected_option == question["correct_answer"]:
         score += 10

   end_quiz(name, score)


def end_quiz(name, score):
   ## Tells the final score and stores name and score data in a different file.

   with open("scores.txt", "a") as f:
      f.write(f"{name} {score}\n")

   print()
   print(r"""################################""")
   print(f" Thank you for playing, {name}!")
   print(f" Final score: {score}")
   print(" Your score has been saved")
   print("")
   print(" 1 - Back to main menu")
   print(" 2 - View leaderboard")
   print(" Q - Exit")
   print(r"""################################""")
   print()

   while True:
      n = input("Enter: ").strip().lower()

      if n == "1":
         main_menu()
      elif n == "2":
         view_scores()
      elif n == "q":
         leaving()
      else:
         print("\nInvalid input!\n")


def view_scores():
   ## Shows top 10 scores from the file. If there are none, it says so.

   try:
      scores = []

      with open("scores.txt", "r") as f:
         for line in f:
            parts = line.strip().split(" ")

            name = parts[0]
            score = int(parts[1])
            scores.append({"name" : name, "score" : score})

      print()
      print(r"""################################""")
      print("-------------Top 10-------------")

      if not scores:
         print(" No score records...")
         
      
      for i in range(0, len(scores) - 1):
         for j in range(i + 1, len(scores)):
            if scores[i]["score"] < scores[j]["score"]:
               scores[i], scores[j] = scores[j], scores[i]

      place = 1

      for score in scores:
         print(f" {place}. {score['name']} - {score['score']}")
         
         place += 1

      print(r"""################################""")
      print()
      print(r"""################################""")
      print(r"""#                              #""")
      print(r"""#                              #""")      
      print(r"""#                              #""")
      print(r"""#     1 - Back to main menu    #""")
      print(r"""#     Q - Exit                 #""")      
      print(r"""#                              #""")
      print(r"""#                              #""")
      print(r"""#                              #""")
      print(r"""################################""")
      print()

      while True:
         n = input("Enter: ").strip().lower()

         if n == "1":
            main_menu()
         elif n == "q":
            leaving() 
         else:
            print("\nInvalid input!\n")

   except FileNotFoundError:
         print("Scores file not found.")
   except Exception as e:
         print(f"An error occurred: {e}")


def leaving():
   ## End screen

   print()
   print(r"""################################""")
   print(r"""#                              #""")
   print(r"""#                              #""")
   print(r"""#                              #""")
   print(r"""#           GOODBYE!           #""")
   print(r"""#                              #""")
   print(r"""#                              #""")
   print(r"""#                              #""")
   print(r"""#                              #""")
   print(r"""################################""")
   print()  

   exit()

