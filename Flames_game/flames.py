class Flames:
    @classmethod
    def find_common_letter_count(cls, name1, name2):
        map = {}
        total_count = len(name1) + len(name2)
        count = 0
        for c in name1:
            map[c] = map.get(c, 0) + 1

        for c in name2:
            if map.get(c):
                count += 1
                map[c] -= 1
        print("total_count ==> ", total_count)
        print("common-letter count ==> ", count, count * 2)

        return total_count - (count * 2)

    @classmethod
    def get_relationship(cls, count):
        ls = ["F", "L", "A", "M", "E", "S"]
        current_index = 0

        while len(ls) != 1:
            print("\nls ==> ", ls)
            print("count ==> ", count)
            print("curt_index ==> ", current_index)
            for _ in range(0, count - 1):
                current_index = (current_index + 1) % len(ls)
                print("next_index ==> ", current_index)
            print("poped-index", current_index)
            ls.pop(current_index)
            print("ls ==> ", ls)

        return ls


if __name__ == "__main__":
    name1 = "Boomibalagan"
    name2 = "varshini"

    remaining_count = Flames.find_common_letter_count(name1, name2)
    print("remaining-count ", remaining_count)

    relationship = Flames.get_relationship(remaining_count)
    print(relationship)
