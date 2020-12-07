class Day7_1:
    input = """"""

    rules = input.split('\n')

    def __init__(self):
        total_candidates = set()
        candidates = list(self.get_new_candidates({"shiny gold"}))
        [total_candidates.add(new) for new in candidates]
        while True:
            new_candidates = self.get_new_candidates(candidates)
            if not new_candidates:
                break
            [total_candidates.add(new) for new in new_candidates]
            candidates = new_candidates
        print(len(total_candidates))

    def get_new_candidates(self, candidates):
        new_candidates = set()
        for candidate in candidates:
            for rule in self.rules:
                new_candidate, content = rule.split('contain')
                if candidate in content:
                    new_candidates.add(new_candidate.split(' bag')[0])
        return new_candidates


Day7_1()
