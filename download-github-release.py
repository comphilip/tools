#!/usr/bin/env python3

import argparse
import urllib.request
import json
import subprocess
import os.path
import sys


def parse_arg():
    parser = argparse.ArgumentParser(
        description="Download github release file")
    parser.add_argument("--release", help="Release id", default="latest")
    parser.add_argument(
        "repo", help="Github repository, like microsoft/vscode")
    parser.add_argument("files", nargs='+', help="file name to download")
    return parser.parse_args()


def fetch_github_release(repo: str, release: str):
    print("Downloading {} release {}".format(repo, release), file=sys.stderr)
    req = urllib.request.Request(
        "https://api.github.com/repos/{}/releases/{}".format(repo, release))
    req.add_header("Accept", "application/vnd.github.v3+json")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def download_file(url: str):
    file_name = os.path.basename(url)
    re = subprocess.run(['curl', '-Lo', file_name, url],
                        stdout=sys.stdout, stderr=sys.stderr)
    if re.returncode != 0:
        raise Exception("Filed to download {}".format(url))


def main():
    args = parse_arg()
    release_info = fetch_github_release(args.repo, args.release)
    for file in args.files:
        for asset in release_info['assets']:
            if file == asset['name']:
                download_file(asset['browser_download_url'])


if __name__ == "__main__":
    main()
