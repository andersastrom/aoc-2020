class Day7_2:
    input = """"""

    rules = input.split('\n')
    total_bags = 0

    def __init__(self):
        bag_content = self.get_bag_content("shiny gold")
        self.total_bags += self.sum_nr_of_bags(bag_content, 1)
        self.calculate_nr_of_bags(bag_content, 1)
        print(self.total_bags)

    def get_bag_content(self, color):
        for rule in self.rules:
            bag, content = rule.split('contain ')
            if bag.split(' bag')[0] == color:
                content = content.replace('.', '').split(', ')
                if content == ['no other bags']:
                    return []
                return content

    def calculate_nr_of_bags(self, bag_content, multiplier):
        for bag in bag_content:
            color = bag.split(' bag')[0][2::]
            nr_of_bags = int(bag[0])
            bag_content = self.get_bag_content(color)
            self.total_bags += self.sum_nr_of_bags(bag_content, multiplier * nr_of_bags)
            self.calculate_nr_of_bags(bag_content, multiplier * nr_of_bags)

    def sum_nr_of_bags(self, content, multiplier):
        return sum([int(bags[0]) for bags in content]) * multiplier


Day7_2()
