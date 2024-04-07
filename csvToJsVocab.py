import csv
import json

# Initialize an empty dictionary
vocabulary = {}

# Open the CSV file
with open('final.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row

    for row in reader:
        # Use the vocab as the key
        key = row[1]

        # Create a new dictionary for the word
        word_dict = {
            'meaning': row[2],
            'pronounce': row[3]
        }

        # If the key is not in the dictionary, add it
        if key not in vocabulary:
            vocabulary[key] = []

        # Append the word dictionary to the list of words for this key
        vocabulary[key].append(word_dict)

# Convert the Python dictionary to a JSON string
json_str = json.dumps(vocabulary, ensure_ascii=False)

# Write the JSON string to a JavaScript file
with open('voc.js', 'w', encoding='utf8') as f:
    f.write('let vocabulary = ' + json_str + ';')
