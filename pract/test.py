import re
def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    other_list = my_list[:4]
    print(other_list)
    print([i for i in my_list if (i%2)==0])
    x = 1
    y = 2
    print(x, "%", y, "=", x%y)

    txt = "The rain in SpainPortugal"
    #Check if "Portugal" is in the string:
    x = re.findall(r"[a-zA-z]*[aeiou][a-zA-z]*", txt)
    print(x)

    if (x):
        print("Yes, there is at least one match!")
    else:
        print("No match")


if __name__ == "__main__":
    main()