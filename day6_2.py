from collections import Counter


class Day6_2:
    input = """"""

    def __init__(self):
        groups = self.input.split('\n\n')
        questions_answered = 0
        for group in groups:
            nr_of_people = len(group.split())
            counter = Counter(group.replace('\n', ''))

            questions_answered += sum(occurrences == nr_of_people for _, occurrences in counter.items())
        print(questions_answered)


Day6_2()
