import csv
from datetime import datetime
import os
import argparse
import sys
import argparse
import pdb
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


argparser = argparse.ArgumentParser()
argparser.add_argument('--cutoff', type=float, default=5, help='The cutoff hour for counting runs in the last 7 days')
argparser.add_argument('--data_dir', type=str, default='./data', help='The path to the data directory')
argparser.add_argument('--data', type=str, default='./data/run_times.csv', help='The path to the data file')
args = argparser.parse_args()

os.makedirs(args.data_dir, exist_ok=True)

# Create a naive datetime object (without timezone)
naive_dt = datetime.now()

# Attach the UTC timezone
utc_dt = naive_dt.replace(tzinfo=timezone.utc)

# Convert to another timezone (e.g., Vancouver)
new_dt = utc_dt.astimezone(ZoneInfo("America/Vancouver"))

print(f"Original (UTC): {utc_dt}")
print(f"Converted (New Time Zone): {new_dt}")

now = new_dt
current_date = now.date()
current_time = now.strftime('%H:%M:%S')

def is_recorded(current_date, data):
    # 读取CSV文件，检查今天的日期是否已经记录
    already_recorded = False
    with open(data, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0 and row[0] == str(current_date):
                already_recorded = True
                break
    return already_recorded

if not os.path.exists(args.data):
    with open(args.data, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'First Run Time'])
    print("file has been created.")
        
if now.hour + now.minute / 60 < args.cutoff:
    print("You stayed up too late last night!")
    sys.exit()
else:
    if not is_recorded(current_date, args.data):
        with open(args.data, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_date, current_time])
            print("data has been recorded.")
    else:
        print("You have already recorded today's data.")
        sys.exit()