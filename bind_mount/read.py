# read_file.py

FILE_NAME = "file.txt"

def read_file():
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read()

        if data.strip():
            print("File content:\n")
            print(data)
        else:
            print("File is empty.")
    except FileNotFoundError:
        print(f"'{FILE_NAME}' not found. Please create the file first.")

if __name__ == "__main__":
    read_file()
