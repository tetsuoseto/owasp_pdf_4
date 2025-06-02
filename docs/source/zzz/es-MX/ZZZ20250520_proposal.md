## Localization Final Review

### Responsibility

- Translation team is responsible for text content, i.e., translation of markdown text files and the parameter file (custom JSON)
- The owasp pdf 4 team is responsible for PDF formatting.
- Brand Manager owns template design, e.g, GenAI Security Project blue/yellow/gray templates.

### Localization Steps

#### Step 1. Translation

Translation team translate and review the markdown files and the parameter file (custom JSON) on #team-llm-translations and sub-channels.
>lightcyan|||||br  owned by: Translation team
>lightcyan|||||br  slack channels: #team-llm-translations and #team-llm-translations-**

#### Step 2. PDF Format Tuning

The two teams run the Final Review together on #owasp_pdf_users channel and agree on the completion of PDF format tuning.
>lightcyan|||||br  owned by: owasp_pdf_4 team
>lightcyan|||||br  slack channel: #owasp-pdf-users

#### Step 3. Watermark Removal

Translation team remove the watermark.
>lightcyan|||||br  owned by: Translation team
>lightcyan|||||br  slack channels: #team-llm-translations and #team-llm-translations-**

#### Step 4. Publish

Translation team send the watermark-removed PDF to the GenAI site maintenance team for posting. As of May 20, 2025, the site maintainer is Gotomarker (web contractor).
>lightcyan|||||br  owned by: Translation team
>lightcyan|||||br  slack channels: #team-llm-translations and #team-llm-translations-**

Appendix-1: Localization Steps on Doc Process shows the mapping of the localization steps on the Document Development and Release Process Guideline.


## Watermark Removal and Brand Protection

![brand value](images/brand_value.png)

Brand Manager owns the brand, i.e. the template. Document owners do not own the brand. As you see on the genai.owasp.org site, there are many PDF files standing out with the "GenAI Security Project" brand (color: blue, yellow, or gray). Some were built using OWASP PDF 4; others were built with other methods.

Brand usually needs to be protected; for example, the brand manager wants to avoid "modern_blue" cover page used in random documents everywhere, or a certain document with the brand updated every time one typo is corrected. Such usage would damage the brand integrity. OWASP PDF 4 has all the GenAI Security Project brand templates built-in.

OWASP PDF 4 also has "free/un-protected" template called "blank." With the "blank" template, the user can attach/remove W.I.P watermark freely. For example, you can use the "blank" template for your personal PDF authoring. OWASP PDF 4 is public domain software licensed under BSD-3.





### Brand Protection Scheme

>lightcyan  
>lightcyan|||||mb   TEMPLATE TYPE   MODE              CODE
>lightcyan|||||mr  ═══════════════════════════════════════════════════════════════════════════
>lightcyan|||||mr   blank           no protection     n/a
>lightcyan|||||mr   modern_blue     soft protection   TBD by Brand Manager and shared with
>lightcyan|||||mr                                     Designated Brand Controller if appointed
>lightcyan|||||mr   custom          hard protection   default for hard protection
>lightcyan|||||mr   ...
>lightcyan  

>lemonchiffon  
>lemonchiffon  The code is a random sequence of small/capital/digit characters and chosen by the brand manager, not by the owasp_pdf_4 maintainer. In case the brand manager designates somebody (Designated Brand Controller), the brand manager is to pass the code to DBC directly. The owasp_pdf_4 maintainer needs to know the code only to implement the scheme in owasp_pdf_4. The owasp_pdf_4 maintainer never divulges the code because anybody who knows the code can remove the watermark.
>lemonchiffon  

### Brand Protection Mode: NO, SOFT, or HARD

#### No Protection
Currently, "blank" template is the only template that belongs to "no protection" mode group. "doc_watermark" parameter in the custom JSON parameter file can be set True or False by the user to enable or disable the watermark.

#### Soft Protection
"doc_watermark" parameter in the custom JSON parameter file is used in PDF generation when "--brand" option is used. The TYPE, MODE, and CODE parameters must match with what Brand Manager defined. Freeze/Thaw step (see Hard Protection below) is not applied. When "--brand" option is not used, "doc_watermark" parameter in the custom JSON is not used.

#### Hard Protection
In addition to the steps for the soft protection, Freeze/Thaw step is to be done. Freeze/Thaw step goes as follows: After the PDF Format Tuning is completed, the markdown files, the custom JSON parameter file, and the output PDF are "frozen" by the the owner of the PDF Format Tuning step. The frozen PDF shows the watermark. By freezing the files, the brand is strictly protected; the translation team and the owasp_pdf_4 team are assured that the frozen files were reviewed and agreed by the two teams. "owasp_pdf --brand" command is used with the frozen set of files to thaw the frozen files (remove the watermark).






### Command Line to Remove Watermark

>lightcyan  
>lightcyan|||||mb   ./owasp_pdf --brand TYPE.MODE.CODE -l PROJ_LANG
>lightcyan  
>lightcyan|||||br       where
>lightcyan|||||br         TYPE: modern_blue, modern_yellow, blank, classic, ...
>lightcyan|||||br         MODE: soft or hard
>lightcyan|||||br         CODE: random sequence of small, capital letters and digits to be defined,
>lightcyan|||||br                   and shared with Designated Brand Controller if appointed, by Brand Manager 
>lightcyan|||||br         PROJ: LLM, IPS, GOV, ...
>lightcyan|||||br         LANG: de-DE, ar-SA, th-TH, ...
>lightcyan  
>lightcyan|||||br   for example,
>lightcyan|||||mb    ./owasp_pdf --brand modern_blue.soft.85FgUL57TrsP -l LLM_de-DE
>lightcyan  

