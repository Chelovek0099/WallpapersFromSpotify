import markdown


def markdownToHtml(myFile):
    with open(myFile, 'r', encoding='utf-8') as file:
        content = file.read()
    html = markdown.markdown(content)
    return html
