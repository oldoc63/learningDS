#Open a file
with open('files_in_python/real_cool_document.txt') as cool_doc:
    cool_contents = cool_doc.read()
print(cool_contents)