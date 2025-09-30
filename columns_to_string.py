import clipboard


str_clipboard = clipboard.paste()

if '\r\n' in str_clipboard:
    str_split = '\r\n'
elif '\n' in str_clipboard and '\r' not in str_clipboard:
    str_split = '\n'

list_clipboard = str_clipboard.split(str_split)

if list_clipboard[0].isdigit():
    str_new_clipboard = (",").join(list_clipboard) 
else:
    str_new_clipboard = "'" + ("','").join(list_clipboard) + "'"
clipboard.copy(str_new_clipboard)