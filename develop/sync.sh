#!/bin/bash
if [ -d "./framework/" ]
then
  echo "./framework dir exists"
else
  mkdir framework/
fi
# sync webpy
if [ -d "./framework/webpy/" ]
then
  echo "./framework/webpy/ exists"
  cd ./framework/webpy
  git pull
else 
  mkdir ./framework/webpy/
  cd ./framework/webpy/
  git clone https://github.com/webpy/webpy.git
fi
# sync flask
# sync django
