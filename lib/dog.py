approved_breeds = [
    "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle",
    "French Bulldog", "Pug", "Pointer"
]

class Dog:
    def __init__(self, name="Doggo", breed="Mutt"):
        self.name = name
        # Only set breed if name was valid (i.e. self._name exists)
        if hasattr(self, '_name'):
            self.breed = breed

    # Name property
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # Breed property
    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
