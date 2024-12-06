# Process
This document describes the progress I make with finding a solution to the smart markdown download link replacer.

## Chat GPT thoughts
Q: im looking for a way to turn myst markdown files into ordinary markdown files

A: 
1. Use myst-parser
2. Use Pandoc
3. Manual cleanup
4. Custom script
   1. use regex python


The first two options seem to have potential, the third option is not what i am looking for as an automated process is desired, the fourth option is a last resort for now.
I will look into myst-parser first, and into Pandoc second.

## Use myst parser
myst parser is just the package that can is used to read and display myst markdown documents. On first sight is does not have the ability to convert markdown files from myst to ordinary.

## Pandoc
The website states: "Pandoc can convert between numerous markup and word processing formats, including, but not limited to, various flavors of Markdown, HTML, LaTeX and Word docx."
This is more promising.
I will now test this by setting up pandoc on a conda environement.

Pandoc is not directly able to convert myst markdown to normal markdown

I did find an issue on [github](https://github.com/executablebooks/rst2myst/issues/2) which describes the exact issue.

This issue led me to [panflute](https://github.com/sergiocorreia/panflute), maybe this python package for creating pandoc filter will help in achieving my goal. [docs](https://scorreia.com/software/panflute/index.html)

Panflute seems to be able to help with writing filters to filter out certain myst features. However on first sight there are not any existing myst filters available.

The issue on [github](https://github.com/executablebooks/rst2myst/issues/2) also leads to a project called [rst-to-myst](https://github.com/executablebooks/rst-to-myst). This also seems helpful, as this project seems to be the reason that the issue on the repo was archived.

## Custom script
I made a start for a custom script. I am using regex to filter out myst markdown directives. I think this solution is reasonable, but i still need to finish it and write some tests to check edge cases. For now i will only focus on the directives that are most commonly found in myst markdown files. Starting with tips and indexes.

## Converting myst -> rst -> md
Using [rst-to-myst](https://github.com/executablebooks/rst-to-myst) and pandoc.
This only works if the rst-to-myst package can convert both ways.


## For jupyter notebooks:
Tool to convert jupyter notebooks to plain text: [Jupy-text](https://jupytext.readthedocs.io/en/latest/#)
