def generate_questions(text):
    sentences = text.split('.')
    questions = []

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 5:
            questions.append("What is " + sentence + "?")

    return questions


if __name__ == "__main__":
    sample_text = "Natural Language Processing is a field of AI. It helps machines understand human language."
    questions = generate_questions(sample_text)

    for q in questions:
        print(q)
