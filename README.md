# OWASP PDF 4 Release Repository
## OWASP PDF v4.4.1 20250126-131847 Update
### Supported projects: GOV, COE, IPS, LLM, ZZZ, RTG
### Project registration package
    - custom style json
    - document image files
    - template image files
    - plug-in Python script: owasp_pdf_register_<proj_code>_plugin.py

To install OWASP PDF 4.4.1 executable on your Mac,
1. `git clone` or [Download ZIP](https://github.com/tetsuoseto/owasp_pdf_4/archive/refs/heads/main.zip) of this repo (owasp_pdf_4) under any directory, e.g., `Playbook` on your desktop: `~/Desktop/Playbook`
2. Double Click dist_4.4.1_20250126 zip file to decompress it to `~/Desktop/Playbook/owasp_pdf_4/dist_4.4.1_20250126` folder
3. Open terminal window, `cd` to `~/Desktop/Playbook/owasp_pdf_4/dist_4.4.1_20250126` directory and run `shasum -a 256 owasp_pdf` to calculate the sha256 hash code of `owasp_pdf` executable. It should match `848fced757611a61abcfd320d51e972d0d544114b4a092af581116d57df48c17`
4. Copy `owasp_pdf` executable file to `~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124`
    Note: [in case Mac complains that it's not downloaded from App Store](https://support.apple.com/guide/mac-help/if-an-app-is-not-from-the-mac-app-store-mh40620/11.0/mac/11.0))
5. `cd ~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124`
6. Run `./owasp_pdf -r` in your Mac terminal window and verify the installation.
7. Run `./owasp_pdf -l LLM_en-US` in your Mac terminal window and verify the released PDF file is successfully built.

```
$ cd ~/Desktop/Playbook/owasp_pdf_4/dist_4.4.1_20250126
$ shasum -a 256 owasp_pdf
848fced757611a61abcfd320d51e972d0d544114b4a092af581116d57df48c17  owasp_pdf
$ cp owasp_pdf ~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124/
$ cd ~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124
$ ./owasp_pdf -r
OWASP_PDF Registered Languages:
  LLM: ar-SA be-BY bn-IN cs-CZ da-DK de-DE en-GB en-US en-ZZ es-ES es-MX et-EE fa-IR fi-FI fr-CA fr-FR he-IL hi-IN hu-HU it-IT ja-JP ko-KR ...
$ ./owasp_pdf -l LLM_en-US
*** Processing LLM_en-US
    804 lines written to <your working directory>/owasp_pdf_4/BldEnv20241124/2_0_vulns/en-US/baseline/LLMAll_en-US.md
        42 page PDF created on <your working directory>/owasp_pdf_4/BldEnv20241124/2_0_vulns/en-US/baseline/LLMAll_en-US.pdf
    Processing time: 44 seconds
```

### OWASP PDF 4 Documentation: 2025-01-25 v1.0.0-Draft
    owasp_pdf_4/doc/OWASP_PDF_4.pdf

    1. Project Owner's Guide: RC - ready for review
    2. Plug-in Developers' Guide: W.I.P. (just a placeholder)
    3. Users' Guide: W.I.P. (copied the owasp_pdf_3 README as a starter)

Note: Archived owasp_pdf_3 README.pdf ["Getting Started" ](https://github.com/tetsuoseto/owasp_pdf_4/blob/main/doc_archives/owasp_pdf_3/README.pdf) is equivalent to 1 + 2.

