import matplotlib.pyplot as plt

def sequence_iterator(data_file):

    with open(data_file, "r") as file:
        file = file.read()
    
    file = file.lower().strip().split(">seq")
    file = [x for x in file if x]

    index_counter = 0

    for x in range(len(file)):

        empty_dictionary = {"a" : 0, "t" : 0, "c" : 0, "g" : 0}
        sequence = file[index_counter]

        for x in sequence:
            if x == "a":
                empty_dictionary["a"] += 1
            elif x == "t":
                empty_dictionary["t"] += 1
            elif x == "c":
                empty_dictionary["c"] += 1
            elif x == "g":
                empty_dictionary["g"] += 1
            else:
                continue

        letters = list(empty_dictionary.keys())
        frequency = list(empty_dictionary.values())
        plt.bar(range(len(empty_dictionary)), frequency, tick_label=letters)
        plt.title(f"Sequence: {index_counter + 1}")
        plt.xlabel("Nucleobases")
        plt.ylabel("Occurences")
        plt.show()
        index_counter = index_counter + 1


sequence_iterator(r"C:\Users\kalle\Documents\Github\lab_1_karl_rydberg_de25\data\dna_raw_complicated.txt")