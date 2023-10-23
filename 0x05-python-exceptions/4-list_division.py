#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    li_st = []
    result = 0
    for n in range(list_length):
        try:
            result = my_list_1[n] / my_list_2[n]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            li_st.append(result)
    return (li_st)
