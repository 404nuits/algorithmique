def contains(string, substring):
    found = False
    i = 0
    start_index = -1

    for char_index,char in enumerate(string):
        
        if char == substring[i]:
            
            if i == 0:
                start_index = char_index

            i += 1

            if i == len(substring):
                
                found = True
                break

        else:
            i = 0

    if found:
        return start_index
    else:
        return -1

def replace(text,old,new):

    start_index = contains(text,old)
    end_index = start_index + len(old) - 1

    new_text = ""

    for i,c in enumerate(text):
        if i < start_index or i > end_index:
            new_text += c
        elif i == start_index:
            new_text += new
    
    return new_text

def replace_all(text,old,new):

    found = contains(text, old)

    while found != -1:
        text = replace(text, old, new)
        found = contains(text, old)

    return text

if __name__ == '__main__':
    text = "lorem ipsum sic dolor"
    print(replace_all(text, "s", "f"))
    