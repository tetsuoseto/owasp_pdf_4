# OWASP PDF 4 Release Repository
## 20240923 Update
### Supported projects: GOV, COE, IPS, LLM
### Project registration package
    - custom style json
    - document image files
    - template image files
    - plug-in Python script: owasp_pdf_register_<proj_code>_plugin.py

To install OWASP PDF 4.1 executable on your Mac,
1. `git clone` or [Download ZIP](https://github.com/tetsuoseto/owasp_pdf_4/archive/refs/heads/main.zip) of this repo under any directory, e.g., `Playbook` on your desktop: `~/Desktop/Playbook`
2. Visit [#owasp_pdf_users Slack channel](https://owasp.slack.com/archives/C07606V664W) and download `dist_4.1.0_20241027.zip` to `~/Desktop/Playbook` folder
3. Double Click the zip file to decompress it to `~/Desktop/Playbook/dist_4.1.0_20241027` folder
4. Open terminal window, `cd` to `~/Desktop/Playbook/dist_4.1.0_20241027` directory and run `shasum -a 256 owasp_pdf` to calculate the sha256 hash code of `owasp_pdf` executable. It should match `6f81deca1d9b70122a4b51fce91dfb723f302a06bb4405dd2e695fb58012eda5`
5. Copy `owasp_pdf` executable file to `~/Desktop/Playbook/owasp_pdf_4/20240923`
    Note: [in case Mac complains that it's not downloaded from App Store](https://support.apple.com/guide/mac-help/if-an-app-is-not-from-the-mac-app-store-mh40620/11.0/mac/11.0))
6. `cd ~/Desktop/Playbook/owasp_pdf_4/20240923`
7. Run `./owasp_pdf -r` in your Mac terminal window and verify the installation.

```
$ cd ~/Desktop/Playbook/dist_4.1.0_20241027
$ shasum -a 256 owasp_pdf
6f81deca1d9b70122a4b51fce91dfb723f302a06bb4405dd2e695fb58012eda5  owasp_pdf
$ cp owasp_pdf ~/Desktop/Playbook/owasp_pdf_4/20240923/
$ cd ~/Desktop/Playbook/owasp_pdf_4/20240923
$ ./owasp_pdf -r
OWASP_PDF Registered Languages:
  LLM: ar-SA be-BY bn-IN cs-CZ da-DK de-DE en-GB en-US en-ZZ es-ES es-MX et-EE fi-FI fr-CA fr-FR he-IL hi-IN hu-HU it-IT ja-JP ko-KR ...

```

### Coming Soon:
    1. User's Guide
    2. Project Owner's Guide
    3. Registration Package Builder's Guide
Note: Existing ["Getting Started" ](https://github.com/Setotet/owasp_pdf/blob/main/README.pdf) is equivalent to 1 + 2.

## Early Adapter's Playbook

### Target Scenario
You're going to fine tune "LLM09_Misinformation.md". Already installed OWASP PDF 4.1 executable following the instruction above.

- Make sure no files exist on `owasp_pdf_4/20240923/2_0_vulns`
- Retrieve `LLM09_Misinformation.md` file from [this PR](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/pull/450/files#diff-08aeade4a5c5613075ba3a2bcbc53b8248b037d2950cfadc44ef0308fcef7b5c) and place it under "2_0_vulns". The markdown file has been already fine-tuned from [the original LLM09_Misinformation.md](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM09_Misinformation.md). The PR on github might be handy to compare the two MD files and see exactly what's changed.
- In the terminal window, change directory to ~/Desktop/Playbook/owasp_pdf_4/20240923. You have owasp_pdf executable file there.
- To create an initial "en-US" directory, run it as follows:
```
$ ./owasp_pdf -l LLM_en-US
*** Loaded 'owasp_pdf_register_LLM_plugin'
*** Processing LLM_en-US
    71 lines written to <your working directory>/owasp_pdf_4/20240923/2_0_vulns/en-US/baseline/LLMAll_en-US.md
        7 page PDF created on <your working directory>/owasp_pdf_4/20240923/2_0_vulns/en-US/baseline/LLMAll_en-US.pdf
    Processing time: 5 seconds
```
- owasp_pdf will take approx. 20 seconds to set up the working environment every time you run it
- Three files will be created as follows:
```
en-US
└── baseline
    ├── LLMAll_en-US.md
    ├── LLMAll_en-US.pdf
    ├── custom_data_LLM_en-US.json
    └── images

2 directories, 3 files
```
- Open LLMAll_en-US.pdf and see what your first PDF looks like.
- Since we focus on "LLM09_Misinformation.md" fine tuning, make two changes to `custom_data_LLM_en-US.json` and remove title page and legal notice page.  Keep TOC because we want to make sure the LLM09 structure is properly listed on the TOC.
>NOTE: There are many other customizable typographical parameters in custom_data_LLM_en-US.json such as font size, line spacing, as well as document title and legal notice contents.  All of them are managed at the LLM project level, so, we keep them as-is and focus on markdown text fine-tuning. 
```
    "doc_cover": false,
...
    "doc_legal_notice": false,
...
    "doc_toc": true,
    "doc_authors_toc": true,
```
- Re-run **./owasp_pdf -l LLM_en-US** and make sure the title page and the legal notice page are gone.
```
$ ./owasp_pdf -l LLM_en-US
*** Loaded 'owasp_pdf_register_LLM_plugin'
*** Processing LLM_en-US
    71 lines written to <your working directory>/owasp_pdf_4/20240923/2_0_vulns/en-US/baseline/LLMAll_en-US.md
        5 page PDF created on <your working directory>/owasp_pdf_4/20240923/2_0_vulns/en-US/baseline/LLMAll_en-US.pdf
    Processing time: 4 seconds
```
- Note: *5 page PDF created* - two pages less than the first build.

> Quick sheet of Markdown-to-OWASP PDF rendering features
> 
> 1. '##' - chapter; starts the chapter title page, '###' - section, '####' - block; they are listed on TOC.  '####' are heavily used in this fine-tuning scenario instead of **BOLD**.
> 2. (two space characters) - paragraph tab; A text line in MD file is rendered as a paragraph in PDF.
> 3. Linked text (blue text) is supported not at character level but at MD text line level or paragraph level in PDF
> 4. Ordered items should be explicitly numbered.

**Quiz**: Block title **8. Training and Education** is rendered on page 2 but the block contents are separated to page 3.  The block title placed at the end of a page is called "orphan." How can we correct the 'orphan'?

**Answer**: Add an empty line before the block title in the markdown file and send it to the next page.


**Quiz**: Another orphan - section title **Related Frameworks and Taxonomies** is rendered on page 3 but the section contents are separated to page 4. How can we correct it?

**Answer**: Two ways to correct the orphan:
1. Add one empty line before the section title and send it to page 4.
2. The paragraph in the section contents seems unnecessary.  Remove it to send ` AML.T0048.002 - Societal Harm MITRE ATLAS` to page 3. If we need more space, maybe, we can remove the empty space before **Scenario #2**.  Still not enough? Can we remove the line space after **Related Frameworks and Taxonomies**?  That makes the structure one-off, but might be better than almost empty page.  Maybe, we can edit the body text somewhere and squeeze one line? 


**Quiz**: Header says "OWASP Top 10 for LLM Applications v2.0"  v2.0 should be v2025 in this release.  How can we change it?

**Answer**: The header text is set in the custom json file.  Edit "doc_header"  entry of `custom_data_LLM_en-US.json` under `20240923/2_0_vulns/en-US/baseline` directory.  Note that `custom_data_LLM_en-US.json` will be corrected at the LLM project level, so no need to make this change at chapter (vuln entry) level.

