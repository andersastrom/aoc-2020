class Day16_1:
    input = """"""

    def __init__(self):
        fields, your, nearby = self.input.split('\n\n')

        valid_ranges = set()
        for field in fields.split('\n'):
            ranges = field.split(':')[1].split(' or ')
            for ran in ranges:
                start, end = ran.split('-')
                valid_ranges.add(range(int(start), int(end) + 1))

        nearby_tickets = self.input.split('\n\n')[2].replace('\n', ',').split(':')[1]
        nearby_tickets = list(map(int, nearby_tickets[1::].split(',')))
        non_valid_numbers = []
        for nr in nearby_tickets:
            if True not in [nr in valid_range for valid_range in valid_ranges]:
                non_valid_numbers.append(nr)
        print(sum(non_valid_numbers))


Day16_1()
