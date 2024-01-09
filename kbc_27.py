import random

class KBCGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"], "answer": "B"},
            {"question": "Which planet is known as the Red Planet?", "options": ["A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"], "answer": "A"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"], "answer": "B"},
            # Add more questions as needed
        ]
        self.score = 0
        self.current_question = 0
        self.lifelines = ["50/50", "Phone a Friend", "Ask the Audience"]

    def display_question(self):
        question_data = self.questions[self.current_question]
        print("\nQuestion {}: {}".format(self.current_question + 1, question_data["question"]))
        for option in question_data["options"]:
            print(option)
        print()

    def ask_question(self):
        user_answer = input("Your answer: ").upper()
        question_data = self.questions[self.current_question]
        correct_answer = question_data["answer"]

        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1000
        else:
            print("Incorrect! The correct answer is '{}'.".format(correct_answer))

    def use_lifeline(self):
        if self.lifelines:
            print("\nAvailable lifelines: {}".format(", ".join(self.lifelines)))
            lifeline_choice = input("Choose a lifeline (type the name): ")
            if lifeline_choice in self.lifelines:
                self.lifelines.remove(lifeline_choice)
                if lifeline_choice == "50/50":
                    self.fifty_fifty()
                elif lifeline_choice == "Phone a Friend":
                    self.phone_a_friend()
                elif lifeline_choice == "Ask the Audience":
                    self.ask_the_audience()
            else:
                print("Invalid lifeline choice. Try again.")
                self.use_lifeline()
        else:
            print("No lifelines left!")

    def fifty_fifty(self):
        question_data = self.questions[self.current_question]
        correct_answer = question_data["answer"]
        incorrect_options = [option for option in question_data["options"] if not option.startswith(correct_answer)]

        options_to_remove = random.sample(incorrect_options, len(incorrect_options) - 1)
        for option in options_to_remove:
            question_data["options"].remove(option)

        print("\n{} options remaining:".format(len(question_data["options"])))
        for option in question_data["options"]:
            print(option)

    def phone_a_friend(self):
        print("\nCalling a friend for help... (ring, ring)")
        print("Friend's suggestion: '{}'".format(random.choice(self.questions[self.current_question]["options"])))

    def ask_the_audience(self):
        print("\nAsking the audience for help...")
        # In a real game, you would implement a more sophisticated audience response simulation.
        print("Audience's choice: '{}'".format(random.choice(self.questions[self.current_question]["options"])))

    def play(self):
        print("Welcome to Kaun Banega Crorepati!\n")
        while self.current_question < len(self.questions):
            self.display_question()
            self.ask_question()
            if self.current_question < len(self.questions) - 1:
                lifeline_option = input("Do you want to use a lifeline? (yes/no): ").lower()
                if lifeline_option == "yes":
                    self.use_lifeline()
            self.current_question += 1

        print("\nCongratulations! You've completed the game.")
        print("Total score: {}".format(self.score))

if __name__ == "__main__":
    game = KBCGame()
    game.play()


