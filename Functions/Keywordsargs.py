def funkey(**kwargs):
    print("Printing the Keyword arguments=")
    for key, val in kwargs.items():
        print(f"{key}=={val}")

funkey(a='a',b='b',c='c',d='d')