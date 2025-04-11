import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import json

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")

        # Questions list
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
                "correct_option": 3
            },
            {
                "question": "Who directed the movie 'Inception'?",
                "options": ["Steven Spielberg", "Christopher Nolan", "James Cameron", "Quentin Tarantino"],
                "correct_option": 2
            },
            {
                "question": "Which programming language is known as the language of the web?",
                "options": ["Python", "Java", "C++", "JavaScript"],
                "correct_option": 4
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "correct_option": 3
            },
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
                "correct_option": 1
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["H2O", "O2", "CO2", "NaCl"],
                "correct_option": 1
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "options": ["China", "Japan", "Thailand", "India"],
                "correct_option": 2
            },
            {
                "question": "What is the square root of 64?",
                "options": ["6", "7", "8", "9"],
                "correct_option": 3
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
                "correct_option": 3
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["0", "1", "2", "3"],
                "correct_option": 3
            },
            {
                "question": "Which element has the atomic number 1?",
                "options": ["Oxygen", "Hydrogen", "Carbon", "Helium"],
                "correct_option": 2
            },
            {
                "question": "What is the capital of Australia?",
                "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                "correct_option": 3
            },
            {
                "question": "Who discovered penicillin?",
                "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Gregor Mendel"],
                "correct_option": 2
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "correct_option": 4
            },
            {
                "question": "What is the capital of Italy?",
                "options": ["Rome", "Venice", "Florence", "Milan"],
                "correct_option": 1
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct_option": 2
            },
            {
                "question": "Who wrote '1984'?",
                "options": ["George Orwell", "Aldous Huxley", "J.K. Rowling", "Ernest Hemingway"],
                "correct_option": 1
            },
            {
                "question": "What is the boiling point of water in Celsius?",
                "options": ["90", "100", "110", "120"],
                "correct_option": 2
            },
            {
                "question": "What is the capital of Canada?",
                "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
                "correct_option": 3
            },
            {
                "question": "Who is known as the father of computers?",
                "options": ["Alan Turing", "Charles Babbage", "John von Neumann", "Ada Lovelace"],
                "correct_option": 2
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_option": 2
            },
            {
                "question": "What is the capital of Germany?",
                "options": ["Berlin", "Munich", "Frankfurt", "Hamburg"],
                "correct_option": 1
            },
            {
                "question": "Who developed the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
                "correct_option": 2
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "options": ["Gold", "Iron", "Diamond", "Platinum"],
                "correct_option": 3
            },
            {
                "question": "What is the capital of Spain?",
                "options": ["Barcelona", "Madrid", "Seville", "Valencia"],
                "correct_option": 2
            },
            {
                "question": "What is the speed of light?",
                "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"],
                "correct_option": 1
            },
            {
                "question": "Who wrote 'Pride and Prejudice'?",
                "options": ["Jane Austen", "Charlotte Bronte", "Emily Bronte", "Mary Shelley"],
                "correct_option": 1
            },
            {
                "question": "What is the capital of the United States?",
                "options": ["New York", "Los Angeles", "Washington, D.C.", "Chicago"],
                "correct_option": 3
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Fe", "Pb"],
                "correct_option": 1
            },
            {
                "question": "Who painted 'Starry Night'?",
                "options": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci"],
                "correct_option": 1
            },
            {
                "question": "What is the capital of Japan?",
                "options": ["Tokyo", "Osaka", "Kyoto", "Nagoya"],
                "correct_option": 1
            },
            {
                "question": "What is the largest desert in the world?",
                "options": ["Sahara", "Gobi", "Arctic", "Antarctic"],
                "correct_option": 4
            },
            {
                "question": "Who invented the telephone?",
                "options": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"],
                "correct_option": 1
            },
            {
                "question": "What is the capital of Russia?",
                "options": ["Moscow", "Saint Petersburg", "Kazan", "Novosibirsk"],
                "correct_option": 1
            },
            {
                "question": "What is the smallest country in the world?",
                "options": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"],
                "correct_option": 3
            },
            {
                "question": "Who wrote 'The Great Gatsby'?",
                "options": ["F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain", "John Steinbeck"],
                "correct_option": 1
            },
            {
                "question": "What is the capital of India?",
                "options": ["Mumbai", "Delhi", "Bangalore", "Chennai"],
                "correct_option": 2
            },
            {
                "question": "What is the chemical symbol for sodium?",
                "options": ["Na", "S", "N", "Sa"],
                "correct_option": 1
            },
            {
                "question": "Who discovered gravity?",
                "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
                "correct_option": 2
            },
            {
                "question": "What is the capital of Brazil?",
                "options": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"],
                "correct_option": 3
            },
            {
                "question": "What is the largest continent?",
                "options": ["Africa", "Asia", "Europe", "North America"],
                "correct_option": 2
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Leo Tolstoy"],
                "correct_option": 1
            },
            {
                "question": "What is the capital of South Korea?",
                "options": ["Seoul", "Busan", "Incheon", "Daegu"],
                "correct_option": 1
            },
            {
                "question": "What is the chemical symbol for oxygen?",
                "options": ["O", "Ox", "O2", "O3"],
                "correct_option": 1
            },
            {
                "question": "Who painted 'The Last Supper'?",
                "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
                "correct_option": 1
            },
            {
                "question": "What is the capital of Egypt?",
                "options": ["Cairo", "Alexandria", "Giza", "Luxor"],
                "correct_option": 1
            },
            {
                "question": "What is the tallest mountain in the world?",
                "options": ["K2", "Mount Everest", "Kangchenjunga", "Lhotse"],
                "correct_option": 2
            },
            {
                "question": "Who wrote 'Moby Dick'?",
                "options": ["Herman Melville", "Mark Twain", "Nathaniel Hawthorne", "Edgar Allan Poe"],
                "correct_option": 1
            },
        ]

        self.score = 0
        self.total_score = 0
        self.round_index = 0
        self.question_index = 0
        self.shuffled_questions = []
        self.rounds = []
        self.time_left = 30  # Timer: 30 seconds per question
        self.timer_running = False

        # Styling
        self.bg_color = "#f0f4f8"  # Light blue-gray background
        self.button_color = "#4CAF50"  # Green buttons
        self.text_color = "#333333"  # Dark text
        self.font = ("Helvetica", 12)
        self.root.configure(bg=self.bg_color)

        # Background image
        try:
            img = Image.open("background.jpg")  # Replace with your image
            img = img.resize((600, 400), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(img)
            self.bg_label = tk.Label(root, image=self.bg_image)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            print("Background image not found. Using plain background.")
            self.bg_label = tk.Label(root, bg=self.bg_color)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # UI elements
        self.score_label = tk.Label(root, text=f"Score: {self.score} | Total: {self.total_score}", font=("Helvetica", 14), bg=self.bg_color, fg=self.text_color)
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(root, text=f"Time: {self.time_left}s", font=("Helvetica", 12), bg=self.bg_color, fg=self.text_color)
        self.timer_label.pack()

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=500, bg=self.bg_color, fg=self.text_color)
        self.question_label.pack(pady=20)

        self.selected_answer = tk.IntVar(value=0)
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.selected_answer, value=i+1, font=self.font, bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color)
            rb.pack(anchor="w", padx=50)
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=self.font, bg=self.button_color, fg="white")
        self.submit_button.pack(pady=5)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=self.font, bg=self.button_color, fg="white", state="disabled")
        self.next_button.pack(pady=5)

        self.high_score_button = tk.Button(root, text="View High Scores", command=self.show_high_scores, font=self.font, bg=self.button_color, fg="white")
        self.high_score_button.pack(pady=5)

        # Start the quiz
        self.start_quiz()

    def split_questions(self, questions, chunk_size=20):
        for i in range(0, len(questions), chunk_size):
            yield questions[i:i + chunk_size]

    def start_quiz(self):
        self.score = 0
        self.total_score = 0
        self.round_index = 0
        self.question_index = 0
        self.score_label.config(text=f"Score: {self.score} | Total: {self.total_score}")
        self.shuffled_questions = self.questions.copy()
        random.shuffle(self.shuffled_questions)
        self.rounds = list(self.split_questions(self.shuffled_questions))
        self.load_round()

    def load_round(self):
        if self.round_index < len(self.rounds):
            self.current_round = self.rounds[self.round_index]
            self.question_index = 0
            self.score = 0
            self.score_label.config(text=f"Score: {self.score} | Total: {self.total_score}")
            self.load_question()
        else:
            self.end_game()

    def load_question(self):
        if self.question_index < len(self.current_round):
            q = self.current_round[self.question_index]
            self.question_label.config(text=f"Round {self.round_index + 1} - Question {self.question_index + 1}: {q['question']}")
            for i, option in enumerate(q["options"]):
                self.radio_buttons[i].config(text=f"{i+1}. {option}")
            self.selected_answer.set(0)
            self.submit_button.config(state="normal")
            self.next_button.config(state="disabled")
            self.start_timer()
        else:
            self.end_round()

    def start_timer(self):
        self.time_left = 30
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.timer_label.config(text=f"Time: {self.time_left}s")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left <= 0:
            self.timer_running = False
            self.timer_label.config(text="Time: 0s")
            messagebox.showerror("Time's Up", "Time's up! Moving to next question.")
            self.check_answer(auto_wrong=True)

    def check_answer(self, auto_wrong=False):
        self.timer_running = False
        if not auto_wrong and self.selected_answer.get() == 0:
            messagebox.showwarning("Warning", "Please select an answer!")
            self.start_timer()
            return
        q = self.current_round[self.question_index]
        if auto_wrong or self.selected_answer.get() != q["correct_option"]:
            correct_answer = q["options"][q["correct_option"] - 1]
            messagebox.showerror("Result", f"Wrong! The correct answer was: {correct_answer}")
        else:
            self.score += 1
            self.total_score += 1
            messagebox.showinfo("Result", "Correct!")
        self.score_label.config(text=f"Score: {self.score} | Total: {self.total_score}")
        self.submit_button.config(state="disabled")
        self.next_button.config(state="normal")

    def next_question(self):
        self.question_index += 1
        self.load_question()

    def end_round(self):
        messagebox.showinfo("Round Over", f"Round {self.round_index + 1} Score: {self.score}/{len(self.current_round)}")
        self.round_index += 1
        if self.round_index < len(self.rounds):
            response = messagebox.askyesno("Next Round", "Do you want to continue to the next round?")
            if response:
                self.load_round()
            else:
                self.end_game()
        else:
            self.end_game()

    def end_game(self):
        self.timer_running = False
        messagebox.showinfo("Game Over", f"Final Score: {self.total_score}/{len(self.questions)}")
        self.save_high_score()
        response = messagebox.askyesno("Play Again", "Do you want to play again?")
        if response:
            self.start_quiz()
        else:
            self.root.quit()

    def save_high_score(self):
        name = tk.simpledialog.askstring("High Score", "Enter your name:", parent=self.root)
        if not name:
            name = "Anonymous"
        score_entry = {"name": name, "score": self.total_score}
        high_scores = []
        try:
            if os.path.exists("high_scores.txt"):
                with open("high_scores.txt", "r") as f:
                    high_scores = json.load(f)
        except:
            pass
        high_scores.append(score_entry)
        high_scores = sorted(high_scores, key=lambda x: x["score"], reverse=True)[:5]  # Keep top 5
        with open("high_scores.txt", "w") as f:
            json.dump(high_scores, f, indent=4)

    def show_high_scores(self):
        high_scores = []
        try:
            if os.path.exists("high_scores.txt"):
                with open("high_scores.txt", "r") as f:
                    high_scores = json.load(f)
        except:
            high_scores = []
        if not high_scores:
            messagebox.showinfo("High Scores", "No high scores yet!")
            return
        score_text = "High Scores:\n" + "\n".join(f"{i+1}. {entry['name']}: {entry['score']}" for i, entry in enumerate(high_scores))
        messagebox.showinfo("High Scores", score_text)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = QuizGame(root)
        root.mainloop()
    except Exception as e:
        print(f"Failed to start application: {e}")