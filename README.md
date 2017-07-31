plagiarism
==========

[![license](https://img.shields.io/github/license/uulm/plagiarism.svg)](https://github.com/uulm/plagiarism/blob/master/LICENSE)

#### Requirements

* Python 3.6.2


#### Installation

```bash
pip3 install -r requirements.txt
```


#### Usage

To search for plagiated documents:

```bash
main.py localfile.txt
main.py localfile.pdf
main.py http://example.ru/somefile.txt
main.py ftp://example.com/somefile.pdf
```

Press Ctrl-C to skip any file you don't want to test

Notice, that somefile.txt must have 'utf-8' encoding.

Chinese documents expected.


#### TODO

* [ ] support Word 97 (`.doc`) files
* [ ] support Rich Text Format (`.rtf`) files
* [ ] finish `spider.py`


#### Attention

The **sample** of `spider.py` use CNKI's kns55 platform to get related papers, though the sample is **unfinished**, abusing the kns55 platform may broke the ToS and EULA of CNKI.

Use these codes **at your own risk**.


#### License

This project is licensed under the [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html), for more information, see [LICENSE](LICENSE).
