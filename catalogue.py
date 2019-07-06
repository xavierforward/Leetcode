# -*- coding: utf-8 -*-
import os, yaml

path1 = 'src/'
path2 = 'src/.vuepress/config.yml'

flist = list(filter(lambda x: x.endswith('.md') and x != 'index.md', os.listdir(path1)))
flist.sort(key = lambda x: int(x[:x.index('_')]))
for i in range(len(flist)):
  flist[i] = '/' + flist[i][: flist[i].index('.md')]
flist.insert(0, '')

with open(path2, 'r+') as f:
    yml_obj = yaml.load(f.read())
    f.seek(0)
    f.truncate()
    yml_obj['themeConfig']['sidebar']['/'] = flist
    yaml.dump(yml_obj, f)