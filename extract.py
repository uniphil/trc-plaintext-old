#!/usr/bin/env python
from __future__ import print_function
import os
import glob
import shutil
import subprocess

import config as c


def split_pages():
    if len(os.listdir(c.OUT_DIR)) > 0:
        return  # already done, delete OUT_DIR contents first to redo
    out_template = 'pdf-pages/page-%03d.pdf'
    cmd = ['pdftk', c.ORIG, 'burst', 'output', out_template]
    if subprocess.call(cmd) is not 0:
        raise SystemExit('Failed to split pages from', c.ORIG)


def is_pdf(filename):
    return filename.rsplit('.', 1)[1] == 'pdf'


def get_name(filename):
    return {
      'orig': filename,
      'name': filename.rsplit('.', 1)[0],
    }

def extract(name):
    pdfpath = '{0}/{1}'.format(c.PDF_DIR, name['orig'])
    txtdir = '{0}/{1}'.format(c.OUT_DIR, name['name'])
    txtpath = '{0}/{1}/extracted.txt'.format(c.OUT_DIR, name['name'])
    mdpath = '{0}/{1}/{2}'.format(c.OUT_DIR, name['name'], c.CLEAN)
    pdfoutpath = '{0}/{1}/page.pdf'.format(c.OUT_DIR, name['name'])
    imageroot = '{0}/{1}/image'.format(c.OUT_DIR, name['name'])

    try:
        os.mkdir(txtdir)
    except OSError:  # already exists (probably)
        pass

    if not os.path.isfile(txtpath):
        result = subprocess.call(['pdftotext', pdfpath, txtpath])
        if result is not 0:
            raise SystemExit('Failed to extract text from', name['orig'])
        result = subprocess.call(['pdfimages', '-j', pdfpath, imageroot])
        if result is not 0:
            raise SystemExit('Failed to extract images from', name['orig'])
        # seems like all the images we need are jpegs, ppms are all blank white?
        map(os.remove, glob.glob('{0}/*.ppm'.format(txtdir)))
        # for some reason all the jpegs are inverted. re-invert them:
        map(lambda f: subprocess.call(['convert', '-negate', f, f]),
            glob.glob('{0}/*.jpg'.format(txtdir)))

    if not os.path.isfile(pdfoutpath):
        shutil.copyfile(pdfpath, pdfoutpath)


def insert_frontmatter(fname):

    fcontent = "---\nclean_pagebreak: true\n---\n\n"
    with open(fname) as f:
        fcontent += f.read()
    with open(fname, 'w') as f:
        f.write(fcontent)


if __name__ == '__main__':
    print('splitting pages...')
    split_pages()
    print('extracting...')
    map(extract,
        map(get_name,
            filter(is_pdf,
                os.listdir(
                    c.PDF_DIR))))
    print('insert frontmatter...')
    map(insert_frontmatter, glob.glob('{0}/*/{1}'.format(c.OUT_DIR, c.CLEAN)))
