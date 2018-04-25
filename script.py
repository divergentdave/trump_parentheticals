#!/usr/bin/env python3
import html
import io
import json
import re
import zipfile

PAREN_RE = re.compile("\\(([^)]+)\\)")


def extract_tweets(path):
    with zipfile.ZipFile(path, "r") as zf:
        for zi in zf.infolist():
            with zf.open(zi) as f:
                data = json.load(io.TextIOWrapper(f, "utf-8"))
                for tweet in data:
                    yield tweet["text"]


def main():
    for year in range(2009, 2019):
        path = "trump_tweet_data_archive/condensed_{}.json.zip".format(year)
        for tweet_text in extract_tweets(path):
            original = tweet_text
            tweet_text = html.unescape(tweet_text)
            tweet_text = tweet_text.replace("(cont)", "")
            for parenthetical in PAREN_RE.findall(tweet_text):
                print(parenthetical)


if __name__ == "__main__":
    main()
