#!/bin/bash
set -e 
read -p "Input git message: " msg

# 更新侧边栏目录脚本
docker-compose run --rm lc-python python catalogue.py


# 提交git仓库，并推送markdown文件等到主分支
cd src/
git add .
git commit -m $msg
git push origin master 

# 编译vuepress
cd ../
docker-compose run --rm lc-vuepress npx vuepress build src

# 提交编译后的静态文件到gitpage分支
cd src/.vuepress/dist/
git init
git add -A
git commit -m $msg
git push -f git@github.com:zhaozecheng/leetcode.git master:gh-pages