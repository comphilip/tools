#!/usr/bin/env bash
set -e

download-github-release.py rust-analyzer/rust-analyzer ra_lsp_server-linux rust-analyzer-0.1.0.vsix
chmod a+x ra_lsp_server-linux
mv ra_lsp_server-linux ~/bin/ra_lsp_server