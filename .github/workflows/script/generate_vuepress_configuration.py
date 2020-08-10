#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, yaml

def loadFileTree(path):
  '''
  从目录提取侧边栏配置信息
  '''
  fileTree = list(filter(lambda x: x != '.vuepress' and x != 'index.md', os.listdir(path)))
  fileTree.sort(key = lambda x: int(x[:x.index('_')]) if x.find('_') > 0 else 0)
  for i in range(len(fileTree)):
    if (fileTree[i].endswith('.md')):
      fileTree[i] = path[path.find('/'):] + fileTree[i][:fileTree[i].index('.md')]
    elif os.path.isdir(path+fileTree[i]):
      title = fileTree[i]
      children = loadFileTree(path + fileTree[i] + '/')
      fileTree[i] = {
        '/' + fileTree[i] + '/': '',
        'title': title,
        'children': children
        }
  return fileTree

def wirteConfig(fileTree):
  '''
  创建vuepress的配置文件
  '''
  templatePath = 'data/vuepress-config-template.yml'
  with open(templatePath, 'r+') as f:
      yml_obj = yaml.load(f.read(), Loader=yaml.FullLoader)
      yml_obj['themeConfig']['sidebar']['/'] = fileTree
  
  configPath = 'src/.vuepress/config.yml'
  if not os.path.exists(configPath):
    os.mkdir('src/.vuepress')
    open(configPath, 'w').close()
  with open(configPath, 'r+') as f:
    f.seek(0)
    f.truncate()
    yaml.dump(yml_obj, f, encoding='utf-8',allow_unicode=True)

if __name__ == "__main__":
  srcPath = 'src/'
  fileTree = loadFileTree(srcPath)
  fileTree.insert(0, '')
  wirteConfig(fileTree)