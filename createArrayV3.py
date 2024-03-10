import os
import csv

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the directory where the CSV files are located (same as the script directory)
csv_dir = script_dir

# Define the output JavaScript file path
output_file = os.path.join(script_dir, 'leitner.js')

# Initialize a dictionary to store LeitnerBox values for each file
all_leitner_values = {}

# Add an empty dataset called "koohii_origin" to the dictionary
all_leitner_values['koohii_origin'] = {}

# Sort the list of CSV files based on their names
csv_files = sorted([f for f in os.listdir(csv_dir) if f.endswith('.csv')])

# Initialize a dictionary to store the total FailCount for each FrameNumber
total_failures = {}

# Initialize a dictionary to store the size differences as an object
differences = {}

# Loop through each sorted CSV file in the directory
for i, csv_file in enumerate(csv_files):
    # Get the file name without the extension
    file_name = os.path.splitext(csv_file)[0]

    # Initialize an empty dictionary to store FrameNumber and LeitnerBox values
    leitner_values = {}

    # Read the CSV file and extract FrameNumber and LeitnerBox values
    with open(os.path.join(csv_dir, csv_file), 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            frame_number = int(row['FrameNumber'])
            leitner_box = int(row['LeitnerBox'])
            leitner_values[frame_number] = leitner_box

    # Calculate size differences between CSV files
    if i == 0:
        # Compare "koohii_origin" to the first CSV file
        koohii_origin_frame_numbers = set(all_leitner_values['koohii_origin'].keys())
        new_elements = len(set(leitner_values.keys()) - koohii_origin_frame_numbers)
        differences[i + 1] = new_elements
    else:
        prev_file = csv_files[i - 1]
        prev_file_name = os.path.splitext(prev_file)[0]
        prev_frame_numbers = set(all_leitner_values[prev_file_name].keys())
        new_elements = len(set(leitner_values.keys()) - prev_frame_numbers)
        differences[i + 1] = new_elements

    # Store the dictionary in the all_leitner_values dictionary
    all_leitner_values[file_name] = leitner_values

# Find the most recent CSV file based on filename date
recent_csv_file = max((os.path.join(csv_dir, f) for f in os.listdir(csv_dir) if f.endswith('.csv')), key=os.path.getctime)

# Read the most recent CSV file and extract FrameNumber and FailCount values
with open(recent_csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        frame_number = int(row['FrameNumber'])
        fail_count = int(row['FailCount'])
        # Add the FailCount to the total for the corresponding FrameNumber
        total_failures[frame_number] = total_failures.get(frame_number, 0) + fail_count

# Write all data to the JavaScript file as JSON-like objects
with open(output_file, 'w', encoding='utf-8') as js_file:
    js_file.write('\n')  # Add an empty line
    js_file.write('const leitnerData = {\n')
    for file_name, data in all_leitner_values.items():
        js_file.write(f'  "{file_name}": {data},\n')
    js_file.write('};\n')

    js_file.write('const Failures = {')
    js_file.write(", ".join(f"{frame_number}: {total}" for frame_number, total in total_failures.items()))
    js_file.write('};\n')

    # Write the differences dictionary to the JavaScript file
    js_file.write('const Differences = {')
    js_file.write(", ".join(f'"{file_index}": {diff}' for file_index, diff in differences.items()))
    js_file.write('};\n')

print(f'Saved data as JavaScript objects in {output_file}')