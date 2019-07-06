#!/bin/bash
set -e 
read -p "Input git message: " msg

# 更新侧边栏目录脚本
python3 catalogue.py

cd src/
git add .
git commit -m $msg
git push origin master 

cd ../
npm run build
cd src/.vuepress/dist/
git init
git add -A
git commit -m $msg
git push -f git@github.com:zhaozecheng/Leetcode.git master:gh-pages


