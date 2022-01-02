import csv
def write_csv_file(data, path, mode):
    with open(path, mode, encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
