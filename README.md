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
  1.11-12 \
  1.11-6 \
  9.99 \
  0:9.99-12 \
  1:1.11 \
  1:1.11-12 \
  1:1.11-18 \
  1:9.99 \
  1:string \
  string
```
