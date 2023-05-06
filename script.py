import csv
import argparse

parser = argparse.ArgumentParser(description='Process a CSV file.')
parser.add_argument('csv_file_name', type=str, help='Name of the CSV file.')
parser.add_argument('part', type=str, help='Part number or "list" for list mode.')
parser.add_argument('--color_id', type=int, help='Color ID (optional).')
parser.add_argument('--include_spare', action='store_true', help='Include spare parts (optional).')
args = parser.parse_args()

if args.part.lower() == 'list':
    # List mode
    parts = {}
    with open(args.csv_file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not args.include_spare and row['is_spare'].lower() == 'true':
                continue
            key = (row['part_num'], row['color_id'])
            if key not in parts or int(row['quantity']) > int(parts[key]['quantity']):
                parts[key] = row
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in parts.values():
            writer.writerow(row)
else:
    # Part mode
    quantity = 0
    with open(args.csv_file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not args.include_spare and row['is_spare'].lower() == 'true':
                continue
            if int(row['quantity']) > quantity and row['part_num'] == args.part:
                if args.color_id is None or int(row['color_id']) == args.color_id:
                    quantity = int(row['quantity'])
    print(quantity)
