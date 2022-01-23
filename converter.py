import markdown


with open('interview.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('interview.html', 'w') as f:
    f.write(html)


