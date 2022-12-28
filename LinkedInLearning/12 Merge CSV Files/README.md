# Python Code Challenge #12: Merge CSV Files

Your goal is to implement a function, `merge_csv()`, that takes two input arguments: a list of file paths to CSV files to merge and an output file path to save the resulting CSV file.

## Example Test Output

Using the two included CSV files with student grades as input:

```console
>>> merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')
```

```py
import csv

def merge_csv(csv_list, output_path):
    # build list with all fieldnames
    fieldnames = []
    for file in csv_list:
        with open(file, 'r', encoding='utf-8') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)

    # write data to output file based on field names
    with open(output_path, 'w', encoding='utf-8', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)


# commands used in solution video for reference
if __name__ == '__main__':
    merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')
```
