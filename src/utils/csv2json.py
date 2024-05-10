import csv
import json
import sys
 
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = []
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary 
        # and add it to data
        for id, rows in enumerate(csvReader):
            print(rows)
            data.append(rows)
            # if id == 0: 
            #     keys = list(rows)
            #     continue

            # data.append(dict())
            # for rid, key in enumerate(keys):
            #     data[id-1][key] = rows[rid]
 
    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        json.dump(data, jsonf, indent=4, ensure_ascii=False, separators=(',', ':'))
 
# Call the make_json function
if __name__ == "__main__":
    make_json(sys.argv[1], sys.argv[2])