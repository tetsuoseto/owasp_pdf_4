#!/usr/local/bin/python
# pylint: disable=invalid-name

"""
BSD 3-Clause License

Copyright (c) 2024, Tetsuo Seto

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import os.path
from pathlib import Path
from typing import Any, Dict, Tuple

def _set_proj_common_fields(cs: Dict[str, Any]):
    cs["doc_template_type"] = "blank"
    cs["doc_title"] = [

        "",
        "",
        "Lorem Ipsum"
    ]
    cs["doc_title_pivot.pt_x"] = 300
    cs["doc_title_pivot.pt_y"] = 200
    cs["doc_toc_title_pivot.pt_x"] = 72
    cs["doc_toc_title_pivot.pt_y"] = 72  # add 15 for bi-di for optimal result
    cs["doc_subtitles"] = [
        "",
        "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet",
        "consectetur, adipisci velit...",
        "There is no one who loves pain itself, who seeks after it",
        "and wants to have it, simply because it is pain..."
    ]
    cs["doc_header"] = "Lorem Ipsum"
    cs["doc_header_pivot.pt_x"] = 72
    cs["doc_header_pivot.pt_y"] = 36
    cs["doc_legal_notice_words"] = [
        "Text in this document was copied from https://www.lipsum.com/ and",
        "the intellectual right of the text belongs to lipsum.com.",
        "Privacy policy of lipsum.com is on https://www.lipsum.com/privacy.",
        "",
        "The information provided in this document does not, and" + \
            " is not intended to, constitute",
        " legal advice. All information is for general informational" + \
            " purposes only.",
        "",
        "This project is licensed under the terms of the Creative Commons" + \
            " Attribution-ShareAlike 4.0",
        "International License.  ( https://creativecommons.org/" + \
            "licenses/by-sa/4.0/ )",
        "",
        "Revision History",
        "    2024-09-01  English  0.1  initial draft"
    ]
    cs["doc_title_font.size"] = 50
    cs["doc_title_font.line_pitch"] = 55
    cs["doc_title_font.line_alignment"] = "center"
    cs["doc_subtitle_font.size"] = 14
    cs["doc_subtitle_font.line_pitch"] = 26.4
    cs["doc_subtitle_font.line_alignment"] = "center"
    cs["doc_toc_title_font.size"] = 24
    cs["doc_toc_title_font.line_alignment"] = "center"
    cs["chapter_pivot.pt_y"] = 67.7
    cs["chapter_font.color"] = "black"
    cs["header_font.color"] = "black"
    cs["doc_appendix_titles"] = [
        "Appendix 1: OWASP PDF Document Model (Title Page)",
        "Appendix 2: OWASP PDF Document Model (Chapter Page)",
        ]
    cs["doc_sponsor_page_titles"] = [
        "OWASP Top 10 for LLM Applications Project Sponsors and Supporters",
        "OWASP Top 10 for LLM Applications Project Supporters",
        ]

def _set_lang_specific_fields(cs: Dict[str, Any], lang:str):
    pass

def _create_template_pdfs(proj_code, data_dir_path, temp_dir_path):
    use_default_templates = True
    return use_default_templates

# register_project does two things:
#   1. create three template PDFs and store them under data directory
#   2. set the PDF styles
#
# proj_code: for example, "IPS"
# lang_codes: tuple of languages, for example ["en-US"]
# data_dir_path: full path to data directory such as "owasp_pdf_data_IPS"
# get_customizable_styles: callback function
def register_project(proj_code: str, lang_codes: Tuple[str, ...],
        data_dir_path: Path, temp_dir_path: str, get_customizable_styles):

    if proj_code != "IPS":
        return None

    use_default_templates = _create_template_pdfs(
        proj_code, data_dir_path, temp_dir_path)
    for lang in lang_codes:
        customizable_styles: Dict[str, Any] = get_customizable_styles(lang)
        _set_proj_common_fields(customizable_styles)
        _set_lang_specific_fields(customizable_styles, lang)
        yield {
            "proj_code": proj_code,
            "lang": lang,
            "proj_dir": "ips",
            "styles": customizable_styles,
            "use_default_templates": use_default_templates,
            }
    return None

def _test():

    def get_cust_styles(lang):
        return {}

    release_date: str = "20240923"
    dont_care = ""
    my_proj_path = os.path.join(os.path.expanduser('~'),
        f"tetsuoseto_Origin/owasp_pdf_4/{release_date}")
    data_dir_path = Path(os.path.join(my_proj_path, "owasp_pdf_data_IPS"))
    proj_def_generator = register_project("IPS", ("en-ZZ",),
        data_dir_path, dont_care, get_cust_styles)
    for proj_def in proj_def_generator:
        assert proj_def["proj_code"] == "IPS"
        assert proj_def["lang"] == "en-ZZ"
        assert proj_def["proj_dir"] == "ips"
        assert isinstance(proj_def["styles"], dict)
    print("Test: success!!")

if __name__ == '__main__':
    _test()
