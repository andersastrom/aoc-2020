from collections import Counter


class Day6_1:
    input = """"""

    def __init__(self):
        groups = self.input.split('\n\n')
        questions_answered = 0
        for group in groups:
            counter = Counter(group.replace('\n', ''))
            questions_answered += len(counter)
        print(questions_answered)


Day6_1()
