import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Combined dataset of patterns and responsespip
pairs = [
    # General Knowledge Questions
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?", "Nice to meet you %1! How can I assist you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"what is your favorite programming language?",
        ["I love Python! It's versatile and easy to learn.", "Python is my favorite too!"]
    ],
    [
        r"who is the president of the United States?",
        ["As of 2023, Joe Biden is the president.", "The current president is Joe Biden."]
    ],
    [
        r"what is the capital of France?",
        ["The capital of France is Paris.", "Paris is the capital city of France."]
    ],
    [
        r"what is the largest planet in our solar system?",
        ["Jupiter is the largest planet in our solar system.", "The largest planet is Jupiter."]
    ],
    [
        r"who wrote 'Romeo and Juliet'?",
        ["'Romeo and Juliet' was written by William Shakespeare.", "William Shakespeare is the author of 'Romeo and Juliet'."]
    ],

    # Technology and Science Questions
    [
        r"what is artificial intelligence?",
        ["Artificial intelligence is the simulation of human intelligence in machines.", "AI refers to the capability of a machine to imitate intelligent human behavior."]
    ],
    [
        r"what is machine learning?",
        ["Machine learning is a subset of AI that enables systems to learn from data.", "It's a method of data analysis that automates analytical model building."]
    ],
    [
        r"what is the internet of things?",
        ["The Internet of Things (IoT) refers to the interconnected network of devices.", "IoT is a system of interrelated physical devices that can collect and exchange data."]
    ],
    [
        r"what is quantum computing?",
        ["Quantum computing uses quantum bits to perform calculations at unprecedented speeds.", "It's a type of computation that takes advantage of quantum mechanics."]
    ],
    [
        r"what is blockchain?",
        ["Blockchain is a decentralized digital ledger that records transactions across many computers.", "It's a technology that enables secure and transparent record-keeping."]
    ],

    # Health and Wellness Questions
    [
        r"what are the benefits of exercise?",
        ["Exercise improves physical health, boosts mood, and enhances mental well-being.", "Regular exercise can help maintain a healthy weight and reduce the risk of chronic diseases."]
    ],
    [
        r"how much water should I drink daily?",
        ["It's generally recommended to drink at least 8 cups (2 liters) of water a day.", "Staying hydrated is important; aim for about 2 liters of water daily."]
    ],
    [
        r"what is a balanced diet?",
        ["A balanced diet includes a variety of foods from all food groups: fruits, vegetables, proteins, grains, and dairy.", "It means consuming the right proportions of carbohydrates, proteins, and fats."]
    ],
    [
        r"how can I reduce stress?",
        ["Practicing mindfulness, exercising, and maintaining a healthy work-life balance can help reduce stress.", "Consider meditation, deep breathing exercises, and spending time in nature."]
    ],
    [
        r"what are the symptoms of flu?",
        ["Common flu symptoms include fever, cough, sore throat, body aches, and fatigue.", "Flu symptoms often include chills, headaches, and muscle aches."]
    ],

    # Entertainment and Pop Culture Questions
    [
        r"who is your favorite actor?",
        ["I don't watch movies, but I've heard that Leonardo DiCaprio is very talented!", "Many people love Tom Hanks for his versatility."]
    ],
    [
        r"what is the highest-grossing movie of all time?",
        ["As of now, 'Avatar' holds the record for the highest-grossing movie.", "'Avatar' is the highest-grossing film worldwide."]
    ],
    [
        r"who won the Grammy for Album of the Year in 2023?",
        ["The Grammy for Album of the Year in 2023 was awarded to Jon Batiste.", "Jon Batiste won the Grammy for Album of the Year."]
    ],
    [
        r"what is your favorite music genre?",
        ["I don't listen to music, but I've heard that pop and rock are very popular!", "Many people enjoy classical music for its soothing qualities."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you rephrase?", "Could you please clarify?"]
    ]
]


# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Function to send message and get response
def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", tk.END)
    if msg != '':
        ChatLog.config(state=tk.NORMAL)
        ChatLog.insert(tk.END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12))
        res = chatbot.respond(msg)
        ChatLog.insert(tk.END, "Bot: " + res + '\n\n')
        ChatLog.config(state=tk.DISABLED)
        ChatLog.yview(tk.END)

# GUI setup
base = tk.Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=False, height=False)

ChatLog = tk.Text(base, bd=0, bg="white", height="8", width="50", font="Arial")
ChatLog.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = tk.Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=send)

EntryBox = tk.Text(base, bd=0, bg="white", width="29", height="5", font="Arial")

scrollbar.place(x=376, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()