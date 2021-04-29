import PyPDF2
import re

pdfFile = open('cis.pdf','rb')
pdf = PyPDF2.PdfFileReader(pdfFile)

ID = 'Page  ([\d.]*) (.*)Profile Applicability:' 
title = 'Page  [\d.]* (.*) (\(Scored\)|\(Not Scored\))?Profile Applicability:'
profile = 'Profile Applicability:   (.*) Description:'
description = 'Description: (.*) Rationale:'
rationale = 'Rationale: (.*?) (Audit:|$)'
audit = 'Audit: (.*?)(\d* \| Page | Remediation:|$)'
remediation = 'Remediation: (.*?)(\d* \| Page)? (CIS Controls:|Impact:|References:|Notes:|$)'

fields = [ID, title, profile, description, rationale, audit, remediation]


def match(regex):    
    matchRegex = re.search(regex, getText(pdf, pageNumber), re.MULTILINE)
    if matchRegex:
        return matchRegex.group(1)
        #print(title, matchRegex.group(1))
        

def getText(pdf, pageNumber):
    return pdf.getPage(pageNumber).extractText().replace('\n','')

def add_row(row, item):
    if item is not None:
        row.append(item)


print('ID, Title, Profile, Description, Rationale, Audit, Remediation')

for pageNumber in range(0,pdf.getNumPages()):
    

    for field in fields:
        #print('\n\n',field)
        text = match(field)
        if text is not None:
            print('"', end='')
            print(text.replace('"','""'),end='')
            print('"', end='')
            if "Remediation: " in field:
                print()
            else:
                print(',', end='')

