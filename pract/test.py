def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    other_list = my_list[:4]
    print(other_list)
    print([i for i in my_list if (i%2)==0])
    x = 1
    y = 2
    print(x, "%", y, "=", x%y)

if __name__ == "__main__":
    main()