import os
def prettify_folder(path,filename,format):

    """INSTRUCTIONS:\n\nThe Filename should be in current directory and,
The Filename(with format or extension) should be in current directory.\n"""

    f = open(filename)
    fileList = f.read().split('\n')
    f.close()
    os.chdir(path)
    files = os.listdir(path)

    i = 1
    for file in files:
        if file not in fileList and file.endswith(f".{format}"):
            os.rename(file,f"{i}.{format}")
            i += 1
        else:
            if file not in fileList:
                os.rename(file,file.capitalize())

if __name__ == "__main__":
    try:
        print("\n------------------ Code by Prajjwal ------------------\n")
        print(prettify_folder.__doc__)

        path = input("Enter the full path where you want your changes: ")
        filename = input("Enter the file name: ")
        format = input("Enter the format for specialize changes: ")

        prettify_folder(path,filename,format)
        print("\nDone with changes😊")

    except Exception as e:
        print(f"Something went wrong that is: {e}")
