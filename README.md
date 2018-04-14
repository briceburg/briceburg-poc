# briceburg-poc

## usage

### dependency container

execute scripts inside a container providing their dependencies...

```
# sort deb-version strings in descending order
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
