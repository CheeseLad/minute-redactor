#!/usr/bin/env python3

import re
import os 
from config import committee_members

if "redacted" not in os.listdir():
    os.mkdir("redacted")

formatting_roles = {
    "chair": "`chair`",
    "vice-chair": "`vice-chair`",
    "secretary": "`secretary`",
    "treasurer": "`treasurer`",
    "webmaster": "`webmaster`",
    "events": "`events`",
    "pro": "`pro`",
    "sysadmin": "`sysadmin`",
    "gdo": "`gdo`",
    "helpdesk": "`helpdesk`",
    "first-year-rep": "`first-year-rep`",
    "ordinary-member": "`ordinary-member`",
}

def main(file_location):
    text = []
    with open(file_location, 'r') as f:
        for line in f:
            text.append(line)

    new_file = "./redacted/" + file_location.strip(".md") + " - Redacted.md"


    with open(new_file, 'w') as f:
        text = "".join(text)
        for word in committee_members:
            pattern = r'\b{}\b'.format(re.escape(word))
            text = re.sub(pattern, committee_members[word], text)
        for word in formatting_roles:
            pattern = r'\b{}\b'.format(re.escape(word))
            text = re.sub(pattern, formatting_roles[word], text)
        text = text.replace("vice-`chair`", "`vice-chair`")
        text = text.replace("``", "`")
        try:
            retrospective_text = text[text.index("## Retrospective"):]
            f.write(text[:text.index("# Useful Links:")])
            f.write(retrospective_text)
        except:
            f.write(text[:text.index("# Useful Links:")])
        
        print("Redacted file written to " + new_file)

for item in os.listdir():
    if item.endswith(".md"):
        main(item)

