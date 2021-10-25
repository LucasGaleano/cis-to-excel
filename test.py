import fitz
import argparse
import re
import time

parser = argparse.ArgumentParser()
parser.add_argument('cisDocument', type=str)
args = parser.parse_args()

pdf = fitz.open(args.cisDocument)


end = '(Remedation:|P a g e| Audit:| Rationale:| Description:| Profile Applicability:|CIS Controls:|Impact:|References:|Notes:|$)'
fields = dict()

fields['ID'] = 'P a g e\s*([\d.]*)(.*?)' + end 
fields['title'] = 'P a g e\s*[\d.]*(.*?)\s*' + end
fields['profile'] = 'Profile Applicability:(.*?)' + end 
fields['description'] = 'Description: (.*?)' + end 
fields['rationale'] = 'Rationale: (.*?) ' + end 
fields['impact'] = 'Impact: (.*?) ' + end 
fields['audit'] = 'Audit: (.*?)' + end 
fields['remediation'] = 'Remediation: (.*?)' + end 



def match(regex):    
    #print(page.get_text().replace('\t',' '))
    matchRegex = re.search(regex, page.get_text().replace('\t',' ').replace('\n',' '), re.MULTILINE)
    if matchRegex:
        return matchRegex.group(1)
        #print(title, matchRegex.group(1))



for page in pdf:
    print('###############################################\n\n\n')
    print(page.get_text().replace('\t',' '))
    for nameField, field in fields.items():
        text = match(field)
        print(nameField,'####',text)
