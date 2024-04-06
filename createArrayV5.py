import os
import csv
from jsmin import jsmin

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
csv_files = sorted((f for f in os.listdir(csv_dir) if f.endswith('.csv')))

# Initialize a dictionary to store the total FailCount for each FrameNumber
total_failures = {}

# Initialize a dictionary to store the size differences as an object
differences = {}

# Initialize an empty dictionary to store pass rates for each date
pass_rates = {}

# Loop through each sorted CSV file in the directory
for i, csv_file in enumerate(csv_files):
    # Get the file name without the extension
    file_name = os.path.splitext(csv_file)[0]

    # Initialize an empty dictionary to store FrameNumber and LeitnerBox values
    leitner_values = {}

    # Read the CSV file and extract FrameNumber and LeitnerBox values
    with open(os.path.join(csv_dir, csv_file), 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        leitner_values = {int(row['FrameNumber']): int(row['LeitnerBox']) for row in csv_reader}

    # Calculate size differences between CSV files
    differences[i + 1] = len(set(leitner_values.keys()) - set(all_leitner_values.get('koohii_origin', {}).keys())) if i == 0 else len(set(leitner_values.keys()) - set(all_leitner_values.get(os.path.splitext(csv_files[i - 1])[0], {}).keys()))

    # Store the dictionary in the all_leitner_values dictionary
    all_leitner_values[file_name] = leitner_values

# Find the most recent CSV file based on filename date
recent_csv_file = max((os.path.join(csv_dir, f) for f in os.listdir(csv_dir) if f.endswith('.csv')), key=os.path.getctime)

# Read the most recent CSV file and extract FrameNumber and FailCount values
with open(recent_csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    total_failures = {int(row['FrameNumber']): total_failures.get(int(row['FrameNumber']), 0) + int(row['FailCount']) for row in csv_reader}

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

    # Iterate over each CSV file
    for i in range(len(csv_files) - 1):
        current_file = csv_files[i]
        next_file = csv_files[i + 1]
        
        # Extract the date from the current and next file's name
        date = next_file.split('_')[1].split('.')[0]  # Extract the date from the filename
        
        # Open the current and next CSV files
        with open(os.path.join(csv_dir, current_file), 'r', encoding='utf-8') as current_csvfile, \
                open(os.path.join(csv_dir, next_file), 'r', encoding='utf-8') as next_csvfile:
            
            current_reader = csv.DictReader(current_csvfile)
            next_reader = csv.DictReader(next_csvfile)
            
            # Read the headers to get the field names
            current_headers = current_reader.fieldnames
            next_headers = next_reader.fieldnames
            
            # Check if 'FailCount' and 'PassCount' columns exist in the headers
            if 'FailCount' not in current_headers or 'PassCount' not in current_headers or \
                'FailCount' not in next_headers or 'PassCount' not in next_headers:
                print(f"Error: 'FailCount' or 'PassCount' column not found in {current_file} or {next_file}. Skipping.")
                continue
            
            total_cards = 0
            failed_cards = 0
            passed_cards = 0
            
            # Iterate over each row in the current CSV
            for current_row, next_row in zip(current_reader, next_reader):
                total_cards += 1
                fail_count_current = int(current_row['FailCount'])
                pass_count_current = int(current_row['PassCount'])
                fail_count_next = int(next_row['FailCount'])
                pass_count_next = int(next_row['PassCount'])
                
                # Check if FailCount or PassCount has increased
                if fail_count_next > fail_count_current:
                    failed_cards += 1
                if pass_count_next > pass_count_current:
                    passed_cards += 1
            
            
            # Calculate the pass rate percentage
            pass_rate = ((passed_cards-failed_cards) / (passed_cards)) * 100 if (passed_cards + failed_cards) > 0 else 0

            # Store the pass rate for the current date
            pass_rates[date] = pass_rate

    # Write the differences dictionary to the JavaScript file
    js_file.write('const Retention = {\n')
    js_file.write('"2023-09-13": 97.96,\n')  # Add the specific date and value as the first element
    for file_index, pass_rate in pass_rates.items():
        js_file.write(f'  "{file_index}": {pass_rate:.2f},\n')
    js_file.write('};\n')

# After writing to the js_file, close it
js_file.close()

# Open the file again in read mode
with open(output_file, 'r', encoding='utf-8') as js_file:
    js = js_file.read()

# Minify the JavaScript code
minified_js = jsmin(js)

# Write the minified code to a new file
minified_output_file = output_file.replace('.js', '.min.js')
with open(minified_output_file, 'w', encoding='utf-8') as js_file:
    js_file.write(minified_js)

print(f'Saved minified data as JavaScript objects in {minified_output_file}')
