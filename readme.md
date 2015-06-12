# Plain-text of _Honouring the Truth, Reconciling for the Future_

This repository is an effort to extract the plain-text content of the Truth & Reconciliation Commission's Executive Summary, in order to make it more accessible.


## Sources

Truth & Reconciliation Commission Executive Summary (PDF, 14MB): http://www.trc.ca/websites/trcinstitution/File/2015/Findings/Exec_Summary_2015_05_31_web_o.pdf


## Tech notes

The PDF is split into pages with [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/).

Each page is run thorough [`pdftotext`](http://www.foolabs.com/xpdf/home.html) to extract the text.

The folder [extracted-pages/](extracted-pages/) contains a subfolder for each page, with the PDF page and extracted text.

These steps are automated with the script [`extract.py`](extract.py):

```bash
$ python extract.py
```


## To do

 * [x] Ask TRC for plain-text sources
      * They are closing the office, and do not have capacity to provide

 * [ ] Find other parallel efforts and try to join forces
      * [x] Tweet about it
      * [ ] Contact key people who might know (_who?_)
      * [ ] Find more collaborators to help

 * [ ] Extract plain-text
      * [ ] Split PDF into pages (so that the plain-text produced can be easily sourced back to the original document) [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/)
      * [ ] Extract text strings from each page with [pdftotext](http://www.foolabs.com/xpdf/home.html)
      * [ ] Fix and mark up the extracted text, one markdown document per page

 * [ ] Compile plain-text into useable formats
      * [ ] HTML:
          * [ ] Export as an HTML web page, which should be easy to link to for reference
          * [ ] Host the web page somewhere that makes sense. (_where?_)
      * [ ] epub (the [current epub conversion](http://cl.ly/bajb) has formatting issues):
      * [ ] ALL THE FORMATS

 * [ ] Investigate collaborative opportunities with [#ReadTheTRCReport](https://zoeandthecity.wordpress.com/2015/06/08/read-the-trc-video-reading-project-readthetrcreport/)
      * [ ] #6 mentions accessibility, including contributing closed captioning. Contribute that!
      * [ ] Other ways of integrating the source text with the video recordings?
