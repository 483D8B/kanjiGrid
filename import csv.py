import csv

def extract_kanji_and_story(csv_file):
    data = {}
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            kanji = row['kanji']
            story = row['story']
            data[kanji] = story
    return data

def extract_kanji_and_keyword(csv_file):
    data = {}
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            kanji = row['kanji']
            keyword = row['keyword']
            data[kanji] = keyword
    return data

def save_to_js(data, js_file):
    with open(js_file, 'w', encoding='utf-8') as file:  # Specify UTF-8 encoding explicitly
        file.write("const stories = ")
        file.write(str(data))  # Writing the dictionary directly to the file
        file.write(";")

def save_to_js_quiz(data, js_file):
    with open(js_file, 'w', encoding='utf-8') as file:  # Specify UTF-8 encoding explicitly
        file.write("const quiz = ")
        file.write(str(data))  # Writing the dictionary directly to the file
        file.write(";")

# Example usage:
csv_file = 'my_stories.csv'  # Assuming your CSV file is named 'my_stories.csv' and is in the same directory as your script
js_file = 'stories.js'  # The JavaScript file where you want to save the data
quiz = 'quiz.js'
result = extract_kanji_and_story(csv_file)
save_to_js(result, js_file)

res = extract_kanji_and_keyword(csv_file)
save_to_js_quiz(res, quiz)




