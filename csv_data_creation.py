# This is the cvs_data_creation script.
from pathlib import Path
import pandas as pd

dir_path = Path.cwd() / "set_of_data"

if not dir_path.exists():
    dir_path.mkdir(parents=True, exist_ok=True)

name_file = input("Enter the name for the CSV file (without extension): ")

number_columns = int(input("Enter the number of columns for the DataFrame: "))

list_of_column_names = []

for i in range(number_columns):
    name = input(f"Enter name for column {i + 1}: ")
    list_of_column_names.append(name)

data = []
counter = 1
while True:
    local_row = []
    try:
        for i in range(len(list_of_column_names)):
            value = input(f"Enter value {counter} for {list_of_column_names[i]}: ")
            local_row.append(value)
            
        data.append(local_row)
        counter += 1
    except KeyboardInterrupt:
        break
    
print("Data entry complete. Creating DataFrame...")
previous_frame = []
for i in range(len(list_of_column_names)):
    previous_frame.append([None] * len(data))

for i in range(len(data)):
    for j in range(len(list_of_column_names)):
        previous_frame[j][i] = data[i][j]
    
df = pd.DataFrame(data=previous_frame, index=list_of_column_names).transpose()

csv_file_path = dir_path / f"{name_file}.csv"
print(f"Saving DataFrame to CSV file at: {csv_file_path}")

df.to_csv(csv_file_path, index=False)
