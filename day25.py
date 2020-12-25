class Day25:

    input = """8184785
5293040"""

    def __init__(self):
        keys = list(map(int, self.input.split()))
        card_pub_key = keys[0]
        door_pub_key = keys[1]

        value = 1
        loop_card = 0
        while value != card_pub_key:
            value = value * 7
            value = value % 20201227
            loop_card += 1

        value = 1
        loop_door = 0
        while value != door_pub_key:
            value = value * 7
            value = value % 20201227
            loop_door += 1

        value = 1
        for i in range(loop_card):
            value = value * door_pub_key
            value = value % 20201227

        encrypt_key = value
        print(encrypt_key)


Day25()
