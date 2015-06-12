#!/usr/bin/env python
from __future__ import print_function
import os
import shutil
import subprocess

ORIG = 'Exec_Summary_2015_05_31_web_o.pdf'
PDF_DIR = 'pdf-pages'
OUT_DIR = 'extracted-pages'


def split_pages():
    out_template = 'pdf-pages/page-%03d.pdf'
    cmd = ['pdftk', ORIG, 'burst', 'output', out_template]
    if subprocess.call(cmd) is not 0:
        raise SystemExit('Failed to split pages from', ORIG)


def is_pdf(filename):
    return filename.rsplit('.', 1)[1] == 'pdf'


def get_name(filename):
    return {
      'orig': filename,
      'name': filename.rsplit('.', 1)[0],
    }

def pdf_to_text(name):
    pdfpath = '{0}/{1}'.format(PDF_DIR, name['orig'])
    txtdir = '{0}/{1}'.format(OUT_DIR, name['name'])
    txtpath = '{0}/{1}/extracted.txt'.format(OUT_DIR, name['name'])
    mdpath = '{0}/{1}/fixed.md'.format(OUT_DIR, name['name'])
    pdfoutpath = '{0}/{1}/page.pdf'.format(OUT_DIR, name['name'])
    os.mkdir(txtdir)
    result = subprocess.call(['pdftotext', pdfpath, txtpath])
    if result is not 0:
        raise SystemExit('Failed to extract text from', name['orig'])
    shutil.copyfile(txtpath, mdpath)
    shutil.copyfile(pdfpath, pdfoutpath)


if __name__ == '__main__':
    print('splitting pages...')
    split_pages()
    print('extracting text...')
    map(pdf_to_text,
        map(get_name,
            filter(is_pdf,
                os.listdir(
                    PDF_DIR))))
