from read_json_file import read_json    

file_path = "C:\\office\\rohit-workspace\\assignments\\PySpark\\amazon_toys_and_games.json"

df = read_json(file_path, data_library='pandas')
print(len(df))
