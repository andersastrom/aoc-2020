import numpy as np


class Day16_2:
    input = """"""

    def __init__(self):
        fields = self.input.split('\n\n')[0].split('\n')

        valid_ranges = set()
        field_ranges = {}
        for index, field in enumerate(fields):
            rang = field.split(':')[1].split(' or ')
            ranges = []
            for r in rang:
                start, end = r.split('-')
                ranges.append(range(int(start), int(end) + 1))
                valid_ranges.add(range(int(start), int(end) + 1))
                field_ranges[index] = ranges

        nearby_tickets = self.input.split('\n\n')[2].replace('\n', ',').split(':')[1]
        nearby_tickets_numbers = list(map(int, nearby_tickets[1::].split(',')))
        non_valid_numbers = set()
        for number in nearby_tickets_numbers:
            if True not in [number in range for range in valid_ranges]:
                non_valid_numbers.add(number)

        tickets = self.input.split('\n\n')[2].split(':\n')[1].split('\n')
        nr_position_candidates = {}
        nr_of_valid_tickets = 0
        for ticket in tickets:
            ticket_numbers = list(map(int, ticket.split(',')))
            is_ticket_valid = True not in [nr in non_valid_numbers for nr in ticket_numbers]
            if is_ticket_valid:
                nr_of_valid_tickets += 1
                for nr_index, ticket_number in enumerate(ticket_numbers):
                    for field_index in field_ranges:
                        range_1 = field_ranges[field_index][0]
                        range_2 = field_ranges[field_index][1]
                        if (ticket_number in range_1) or (ticket_number in range_2):
                            if nr_index in nr_position_candidates:
                                nr_position_candidates[nr_index].append(field_index)
                            else:
                                nr_position_candidates[nr_index] = [field_index]

        field_occurrences = {}
        for candidate in nr_position_candidates:
            for field_index in range(len(fields)):
                field_count = nr_position_candidates[candidate].count(field_index)
                if field_count == nr_of_valid_tickets:
                    if field_index in field_occurrences:
                        field_occurrences[field_index].add(candidate)
                    else:
                        field_occurrences[field_index] = {candidate}

        field_indexes = set([i for i in range(len(fields))])
        field_nr_position_map = {}
        while field_indexes:
            for field_index in field_indexes.copy():
                if len(field_occurrences[field_index]) == 1:
                    nr_pos = list(field_occurrences[field_index])[0]
                    field_nr_position_map[field_index] = nr_pos
                    field_indexes.remove(field_index)
                    for field in field_occurrences:
                        try:
                            field_occurrences[field].remove(nr_pos)
                        except Exception:
                            pass

        your_ticket = list(map(int, self.input.split('\n\n')[1].split(':\n')[1].split(',')))
        departures = []
        for field_index in field_nr_position_map:
            if field_index < 6:
                departures.append(your_ticket[field_nr_position_map[field_index]])
        print(np.product(departures))


Day16_2()
