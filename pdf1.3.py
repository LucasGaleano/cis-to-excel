import fitz
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('cisDocument', type=str)
args = parser.parse_args()

pdf = fitz.open(args.cisDocument)

end = '(P a g e|Audit:|Rationale:|Description:|Profile Applicability:|CIS Controls:|Impact:|References:|Notes:|$)'
ID = 'P a g e\s*([\d.]*)(.*)Profile Applicability:' 
title = 'P a g e\s*[\d.]*(.*)\s*Profile Applicability:'
profile = 'Profile Applicability:(.*)Description:'
description = 'Description: (.*) Rationale:'
rationale = 'Rationale: (.*?) (Audit:|$)'
impact = 'Impact: (.*?) (Audit:|$)'
audit = 'Audit: (.*?)(\d* \| Page | Remediation:|$)'
remediation = 'Remediation: (.*?)(\d* \| Page)? (CIS Controls:|Impact:|References:|Notes:|$)'

fields = [ID, title, profile, description, rationale, impact ,audit, remediation]


def match(regex):    
    #print(page.get_text().replace('\t',' '))
    matchRegex = re.search(regex, page.get_text().replace('\t',' ').replace('\n',' '), re.MULTILINE)
    if matchRegex:
        return matchRegex.group(1)
        #print(title, matchRegex.group(1))


def add_row(row, item):
    if item is not None:
        row.append(item)


print('ID, Title, Profile, Description, Rationale, Impact, Audit, Remediation')

for page in pdf:
    for field in fields:
        #print('\n\n',field)
        text = match(field)
        #print(text)
        if text is not None:
            print('"', end='')
            print(text.replace('"','""'),end='')
            print('"', end='')
            if "Remediation: " in field:
                print()
            else:
                print(',', end='')
