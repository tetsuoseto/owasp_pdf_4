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

from PIL import Image
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen.canvas import Canvas # type: ignore
from reportlab.lib.pagesizes import A4, LETTER # type: ignore

def _set_proj_common_fields(cs: Dict[str, Any]):
    new_cs: Dict[str, Any] = {
        "doc_template_type": "custom",
        "doc_title_pivot.pt_x": 300, # temporary
        "doc_title_pivot.pt_y": 324,
        "doc_toc_title_pivot.pt_x": 72,
        "doc_toc_title_pivot.pt_y": 0,
        "chapter_pivot.pt_y": 32,
        "doc_title_font.line_alignment": "center",
        "doc_title_font.size": 40,
        "doc_title_font.line_pitch": 48,
        "doc_subtitle_font.size": 20, # 16
        "doc_subtitle_font.line_alignment": "center",
        "doc_toc_title_font.size": 24,
        "doc_toc_title_font.line_alignment": "center",
        "doc_site_name": "genai.owasp.org",
        "doc_site_url": "https://genai.owasp.org/",
        "chapter_font.line_alignment": "center",
        "chapter_font.color": "white",
        "chapter_font.size": 24,
        "section_font.size": 16,
        "doc_appendix_titles": [],
    }
    for key in new_cs:
        assert key in cs, \
            f"'{key}' is not defined in customizable styles."
    cs.update(new_cs)

def _set_lang_specific_fields(cs: Dict[str, Any], lang:str):
    if lang[:2] == "en":
        cs["doc_title"] = [
            "LLM AI Security &",
            "Governance Checklist"
        ]
        cs["doc_subtitles"] = [
            "",
            "",
            "",
            "From the OWASP Top 10 for LLM Applications Team",
            "",
            "",
            "Version: 1.1",
            "Published: April 10, 2024"
        ]
        cs["doc_toc_contents_title"] = "Table of Contents"
        cs["doc_toc_figures_title"] = "Figures"
        cs["doc_legal_notice"] = True
        cs["doc_legal_notice_words"] = [
            "The information provided in this document does not, and is" + \
                " not intended to, constitute legal advice.",
            "All information is for general informational purposes only.",
            "",
            "This document contains links to other third-party websites." + \
                " Such links are only for convenience",
            "and OWASP does not recommend or endorse the contents of the" + \
                " third-party sites.",
            "",
            "This project is licensed under the terms of the Creative " + \
                "Commons Attribution-ShareAlike 4.0 ",
            " International License. " + \
                "( https://creativecommons.org/licenses/by-sa/4.0/ )",
            "",
            "Revision History",
            "    2023-11-01  English  0.1  initial draft",
            "    2023-12-06  English  0.5  public draft",
            "    2024-02-15  English  0.9  pre-release draft",
            "    2024-02-19  English  1.0  public release v 1.0",
            "    2024-04-10  English  1.1  public release v 1.1"
        ]
    elif lang == "ja-JP":
        cs["doc_title"] = [
            "LLM AI サイバーセキュリティと",
            "ガバナンスのチェックリスト"
        ]
        cs["doc_subtitles"] = [
            "",
            "",
            "OWASP 大規模言語モデル",
            "アプリケーション リスク トップ10 チーム 監修",
            "",
            "",
            "",
            "",
            "2.0 版",
            "令和6年10月1日"
        ]
        cs["doc_toc_contents_title"] = "目 次"
        cs["doc_toc_figures_title"] = "図 表"
        cs["doc_legal_notice"] = True
        cs["doc_legal_notice_words"] = [
            "本書で提供される情報は、法的助言を構成するものではなく、また構成することを意図する",
            "ものでもありません。すべての情報は一般的な情報提供のみを目的としています。",
            "",
            "この文書には、他の第三者のウェブ・サイトへのリンクが含まれていますが、",
            "OWASPは、それら第三者のサイトのコンテンツを推奨または保証するものではありません。",
            "",
            "このプロジェクトは、クリエイティブ・コモンズ 表示 - 継承 4.0 国際 ライセンスの下でライセンスされています。",
            "https://creativecommons.org/licenses/by-sa/4.0/deed.ja",
            "",
            "改定履歴",
            "　　2023-11-01　英語版　0.1　initial draft",
            "　　2023-12-06　英語版　0.5　public draft",
            "　　2024-02-15　英語版　0.9　pre-release draft",
            "　　2024-02-19　英語版　1.0　public release v 1.0",
            "　　2024-04-10　英語版　1.1　public release v 1.1",
            "　　令和6年4月10日　日本語版　1.1",
            "　　2024-10-01　英語版　2.0　public release v 2.0",
            "　　令和6年10月1日　日本語版　2.0"
        ]

def _create_gov_chapter_page(paper_size: Tuple, paper_size_str: str,
        data_dir_path: Path, temp_dir_path: str):
    chapter_page_name: str = f"2_gov_chapter_{paper_size_str}.pdf"
    chapter_page_path = os.path.join(data_dir_path,
        "templates/page_pdfs", chapter_page_name)
    image_file_path = os.path.join(data_dir_path,
        "templates/image_parts/head_header.jpg")
    header_img = Image.open(image_file_path)
    img_width, img_height = header_img.size
    img_aspect = img_height / float(img_width)
    print_width = paper_size[0]
    print_height = print_width * img_aspect * 4 /5

    canvas = Canvas(chapter_page_path, pagesize=paper_size)
    canvas.drawImage(image_file_path, \
        0.0, paper_size[1] - print_height, \
        print_width, print_height
        )
    canvas.showPage()
    canvas.save()

def _merge_pdf(output_pdf, base_pdf, overlay_pdf):
    overlay = PdfReader(overlay_pdf).pages[0]
    base_page = PdfReader(base_pdf).pages[0]
    writer = PdfWriter()
    base_page.merge_page(overlay)
    writer.add_page(base_page)
    with open(output_pdf, "wb") as out_file:
        writer.write(out_file)
    writer.close()
    return output_pdf

def _create_gov_cover_page(paper_size: Tuple, paper_size_str: str,
        data_dir_path: Path, temp_dir_path: str):
    # Step 1: draw background image to blank page
    cover_page_name = f"1_gov_cover_{paper_size_str}.pdf"
    cover_page_path = os.path.join(data_dir_path,
        "templates/page_pdfs", cover_page_name)
    image_file_path = os.path.join(data_dir_path,
        "templates/image_parts/cover_background.jpg")
    bkgd_img = Image.open(image_file_path)
    canvas = Canvas(cover_page_path, pagesize=paper_size)
    canvas.drawInlineImage(image_file_path, 0.0, 0.0, \
        bkgd_img.size[0], paper_size[1])
    canvas.showPage()
    canvas.save()

    # Step 2: draw owasp image to blank page
    image_file_path = os.path.join(data_dir_path,
        "templates/image_parts/cover_owasp.png")

    owasp_pdf = os.path.join(temp_dir_path, "owasp.pdf")
    canvas = Canvas(owasp_pdf, pagesize=paper_size)
    canvas.drawImage(image_file_path, 0.0, 0.0, \
        paper_size[0], paper_size[1], mask = "auto")
    canvas.showPage()
    canvas.save()

    # Step 3: draw owasp logo image to blank page
    # pylint: disable=duplicate-code
    image_file_path = os.path.join(data_dir_path,
        "templates/image_parts/cover_logo.png")
    logo_img = Image.open(image_file_path)
    aspect_ratio = logo_img.size[1] / logo_img.size[0]
    owasp_logo_pdf = os.path.join(temp_dir_path, "owasp_logo.pdf")
    canvas = Canvas(owasp_logo_pdf, pagesize=paper_size)
    img_print_width = 200.0
    img_print_heigit = img_print_width * aspect_ratio
    canvas.drawImage(image_file_path, \
        paper_size[0] * 0.5 - (img_print_width/2.0), \
        paper_size[1] * 0.8, \
        img_print_width, img_print_heigit,
        mask = "auto")
    canvas.showPage()
    canvas.save()

    # Step 4: merge to cover page base
    _merge_pdf(cover_page_path, cover_page_path, owasp_pdf)
    _merge_pdf(cover_page_path, cover_page_path, owasp_logo_pdf)
    # pylint: enable=duplicate-code

def _create_gov_blank_page(paper_size: Tuple, paper_size_str: str,
        data_dir_path: Path, temp_dir_path: str, temp_type: str):
    assert temp_type in ["toc", "body"]
    temp_id: int = 4 if temp_type == "toc" else 3
    cover_page_name = f"{temp_id}_gov_{temp_type}_{paper_size_str}.pdf"
    cover_page_path = data_dir_path/"templates/page_pdfs"/cover_page_name
    canvas = Canvas(str(cover_page_path), pagesize=paper_size)
    canvas.showPage()
    canvas.save()

def _create_template_pdfs(proj_code, data_dir_path, temp_dir_path):
    paper_sizes = [LETTER, A4]
    for paper_size in paper_sizes:
        paper_size_str = "LETTER" if paper_size == LETTER else "A4"
        _create_gov_cover_page(paper_size, paper_size_str,
            data_dir_path, temp_dir_path)
        _create_gov_chapter_page(paper_size, paper_size_str,
            data_dir_path, temp_dir_path)
        _create_gov_blank_page(paper_size, paper_size_str,
            data_dir_path, temp_dir_path, "body")
        _create_gov_blank_page(paper_size, paper_size_str,
            data_dir_path, temp_dir_path, "toc")
    use_default_templates = False
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

    if proj_code != "GOV":
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
            "proj_dir": "llm-top-10-governance-doc",
            "styles": customizable_styles,
            "use_default_templates": use_default_templates,
            }
    return None

def _test():

    def get_cust_styles(lang):
        return {}

    release_date: str = "20240923"
    dont_care:str = ""
    my_proj_path = os.path.join(os.path.expanduser('~'),
        f"tetsuoseto_Origin/owasp_pdf_4/{release_date}")
    data_dir_path = Path(os.path.join(my_proj_path, "owasp_pdf_data_GOV"))
    proj_def_generator = register_project("GOV", ("en-ZZ",),
        data_dir_path, dont_care, get_cust_styles)
    for proj_def in proj_def_generator:
        assert proj_def["proj_code"] == "GOV"
        assert proj_def["lang"] == "en-ZZ"
        assert proj_def["proj_dir"] == "llm-top-10-governance-doc"
        assert isinstance(proj_def["styles"], dict)
    print("Test: success!!")

if __name__ == '__main__':
    _test()
