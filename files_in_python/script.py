#Open a file and read the whole document
with open('files_in_python/real_cool_document.txt') as cool_doc:
    cool_contents = cool_doc.read()
print(cool_contents)

#Open a file and read it line by line
with open('keats_sonnet.txt') as keats_sonnet:
    for line in keats_sonnet.readlines():
        print(line)