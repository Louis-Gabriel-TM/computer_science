"""
SRP = Single Responsibility Principle (1st SOLID principle):

    "A class should have only one reason to be changed / rewritten."

Similar to SOC (Separation of Concerns) principle.
"""


class Diary:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self):
        return "\n".join(self.entries)

    # Breaking the Single Responsibility Principle:
    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

    def load(self, filename):
        pass

    def load_from_web(self, url):
        pass
    # The class has a 1st responsibility to manipulate entries of a diary.
    # It should not have the responsibility of its persistence:
    # save / load / ... methods should be necessary for other classes.
    # Repeating this merhods for each class would not be DRY

    # A class with all relative responsibilities consist of an antipattern
    # The God objects antipattern


# A better idea is to create a dedicated class for persistence:
class PersistenceManager:

    @staticmethod
    def save_to_file(diary, filename):
        with open(filename, 'w') as f:
            f.write(str(diary))


if __name__ == "__main__":
    my_diary = Diary()

    my_diary.add_entry("Today, I learn the Single Responsibility Principle.")
    my_diary.add_entry("And now, the others SOLID principles await!")

    print(f"Diary entries:\n{my_diary}")

    diary_file = "diary.text"
    PersistenceManager.save_to_file(my_diary, diary_file)

    with open(diary_file) as f:
        print(f.read())
