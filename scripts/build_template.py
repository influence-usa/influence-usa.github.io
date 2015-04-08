import json

from jinja2 import Template

with open('templates/index.jinja') as fin:
    template = Template(fin.read())

with open('data/campaign_finance_tasks.json') as jin:
    campaign_finance_tasks = json.load(jin)

with open('index.html', 'w') as fout:
    fout.write(template.render(campaign_finance_tasks=campaign_finance_tasks))
