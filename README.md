# OWASP PDF 4 Release Repository
## OWASP PDF OWASP PDF v4.6.0 20250530-164118 Update
### Supported projects: GOV, COE, IPS, LLM, ZZZ, RTG
### Project registration package
    - custom style json
    - document image files
    - template image files
    - plug-in Python script: owasp_pdf_register_<proj_code>_plugin.py

To install OWASP PDF 4.6.0 executable on your Mac,
1. `git clone` or [Download ZIP](https://github.com/tetsuoseto/owasp_pdf_4/archive/refs/heads/main.zip) of this repo (owasp_pdf_4) under any directory, e.g., `Playbook` on your desktop: `~/Desktop/Playbook`
2. Double Click dist_4.6.0_20250530 zip file to decompress it to `~/Desktop/Playbook/owasp_pdf_4/dist_4.6.0_20250530` folder
3. Open terminal window, `cd` to `~/Desktop/Playbook/owasp_pdf_4/dist_4.6.0_20250530` directory and run `shasum -a 256 owasp_pdf` to calculate the sha256 hash code of `owasp_pdf` executable. It should match `948ba00d31b4d294b7a3f4f6a450c09fdb163374130c62a7fd78d773ec96a0c0`
4. Copy `owasp_pdf` executable file to `~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124`
5. `cd ~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124`
    Note: [in case Mac complains that it's not downloaded from App Store](https://support.apple.com/guide/mac-help/if-an-app-is-not-from-the-mac-app-store-mh40620/11.0/mac/11.0))
6. Run `./owasp_pdf -v` in your Mac terminal window and verify the installation.
    Note: It takes a minute for owasp_pdf to set up the build environment.
7. Run `./owasp_pdf -l LLM_en-US` in your Mac terminal window and verify the released PDF file is successfully built.

```
$ cd ~/Desktop/Playbook/owasp_pdf_4/dist_4.6.0_20250530
$ shasum -a 256 owasp_pdf
948ba00d31b4d294b7a3f4f6a450c09fdb163374130c62a7fd78d773ec96a0c0  owasp_pdf
$ cp owasp_pdf ~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124/
$ cd ~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124
$ ./owasp_pdf -v
OWASP_PDF Version: OWASP PDF v4.6.0 20250530-164118
$ ./owasp_pdf -l LLM_en-US
*** Loaded 'owasp_pdf_register_LLM_plugin'
*** Processing LLM_en-US
    805 lines written to <your working directory>/owasp_pdf_4/BldEnv20241124/2_0_vulns/en-US/baseline/LLMAll_en-US.md
        43 page PDF created on <your working directory>/owasp_pdf_4/BldEnv20241124/2_0_vulns/en-US/baseline/LLMAll_en-US.pdf
    Processing time: 54 seconds
```

### OWASP PDF 4 Documentation: 2025-02-17 v1.0.0-Draft
    owasp_pdf_4/doc/OWASP_PDF_4.pdf

    1. Project Owner's Guide: RC - ready for review
    2. Plug-in Developers' Guide: W.I.P. (just a placeholder)
    3. Users' Guide: W.I.P. (copied the owasp_pdf_3 README as a starter)

Note: Archived owasp_pdf_3 README.pdf ["Getting Started" ](https://github.com/tetsuoseto/owasp_pdf_4/blob/main/doc_archives/owasp_pdf_3/README.pdf) is equivalent to 1 + 2.
