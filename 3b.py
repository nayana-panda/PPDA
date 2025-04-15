def input_dictionary(num):
    print(f"\nEnter key-value pairs for Dictionary {num}.")
    print("Type 'done' as the key to finish input.")

    dictionary = {}
    while True:
        key = input("Enter key: ")
        if key.lower() == 'done':
            break
        value = input("Enter value: ")
        dictionary[key] = value
    return dictionary

def merge_dictionaries(dict1, dict2):
    # Merge dict2 into dict1. dict2's values will overwrite if keys collide.
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def main():
    print("=== Merge Two Dictionaries ===")
    dict1 = input_dictionary(1)
    dict2 = input_dictionary(2)

    print("\nDictionary 1:", dict1)
    print("Dictionary 2:", dict2)

    merged_dict = merge_dictionaries(dict1, dict2)
    print("\nMerged Dictionary:", merged_dict)

if __name__ == "__main__":
    main()

