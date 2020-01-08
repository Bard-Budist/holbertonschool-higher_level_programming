def safe_print_list(my_list=[], x=0):
    leng = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            leng = leng + 1
        print("")
    except IndexError:
        print("")
    return leng
