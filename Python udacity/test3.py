#define the  html_list function
def html_list(str_list):
    str_res = "<ul>\n"
    for item in str_list:
        str_res += "<li>" + item + "</li>\n"
    str_res += "</ul>"
    return str_res

lis = ['first string', 'second string']
print(html_list(lis))
