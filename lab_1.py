def nucleobase_count(data_file): 
    """ The purpose of this function is to count the occurences of nucleobases in one or more sequences of DNA. It is intended to 
    take the path of a text file as an argument when called, but the contained data need to be formatted in the same way as the 
    data in the sample files, with each sequence separated by '>seq'. Mandates an install of matplotlib. """

    import matplotlib.pyplot as plt

    index_counter = 0  # Variable used to refer to individual list elements
    
    with open(data_file, "r") as file:
        read_file = file.read() 

    sequence_list = read_file.lower().strip().split(">seq") # Cleans string data and splits each sequence into separate list elements
    sequence_list = [sequence for sequence in sequence_list if sequence] # Removes falsy values, i.e empty list elements
                 
    for iteration in range(len(sequence_list)): # Iterates code block as many times as list contains elements
        empty_dictionary = {"a" : 0, "t" : 0, "c" : 0, "g" : 0}
        sequence = sequence_list[index_counter]
        for nucleobase in sequence: # Iterates through the element which index value equals the value of index_counter
            if nucleobase in empty_dictionary:
                empty_dictionary[nucleobase] += 1
            else:
                continue
        letters = list(empty_dictionary.keys()) # Creates list variable with dictionary keys as elements
        frequency = list(empty_dictionary.values()) # Creates list variable with dictionary values as elements
        plt.figure()
        plt.bar(range(len(empty_dictionary)), # Initiates bar graph using "plt.bar", along with necessary parameters 
                frequency, 
                tick_label=letters) 
        plt.title(f"Sequence: {index_counter + 1}")
        plt.xlabel("Nucleobases")
        plt.ylabel("Occurences")
        plt.savefig(f"sequence_{index_counter + 1}.png")
        plt.show()
        plt.close()
        index_counter = index_counter + 1 # Changes the value of index_counter and thusly the referred sequence

nucleobase_count("dna_raw.txt")