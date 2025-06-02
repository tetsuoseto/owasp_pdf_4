## Document Development and Release Process

### Overview

For both English original and localized versions, the authoring process goes as outlined in the Figure 1: Document Development and Release Process below:

![Figure 1: Document Development and Release Process](images/project_asset_dev_and_rel_process.png)

##### Figure 1: Document Development and Release Process


Core value is created in the contents development phase; i.e, original (English) contents creation from the scratch or translation of the original English contents. In OWASP PDF 4 PDF authoring process, it is technically done by editing markdown files (simple text files) collaboratively.

Final Review comes after the review and tuning of the contents development to ensure that PDF is professionally formatted to maximize and protect the content value as well as the GenAI brand value, e.g., the cover page with GenAI Security Project logo.

In Figure 1, "Ideation, Initial Contribution", "Contribution and Refinement", and "Review and Tuning" map to the contents creation. "Final Review" maps to the escrow. Final Review (escrow) comes after completion of the contents creation. They are clearly separated in Document Development and Release Process.

Speaking of accountability, the entry teams own the content of the original English PDFs. Translation teams own the content of localized PDFs. The publishing team owns the formatting for both.

The term "escrow" in OWASP PDF 4 process emanated from "escrow in selling/buying house." Let's recap what the escrow is in the real estate market first. It's a good analogy and helps get a grasp on the OWASP PDF 4 Escrow Process.

## Escrow in Selling/Buying House

### What is Escrow in Selling/Buying House?

In real estate, escrow is a process where a neutral third party (like a title company) holds funds and documents related to a property sale until all conditions of the sale are met.

There are symmetric roles between OWASP PDF 4 Escrow Process and the escrow in selling/buying house:

>lightcyan  
>lightcyan|||||mb                         OWASP PDF 4  :  REAL ESTATE MARKET
>lightcyan|||||mr                    ────────────────────────────────────────────
>lightcyan|||||mr                            PDF File  :  Property/House
>lightcyan|||||mr                      Document Owner  :  Seller
>lightcyan|||||mr                         Translators  :  Buyer
>lightcyan|||||mr                    Authorized Proxy  :  Real Estate Broker
>lightcyan|||||mr                      Escrow Manager  :  Title Company
>lightcyan  

### What does the Title Company do?

They open and manage the escrow account, hold funds like the down payment and earnest money, and ensure that all documents are properly executed and recorded.

### Why use a Title Company for Escrow?

Title companies are experienced in handling these transactions and can ensure a smooth and secure process for both the buyer and seller.

#### Benefits of using a Title Company
- Neutral Party: They act as an impartial third party, ensuring the transaction is fair for both parties. 
- Expertise: They are familiar with the legal and regulatory requirements of real estate transactions. 
- Security: They provide a secure and transparent process for managing funds and documents. 

### What does the Real Estate Broker do for sellers and buyers?

A real estate broker acts as an intermediary in real estate transactions, helping both buyers and sellers navigate the process. They can represent either a buyer or seller, but not both. Brokers provide guidance, advice, and professional services to ensure a smooth and successful transaction.

#### For Sellers:
- Listing and Marketing: A seller's broker lists the property on the Multiple Listing Service (MLS) and uses various marketing strategies to attract potential buyers. 
- Negotiation: They negotiate with potential buyers on behalf of the seller, aiming for a price and terms that are mutually agreeable. 
- Documentation and Compliance:They help prepare and manage the necessary paperwork, ensuring the transaction complies with legal and ethical standards. 
- Closing Assistance:They assist with the closing process, including coordinating with other professionals like attorneys and title companies. 

#### For Buyers:

- Property Search: A buyer's broker helps find properties that meet the buyer's needs and preferences. 
- Offer Preparation and Negotiation:They prepare and submit offers to purchase a property and negotiate the terms with the seller's broker. 
- Inspection Coordination:They assist with coordinating home inspections and addressing any issues that arise. 
- Financing Guidance:They can provide guidance on financing options and help connect buyers with lenders. 
- Closing Assistance:They guide buyers through the closing process, ensuring a smooth transition into their new home. 

Source:
  https://www.rocketmortgage.com/
  https://ctccal.com/blog/can-a-title-company-handle-escrows-in-california
  https://www.superiorschoolnc.com/
  https://www.indeed.com/
  https://www.investopedia.com/
  https://greatcoloradohomes.com/

## Escrow Process Work Flow

Let's think about the original English document development first. The document owner, or a proxy appointed by he document owner, can “open escrow” by submitting "escrow request" when the owner deems the document has reached “Final” status after “Release Candidate (RC)” status. The escrow is “time-based” -- the owner sets the time such as “48 hour escrow” at opening. Escrow condition is “no objections to publish the document.”

If the condition is met when the specified time has passed, the escrow is automatically "closed" and the document status changes to “Final.”  If an objection is raised, the escrow is automatically "cancelled" and the document stays in RC status. Escrow request needs to be filed again to re-open an escrow.

### English Escrow Process

![Figure 2: How Top10 for LLM 2025 English Escrow Process was Run](images/fig2_english_2025.png)

##### Figure 2: Top10 for LLM 2025 English Escrow Process

"Top 10 for LLM 2025 English" escrow was managed in Nov. 2024. After long content development (markdown files) effort by each entry team (#team-llm-* channel), the document owner sent a request to the owasp_pdf team on 10/29/24 to finalize PDF and publish the Top 10 for LLM 2025.

The escrow manager was immediately appointed. In addition, the document owner requested the escrow manager to fine-tune the contents as well as formatting. We needed this "Review and Tuning" or "integration" in the following two weeks because the entry development (LLM01 - LLM10) was widely distributed.

The escrow manager fine-tuned the formatting, created a Final RC PDF and announced a 48-hour escrow on 11/13/24 to the project core team channel sharing the Final RC, which still has W.I.P. watermark. On the same day, one oversight detected and reported by a member of the project core team. The escrow was immediately cancelled and sent back to the escrow requester who quickly corrected and requested to reopen an escrow. The escrow manager created Final RC 2 PDF and opened the second escrow. After two more cancellations/re-openings, 48 hours passed with no objections and the escrow was closed on 11/17/24. The escrow manager created and sent the publish-ready PDF to the GenAI site management team on 11/17/24. The GenAI site management team immediately posted the Release PDF to the GenAI site. 

### Escrow Process for Localized Versions

For localized versions, the challenge to the document owner is multiplied because there are multiple languages and for each language, multiple translators are involved.  Two resolutions:

1. The document owner appoints a proxy who coordinates multiple languages and translators and send "escrow request" for 2 or more languages in one request. (Recommended)

2. For each language, the document owner appoints a translator as a proxy who is authorized to submit "escrow request" of one language. (One-off High Priority Exception Only)























##$ Case 1 - Escrow Request Submission by Authorized Proxy
### (Recommended)

![Figure 3: Escrow Request Submission by Authorized Proxy](images/fig3_by_authorized_proxy.png)

##### Figure 3: Case 1 - Escrow Request Submission by Authorized Proxy



















##$ Case 2 - Escrow Request Submission by Individual Translator
### (One-off High Priority Exception Only)

![Figure 4: Case 2 - Escrow Request Submission by Individual Translator](images/fig4_by_individual_translator.png)

##### Figure 4: Case 2 - Escrow Request Submission by Individual Translator

## Escrow Request Template

Escrow Request on the owasp_pdf_4 github repository: https://github.com/tetsuoseto/owasp_pdf_4/issues

>lightcyan  
>lightcyan|||||hb Project Code: (to be filled in by the requester)
>lightcyan    One project code such as "LLM"
>lightcyan  
>lightcyan|||||hb Language Codes: (to be filled in by the requester)
>lightcyan    One or more language codes such as "ar-SA, ja-JP, th-TH"
>lightcyan  
>lightcyan|||||hb Source Commit ID URL: (to be filled in by the requester)
>lightcyan    unique SHA or hash for the commit of the source MD files, custom JSON, and image files.
>lightcyan    example: https://github.com/johndoe/llm_2025/commit/8d0cf83dca3b1c47e83da0d1ac5046376dd49071
>lightcyan  
>lightcyan|||||br    directory structure example:
>lightcyan  
>lightcyan|||||mr    ar-SA
>lightcyan|||||mr      ├── LLM00_Preface.md
>lightcyan|||||mr      ├── LLM01_Chapter_01.md
>lightcyan|||||mr      ├── LLM02_Chapter_02.md
>lightcyan|||||mr      ├── LLM03_Chapter_03.md  
>lightcyan|||||mr      └── baseline
>lightcyan|||||mr          ├── custom_data_LLM_ar-SA.json
>lightcyan|||||mr          └── images
>lightcyan|||||mr              ├── image_000.jpeg
>lightcyan|||||mr              └── image_001.png
>lightcyan  
>lightcyan|||||hb Escrow Manager: (to be filled in by the escrow manager if/when the request is accepted)
>lightcyan    Slack ID to be assigned when the escrow request is accepted.
>lightcyan  
> 
