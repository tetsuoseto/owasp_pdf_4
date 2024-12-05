# OWASP PDF 4 Release Repository
## OWASP PDF 4.3.1 20241217 Update
### Supported projects: GOV, COE, IPS, LLM, ZZZ, RTG
### Project registration package
    - custom style json
    - document image files
    - template image files
    - plug-in Python script: owasp_pdf_register_<proj_code>_plugin.py

To install OWASP PDF 4.3.1 executable on your Mac,
1. `git clone` or [Download ZIP](https://github.com/tetsuoseto/owasp_pdf_4/archive/refs/heads/main.zip) of this repo (owasp_pdf_4) under any directory, e.g., `Playbook` on your desktop: `~/Desktop/Playbook`
2. Double Click dist_4.3.1_20241217 zip file to decompress it to `~/Desktop/Playbook/owasp_pdf_4/dist_4.3.1_20241217` folder
3. Open terminal window, `cd` to `~/Desktop/Playbook/owasp_pdf_4/dist_4.3.1_20241217` directory and run `shasum -a 256 owasp_pdf` to calculate the sha256 hash code of `owasp_pdf` executable. It should match `6babcfec3c21269f1eda61e40f8a6abb4715495169bbf9e459fc73c554387479`
4. Copy `owasp_pdf` executable file to `~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124`
    Note: [in case Mac complains that it's not downloaded from App Store](https://support.apple.com/guide/mac-help/if-an-app-is-not-from-the-mac-app-store-mh40620/11.0/mac/11.0))
5. `cd ~/Desktop/Playbook/owasp_pdf_4/BldEnv20241124`
6. Run `./owasp_pdf -r` in your Mac terminal window and verify the installation.
7. Run `./owasp_pdf -l LLM_en-US` in your Mac terminal window and verify the released PDF file is successfully built.

```
$ cd ~/Desktop/Playbook/owasp_pdf_4/dist_4.3.1_20241217
$ shasum -a 256 owasp_pdf
6babcfec3c21269f1eda61e40f8a6abb4715495169bbf9e459fc73c554387479  owasp_pdf
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

### Coming Soon:
    0. LLM Top 10 Localization Early Bird Sampler
       (partially machine-translated PDF's for all the registered languages)
       (zip file is stored under /owasp_pdf_4 in this repository)
    1. User's Guide
    2. Project Owner's Guide
    3. Registration Package Builder's Guide
Note: Archived owasp_pdf_3 ["Getting Started" ](https://github.com/tetsuoseto/owasp_pdf_4/blob/main/doc_archives/owasp_pdf_3/README.pdf) is equivalent to 1 + 2.

