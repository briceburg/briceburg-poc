# briceburg-poc

[![Build Status](https://travis-ci.org/briceburg/briceburg-poc.svg?branch=master)](https://travis-ci.org/briceburg/briceburg-poc)
![try some wheels](docs/Agile-Pyramid-comic-transparant.png)

## usage

### bin/run

`bin/run` executes arbitrary commands inside a container providing dependencies. [Dockerfile source](Dockerfile).

```
bin/run <command>
bin/run ls
bin/run scripts/deb-version-compare.py
```


## scripts

### deb-version-compare.py

sort deb-version strings in descending order (highest priority first).


```
# example
bin/run scripts/deb-version-compare.py \
  1:1.4.6-8 \
  1.4.7 \
  1.4.7-99 \
  0.8.5 \
  8.5 \
  .8.5 \
  0:1.4.7 \
  0:8.5 \
  string-version \
  2:string-version \
  1:string-version
```
