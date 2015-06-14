# Plain-text of _Honouring the Truth, Reconciling for the Future_

This repository is an effort to extract the plain-text content of the Truth & Reconciliation Commission's Executive Summary, in order to make it more accessible.


## Sources

Truth & Reconciliation Commission Executive Summary (PDF, 14MB): http://www.trc.ca/websites/trcinstitution/File/2015/Findings/Exec_Summary_2015_05_31_web_o.pdf


## Tech notes

The PDF is split into pages with [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/).

Each page is run thorough [`pdftotext`](http://www.foolabs.com/xpdf/home.html) to extract the text, then through `pdfimages` to extract the images.

The jpgs are all inverted for some reason, so `imagemagick` is used to re-invert them back to normal.

The folder [extracted-pages/](extracted-pages/) contains a subfolder for each page, with the PDF page and extracted text.

These steps are automated with the script [`extract.py`](extract.py):

```bash
$ python extract.py
```

## Fixup Conventions

  * **Photos**: available, auto-extracted from PDF. Perhaps files can be discovered and auto-renamed based on markdown + alt text.
  * **Citations**: no solution yet. For now, using `[[intro:N]]` format, like `[[intro:3]]`, where the number matches the citation number in the Report source. `intro:` prefix is necessary because the TRC numbers reset for each section. `[[]]` convention is made-up, but it should be possible to script a fix if it has to change for a better solution.
  * **Paragraphs spanning page breaks**: flag in front matter to deal with this, `clean_pagebreak`.
  * **Real page numbers vs. TRC page numbers**: No resolution at the moment, can be scripted later if needed.
  * **Medium-specific strings**: removed, including the table of contents, which we can auto-generate.

Fixup example: [Pages 1-10](https://github.com/uniphil/trc-plaintext/pull/1/files).


## To do

 * [x] Ask TRC for plain-text sources
      * They are closing the office, and do not have capacity to provide

 * [ ] Find other parallel efforts and try to join forces
      * [x] Tweet about it
      * [ ] Contact key people who might know (_who?_)
      * [ ] Find more collaborators to help

 * [ ] Extract plain-text
      * [x] Split PDF into pages (so that the plain-text produced can be easily sourced back to the original document) [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/)
      * [x] Extract text strings from each page with [pdftotext](http://www.foolabs.com/xpdf/home.html)
      * [x] Extract images from each page with `pdfimages` (also from `xpdf`)
      * [ ] Fix and mark up the extracted text, one markdown document per page

 * [ ] Rejoin into a giant markdown document
      * [ ] Write a python script for it

 * [ ] Compile plain-text into useable formats
      * [ ] HTML:
          * [ ] Export as an HTML web page, which should be easy to link to for reference
          * [ ] Host the web page somewhere that makes sense. (_where?_)
      * [ ] epub (the [current epub conversion](http://cl.ly/bajb) has formatting issues):
      * [ ] ALL THE FORMATS

 * [ ] Investigate collaborative opportunities with [#ReadTheTRCReport](https://zoeandthecity.wordpress.com/2015/06/08/read-the-trc-video-reading-project-readthetrcreport/)
      * [ ] #6 mentions accessibility, including contributing closed captioning. Contribute that!
      * [ ] Other ways of integrating the source text with the video recordings?
