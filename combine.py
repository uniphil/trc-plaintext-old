#!/usr/bin/env python
from __future__ import print_function
import os
import re
import glob
import shutil

import config as c


image_re = r'\!\[(?P<caption>.*)\]\((?P<filename>.*)\)'


def normalize(string):
    normed = string
    normed = string.split('.')[0]
    normed = normed.strip()
    normed, _ = re.subn(r'[^\w]+', '-', normed)
    normed = re.sub(r'\-+$', '', normed)  # trailing -
    return normed


def get_page_folders():
    return sorted(os.listdir(c.OUT_DIR))


def read_cleaned(folder):
    with open('{0}/{1}/{2}'.format(c.OUT_DIR, folder, c.CLEAN)) as f:
        contents = f.read()
    return {
        'folder': folder,
        'fixed': contents,
    }


def compile_images(page):
    def process(match):
        capture = match.groupdict()
        old_filename = capture['filename']
        old_path = '{0}/{1}/{2}'.format(c.OUT_DIR, page['folder'], old_filename)
        caption = capture['caption']
        new_filename = '{0}.jpg'.format(normalize(caption))
        new_path = '{0}/images/{1}'.format(c.COMP_DIR, new_filename)
        shutil.copy(old_path, new_path)
        return '![{0}](images/{1})'.format(caption, new_filename)
    replaced = re.subn(image_re, process, page['fixed'])
    return {
        'folder': page['folder'],
        'fixed': replaced,
    }


def parse_frontmatter(contents):
    yaml = r'^---.*\n---'
    pass


if __name__ == '__main__':
    # join(get_contents())
    map(compile_images,
        map(read_cleaned,
            get_page_folders()))
