def safe_print_list(my_list=[], x=0):
    leng = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            leng = leng + 1
        except IndexError:
            print("")
            return leng
    print("")
    return leng
