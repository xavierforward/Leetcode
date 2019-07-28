# -*- coding: utf-8 -*-
import json, sys

url = 'https://leetcode.com'

with open('_data/config.json', 'r+') as f_config:
    config = json.load(f_config)
    if(len(sys.argv) > 1 and sys.argv[1]) :
        no = int(sys.argv[1])
    else :
        no = int(config['last_no']) + 1
    config['last_no'] = no 
    f_config.seek(0)
    f_config.truncate()
    json.dump(config, f_config)
        
print('Question %s is about to be generated' % no)

problem_data = {}
with open('_data/problemset.json', 'r') as f_problemset:
    problemset = json.load(f_problemset)
    problem = problemset['stat_status_pairs'][-1 * no] 
    problem_data['title_en'] = '%s.%s' % (no, problem['stat']['question__title'])
    problem_data['file_name'] = '%s_%s.md' % (no, problem['stat']['question__title'].replace(' ', '_').lower())
    problem_data['url'] = '%s/problems/%s/' % (url, problem['stat']['question__title_slug'])

with open('_data/translation.json', 'r') as f_translation:
    translations = json.load(f_translation)
    problem_data['title_cn'] = '%s.%s' % (no, translations['data']['translations'][no-1]['title'])

# generate the Markdown file
with open('src/%s' % problem_data['file_name'], 'w') as mdf:
    mdf.write('# %s' % problem_data['title_cn'])
    mdf.write('\n')
    mdf.write('## 题目')
    mdf.write('\n')
    mdf.write('[原题链接](%s)' % problem_data['url'])
    mdf.write('\n')
    mdf.write('\n')
    mdf.write('## 思路')
    mdf.write('\n')
    mdf.write('\n')
    mdf.write('## 代码')
    mdf.write('\n')
    mdf.write('```java')
    mdf.write('\n')
    mdf.write('```')

print('Question %s has been generated' % no)

