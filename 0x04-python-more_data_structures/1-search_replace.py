#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li_st = []
    for i in my_list:
        if i == search:
            li_st.append(replace)
        else:
            li_st.append(i)
    return (li_st)
