def input_dictionary(num):
    print(f"\nEnter key-value pairs for Dictionary {num}.")
    print("Type 'done' as the key to finish input.")

    dictionary = {}
    while True:
        key = input("Enter key: ")
        if key.lower() == 'done':
            break
        value = input("Enter numeric value: ")
        try:
            dictionary[key] = float(value)  # Convert to float for generality
        except ValueError:
            print("Please enter a valid number.")
    return dictionary

def merge_dictionaries_add_values(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Add values if key overlaps
        else:
            merged[key] = value
    return merged

def main():
    print("=== Merge Two Dictionaries (Add values for overlapping keys) ===")
    dict1 = input_dictionary(1)
    dict2 = input_dictionary(2)

    print("\nDictionary 1:", dict1)
    print("Dictionary 2:", dict2)

    merged_dict = merge_dictionaries_add_values(dict1, dict2)
    print("\nMerged Dictionary (with added values):", merged_dict)

if __name__ == "__main__":
    main()

