with open('app/data/en-abbreviations.txt', 'r') as text_file:
    whole_text = text_file.read()
lines_array = whole_text.splitlines()

def remove_comments(text):
    no_comments = []
    for line in text:
        if '#' in line:
            continue
        no_comments.append(line)
    return no_comments

def ten_headers(text):
    output = []
    for i in range(10):
        output.append(text[i])
    return output

def search_string(string):
    if string:
        results = []
        for line in no_comments:
            if line.startswith(string):
             results.append(line)
    else:
        return ["Search Term Empty"]
    return results

no_comments = remove_comments(lines_array)
ten_abbs = ten_headers(no_comments)




