#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
from github import Github

srcPath = 'src/'
postPath = 'new post/'

pathDict = {}
for dirname, dirnames, filenames in os.walk(srcPath):
    floderName = dirname[dirname.rfind('/')+1:]
    if (len(floderName) > 0):
        pathDict[floderName] = dirname

githubToken = os.environ.get('GITHUB_TOKEN')
# githubToken = os.environ.get('ee3880a9d12ecc0ea560ee24bd9102fc89dc96c2')
githubRepo = os.environ.get('GITHUB_REPOSITORY')
# githubRepo = os.environ.get('xize1993/leetcode')
# g = Github(githubToken)
# repo = g.get_repo(githubRepo)
g = Github('ee3880a9d12ecc0ea560ee24bd9102fc89dc96c2')
repo = g.get_repo('xize1993/leetcode')
closedIssues = repo.get_issues(state='closed')
lastClosedIssue = sorted(closedIssues, key=lambda x: x.closed_at, reverse=True)[0]
targetDir = ''
no = -1
if (lastClosedIssue.title.startswith('post:')):
    no = lastClosedIssue.title[5:]
    for label in lastClosedIssue.labels:  
        if label.name in pathDict:
            targetDir = pathDict[label.name]

if targetDir:
    files = list(filter(lambda x: x.startswith(no) and x.endswith('.md'), os.listdir(postPath)))
    if (len(files) > 0):
        os.rename(postPath + files[0], targetDir + '/' + files[0])
    else:
        raise RuntimeError('post file is not exist')
else:
    raise RuntimeError('target directory is not exist')