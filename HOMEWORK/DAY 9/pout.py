numbers = [1, 2, 3]
letters = ["a", "b", "c"]
zipped = zip(numbers, letters)
  # Holds an iterator object


type(zipped)

zipped_dict = dict(zipped)
print(list(zipped))
print(zipped_dict)