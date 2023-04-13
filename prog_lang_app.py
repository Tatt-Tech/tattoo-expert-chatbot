from tattoo_expert_bot import answer_question

def main():
    question = "Translate the following English text to French: 'Hello, how are you doing?'"
    response = answer_question(question)
    print(response)

if __name__ == "__main__":
    main()
