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
from pdb import set_trace # pylint: disable=unused-import

def _set_proj_common_fields(cs: Dict[str, Any]):
    cs["doc_title_pivot.pt_y"] = 250
    cs["doc_title_font.size"] = 40
    cs["doc_title_font.line_pitch"] = 48
    cs["doc_subtitle_font.size"] = 20
    cs["doc_subtitle_font.line_pitch"] = 24
    cs["chapter_font.color"] = "white"
    cs["doc_appendix_titles"] = []

def _set_lang_specific_fields(cs: Dict[str, Any], lang:str):
    cs["doc_title"] = [
        "LLM and Gen AI Security",
        "Center of Excellence",
        "(CoE) Guide",
    ]
    cs["doc_subtitles"] = [
        "",
        "",
        "",
        "From the OWASP Top 10 for LLM",
        "Applications Team",
        "",
        "",
        "",
        "",
        "Version: 0.5",
        "Early Draft Published for Feedback: July 12, 2024",
    ]
    cs["doc_legal_notice_words"] = [
        "The information provided in this document does not," + \
            " and is not intended to,",
        "constitute legal advice. All information is for general " + \
            "informational purposes only.",
        "",
        "This document contains links to other third-party websites.",
        "Such links are only for convenience and OWASP does not" + \
            " recommend or endorse",
        "the contents of the third-party sites.",
        "",
        "",
        "LICENSE AND USAGE",
        "",
        "This document is licensed under Creative Commons, CC BY-SA 4.0",
        "You are free to:",
        "  Share — copy and redistribute the material in any medium" + \
            " or format",
        "  Adapt — remix, transform, and build upon the material for" + \
            " any purpose, even commercially.",
        "    under the following terms:",
        "    Attribution — You must give appropriate credit, provide" + \
            " a link to the license, and indicate",
        "      if changes were made. You may do so reasonably, but not" + \
            " in any way that suggests",
        "      the licensor endorses you or your use.",
        "    Attribution Guidelines - must include the project name" + \
            " and the name of the asset Referenced.",
        "      OWASP Top 10 for LLMs - LLM AI Security Center of" + \
            " Excellence (CoE) Guide",
        "      OWASP Top 10 for LLMs - LLM AI Security Center of" + \
            " Excellence Guide",
        "      OWASP Top 10 for LLMs - LLM AI Security CoE Guide",
        "    ShareAlike — If you remix, transform, or build upon " + \
            "the material, you must distribute",
        "      your contributions under the same license as the original.",
        "https://creativecommons.org/licenses/by-sa/4.0/legalcode",
        "",
        "",
        "REVISION HISTORY",
        "",
        "    2024-05-15  0.1  Scott Clinton  Initial Outline Draft",
        "    2024-07-02  0.2  Scott Clinton, Updated with initial comments",
        "                                 Sandy Dunn, Team",
        "    2024-07-10  0.5  Open  Early draft, open for comment and input",
    ]
    cs["doc_header"] = "LLM and Gen AI Security Center of Excellence Guide"
    cs["doc_toc_contents_title"] = "Contents"
    cs["doc_toc_figures_title"] = "Figures"

def _create_template_pdfs(proj_code, data_dir_path, temp_dir_path):
    use_default_templates = True
    return use_default_templates

# register_project does two things:
#   1. create three template PDFs and store them under data directory
#   2. set the PDF styles
#
# proj_code: for example, "OLM"
# lang_codes: tuple of languages, for example ["en-US"]
# data_dir_path: full path to data directory "owasp_pdf_data_OLM"
# get_customizable_styles: callback function
# temp_dir_path: temporary directory path
def register_project(proj_code: str, lang_codes: Tuple[str, ...],
        data_dir_path:Path, temp_dir_path: str, get_customizable_styles):

    if proj_code != "COE":
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
            "proj_dir": "coe",
            "styles": customizable_styles,
            "use_default_templates": use_default_templates,
            }
    return None

def _test():

    def get_cust_styles(lang):
        # define chapter_font.size to avoid undefined key error
        return {"chapter_font.size": 999}

    dont_care:str = ""
    my_proj_path = os.path.join(os.path.expanduser('~'), "Setotet_Origin/" + \
        "www-project-top-10-for-large-language-model-applications/")
    data_dir_path = Path(os.path.join(my_proj_path, "owasp_pdf_data_COE"))
    proj_def_generator = register_project("COE", ("en-ZZ",),
        data_dir_path, dont_care, get_cust_styles)
    for proj_def in proj_def_generator:
        assert proj_def["proj_code"] == "COE"
        assert proj_def["lang"] == "en-ZZ"
        assert proj_def["proj_dir"] == "coe"
        assert isinstance(proj_def["styles"], dict)
        assert proj_def["styles"]["chapter_font.size"] == 999
    print("Test: success!!")

if __name__ == '__main__':
    _test()
