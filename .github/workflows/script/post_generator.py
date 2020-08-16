#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, sys, os
from github import Github

def generateProblem(no):
    url = 'https://leetcode.com'
    problem_data = {}
    with open('data/problemset.json', 'r') as f_problemset:
        problemset = json.load(f_problemset)
        problem = problemset['stat_status_pairs'][-1 * no] 
        problem_data['title_en'] = '%s.%s' % (no, problem['stat']['question__title'])
        problem_data['file_name'] = '%s_%s.md' % (no, problem['stat']['question__title'].replace(' ', '_').lower())
        problem_data['url'] = '%s/problems/%s/' % (url, problem['stat']['question__title_slug'])

    with open('data/translation.json', 'r') as f_translation:
        translations = json.load(f_translation)
        problem_data['title_cn'] = '%s.%s' % (no, translations['data']['translations'][no-1]['title'])

    # generate the Markdown file
    if not os.path.exists('new post'):
        os.mkdir('new post')
    with open('new post/%s' % problem_data['file_name'], 'w') as mdf:
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

if __name__ == "__main__":
    githubToken = os.environ.get('GITHUB_TOKEN')
    githubRepo = os.environ.get('GITHUB_REPOSITORY')
    g = Github(githubToken)
    repo = g.get_repo(githubRepo)
    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        if (repo.owner == issue.user and len(issue.labels) > 0):
            generateProblem(int(issue.title[issue.title.find(':')+1:]))
