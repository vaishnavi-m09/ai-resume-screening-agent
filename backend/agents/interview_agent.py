QUESTION_BANK = {

    "python": [
        "Explain decorators.",
        "What is GIL?"
    ],

    "sql": [
        "Difference between JOIN and UNION?"
    ],

    "machine learning": [
        "Explain overfitting."
    ]
}


class InterviewAgent:

    def generate_questions(
        self,
        skills
    ):

        questions = []

        for skill in skills:

            if skill in QUESTION_BANK:
                questions.extend(
                    QUESTION_BANK[skill]
                )

        return list(set(questions))[:10]