class AIAssistant:

    def __init__(self, name):
        self.name = name

    def answer(self, question):

        question = question.lower()

        if "magacaagu" in question:
            return "Magacaygu waa " + self.name

        elif "salaan" in question or "asc" in question:
            return "Waad salaaman tahay! 👋"

        elif "sidee tahay" in question:
            return "Waan fiicanahay! Adiguna?"

        elif "yaa ku sameeyay" in question:
            return "Hassan ayaa i sameynaya! 🤖"

        elif "jooji" in question or "exit" in question:
            return "Nabad gelyo! 👋"

        else:
            return "Su'aashaas weli ma fahmin."


assistant = AIAssistant("Hassan AI Assistant")

print("🤖 Hassan AI Assistant")
print("Qor 'jooji' si aad uga baxdo.")

while True:

    question = input("Adiga: ")

    answer = assistant.answer(question)

    print("Assistant:", answer)

    if "jooji" in question.lower() or "exit" in question.lower():
        break
