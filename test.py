import fitz
import argparse
import re
import time
from alive_progress import alive_bar

parser = argparse.ArgumentParser()
parser.add_argument('cisDocument', type=str)
args = parser.parse_args()

pdf = fitz.open(args.cisDocument)


end = '(Remediation:|P a g e| Audit:| Rationale:| Description:| Profile Applicability:|CIS Controls:|Impact:|References:|Notes:|$)'
end2 = '(Remediation:|P a g e| Audit:| Rationale:| Description:| Profile Applicability:|CIS Controls:|Impact:|References:|Notes:)'

fields = dict()
fields['ID'] = r'P a g e\s*([\d.]+)(.*?)' + end2 
fields['title'] = r'P a g e\s*[\d.]+(.*?)\s*' + end2
fields['profile'] = r'Profile Applicability:(.*?)' + end 
fields['description'] = r'Description: (.*?)' + end 
fields['rationale'] = r'Rationale: (.*?) ' + end 
fields['impact'] = r'Impact: (.*?) ' + end 
fields['audit'] = r'Audit: (.*?)' + end 
fields['remediation'] = r'Remediation: (.*?)' + end 



def match(regex):    
    #print(page.get_text().replace('\t',' '))
    matchRegex = re.search(regex, page.get_text().replace('\t',' ').replace('\n',' '), re.MULTILINE)
    if matchRegex:
        return matchRegex.group(1)
        #print(title, matchRegex.group(1))

def quotes_text(text: str) -> str:
    print('"', end='')
    print(text.replace('"','""'),end='')
    print('"', end='')


with alive_bar(pdf.page_count ,title='Number of Pages', length=30) as bar:
    for page in pdf:   
        bar()
        
        # print('###############################################\n\n\n') #DEBUG
        # print(page.get_text().replace('\t',' ')) #DEBUG
        for nameField, field in fields.items():
            text = match(field)
            # if text is not None:
                # quotes_text(text)
                # if "Remediation" == nameField:
                    # print()
                # else:
                    # print(',', end='')
            
            # print(nameField,'####',text) #DEBUG
