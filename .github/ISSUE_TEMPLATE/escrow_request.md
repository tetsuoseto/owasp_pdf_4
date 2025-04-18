---
name: Escrow request
about: Initiate an escrow in the final review phase
title: 'Escrow Request:'
labels: 'escrow'
assignees: ''

---

**Project Code** (to be filled in by the requester)
One project code such as "LLM"

**Language Codes** (to be filled in by the requester)
One or more language codes such as "ar-SA, ja-JP, th-TH"

**Source Commit ID URL** (to be filled in by the requester)
unique SHA or hash for the commit of the source MD files, custom JSON, and image files.

example: https://github.com/johndow/llm_2025/commit/8d0cf83dca3b1c47e83da0d1ac5046376dd49071

directory structure example:
ar-SA
  ├── LLM00_Preface.md
  ├── LLM01_Chapter_01.md
  ├── LLM02_Chapter_02.md
  ├── LLM03_Chapter_03.md  
  └── baseline
      ├── custom_data_LLM_ar-SA.json
      └── images
          ├── image_000.jpeg
          └── image_001.png

**Escrow Manager** (to be filled in by the escrow manager if/when the request is accepted)
Slack ID to be assigned when the escrow request is accepted.



*Escrow Process Overview*

ESCROW PROCESS

  The project owner of the document (PDF) can “open escrow” when the owner deems the document (PDF) has reached “Final” status after “Release Candidate (RC)” status. The escrow is “time-based” -- the owner sets the time such as “48 hour escrow” at opening. Escrow condition is “no objections to publish the docu- ment.”
  If the condition is met when the specified time has passed, the document (PDF) status changes to “Final” and the escrow is "closed." If an objection is raised, the escrow is "cancelled" and the document (PDF) stays in RC status.
  In case of localization, the project owner opens escrow with the localized final RC PDF.
  Escrow request needs to be filed again when escrow is cancelled.

FAIR COLLABORATION RULE and PEER REVIEW
  *To be considered when escrow request is filed.*

  Localization can be started by one person, but strongly recommended to form a team of two or more mem- bers. The rule of thumb **fair collaboration rule** is that no more than half members can represent one organi- zation/company; for example, if two members work for the same company, two or more members should be invited from outside the company by the time to enter RC peer review. To invite additional collaborators, a recruiting message should be posted on slack, e.g., #project-top10-for-llm for one week. **Peer review** is required for localized RC PDF to be posted on the genai.owasp.org site. The project owner is to define a credit page format for the localization team to use in the PDF.
