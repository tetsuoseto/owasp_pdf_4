## Brev från projektledarna

OWASP Top 10 for Large Language Model Applications startade 2023 som ett community-drivet försök att lyfta fram och ta itu med säkerhetsproblem som är specifika för AI-applikationer. Sedan dess har tekniken fortsatt att spridas över branscher och applikationer, och det har även de därmed förknippade riskerna. I takt med att LLM:er är djupare inbäddade i allt från kundinteraktioner till intern verksamhet, upptäcker utvecklare och säkerhetspersonal nya sårbarheter – och sätt att motverka dem.

2023 års lista var en stor framgång för att öka medvetenheten och bygga en grund för säker LLM-användning, men vi har lärt oss ännu mer sedan dess. I den här nya 2025-versionen har vi arbetat med en större, mer mångsidig grupp av bidragsgivare över hela världen som alla har hjälpt till att forma den här listan. Processen innefattade brainstormsessioner, röstning och verklig feedback från yrkesverksamma inom LLM-applikationssäkerhet, antingen genom att bidra eller förfina dessa bidrag genom feedback. Varje röst var avgörande för att göra denna nya release så grundlig och praktisk som möjligt.

### What’s New in the 2025 Top 10

The 2025 list reflects a better understanding of existing risks and introduces critical updates on how LLMs are used in real-world applications today. For instance, **Unbounded Consumption** expands on what was previously Denial of Service to include risks around resource management and unexpected costs—a pressing issue in large-scale LLM deployments.

The **Vector and Embeddings** entry responds to the community’s requests for guidance on securing Retrieval-Augmented Generation (RAG) and other embedding-based methods, now core practices for grounding model outputs.

We’ve also added **System Prompt Leakage** to address an area with real-world exploits that were highly requested by the community. Many applications assumed prompts were securely isolated, but recent incidents have shown that developers cannot safely assume that information in these prompts remains secret.

**Excessive Agency** has been expanded, given the increased use of agentic architectures that can give the LLM more autonomy.  With LLMs acting as agents or in plug-in settings, unchecked permissions can lead to unintended or risky actions, making this entry more critical than ever.

### Går framåt

Liksom själva tekniken är den här listan en produkt av open source-gemenskapens insikter och erfarenheter. Den har formats av bidrag från utvecklare, datavetare och säkerhetsexperter över olika sektorer, alla engagerade i att bygga säkrare AI-applikationer. Vi är stolta över att dela denna 2025-version med dig, och vi hoppas att den ger dig verktygen och kunskapen för att effektivt säkra LLM:er.

Tack till alla som hjälpte till att sammanföra detta och de som fortsätter att använda och förbättra det. Vi är tacksamma över att få vara en del av detta arbete med dig.


###@ Steve Wilson
Project Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: https://www.linkedin.com/in/wilsonsd/

###@ Ads Dawson
Technical Lead & Vulnerability Entries Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: https://www.linkedin.com/in/adamdawson0/
