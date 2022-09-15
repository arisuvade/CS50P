question = input("File name: ")
file_name = question[-3] + question[-2] + question[-1]

if file_name == "gif":
    print("images/gif")
elif file_name == "jpg":
    print("images/jpeg")
elif file_name == "peg":
    print("images/jpeg")
elif file_name == "png":
    print("images/png")
elif file_name == "pdf":
    print("pdf file")
elif file_name == "txt":
    print("text file")
elif file_name == "zip":
    print("zip file")
else:
    print("application/octet-stream")
