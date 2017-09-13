plagiarism
==========

[![license](https://img.shields.io/github/license/uulm/plagiarism.svg)](https://github.com/uulm/plagiarism/blob/master/LICENSE)

#### Requirements

* Python 3.6.2


#### Installation

`python-Levenshtein` may not be installed successfully on Windows, use the whl file from http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-levenshtein.

```bash
pip3 install -r requirements.txt
```


#### Usage

To search for plagiated documents:

```bash
main.py localfile.pdf
main.py localfile.txt
main.py http://example.ru/somefile.txt
main.py ftp://example.com/somefile.pdf
```

Press Ctrl-C to skip any file you don't want to test

Notice, that somefile.txt must have 'utf-8' encoding.

Or you can use it as a package:

```python
from plagiarism import checkfile

checkfile('localfile.pdf')
```

Chinese documents expected.


#### FEATURE

- [x] Keywords extraction by TF-IDF
- [x] Plagiarism detection by Levenshtein Distance
- [x] Support reading file from local filesystem
- [x] Support reading file from network
- [x] Support China Academic Journals (`.caj`) files <sup>*</sup>
- [x] Support Microsoft Office Word 97 (`.doc`) files
- [x] Support Office Open XML Document (`.docx`) files
- [x] Support HyperText Markup Language (`.html`) files
- [x] Support Portable Document Format (`.pdf`) files
- [x] Support Rich Text Format (`.rtf`) files
- [x] Support Text File (`.txt`) files
- [ ] Search related papers from Internet
- [x] As a python package
- [x] As a script


#### Attention

The **sample** of `spider.py` use CNKI's kns55 platform to get related papers, though the sample is **unfinished**, abusing the kns55 platform may break the ToS and EULA of CNKI.

Use these codes **at your own risk**.


#### License

This project is licensed under the [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html), for more information, see [LICENSE](LICENSE).
