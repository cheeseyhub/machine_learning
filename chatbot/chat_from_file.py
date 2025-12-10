import pandas as pd


def read_qa_dataframe(filepath: str, key_column, value_column, delimiter=","):
    try:
        df = pd.read_csv(filepath, sep=delimiter)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return {}

    df = df.set_index(key_column)

    qa_dict = df[value_column].to_dict()

    return qa_dict


data_dict = read_qa_dataframe(
    "./train.csv", key_column="question", value_column="answer"
)


if data_dict:
    user_input = input("Enter your question: ").lower()

    if user_input in data_dict:
        print(data_dict[user_input])

    else:
        user_words = set(user_input.split())
        best_match_question = None
        max_score = 0

        for question in data_dict.keys():
            question_words = set(question.lower().split())

            shared_words = user_words.intersection(question_words)
            current_score = len(shared_words)

            if current_score > max_score:
                max_score = current_score
                best_match_question = question

        # 3. Print the answer for the single best-scoring question
        if max_score > 0:
            print(data_dict[best_match_question])
        else:
            print("I'm sorry, I don't have a good answer for that.")

else:
    print("Data could not be loaded")
