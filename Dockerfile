FROM debian:jessie

# deps
RUN apt-get update && apt-get install -y \
  python-apt \
  && rm -rf /var/lib/apt/lists/*
