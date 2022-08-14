while True:
    foo = input()
    foor = int(foo.split(", ")[0])
    foog = int(foo.split(", ")[1])
    foob = int(foo.split(", ")[2])

    print(f"{round(foor/255,4)},{round(foog/255,4)},{round(foob/255,4)}")
