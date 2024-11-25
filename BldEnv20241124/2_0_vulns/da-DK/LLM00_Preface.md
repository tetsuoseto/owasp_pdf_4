## Brev fra projektlederne

OWASP Top 10 for store sprogmodelapplikationer startede i 2023 som en fællesskabsdrevet indsats for at fremhæve og adressere sikkerhedsproblemer, der er specifikke for AI-applikationer. Siden da er teknologien fortsat med at sprede sig på tværs af industrier og applikationer, og det samme har de tilhørende risici. Efterhånden som LLM'er er indlejret dybere i alt fra kundeinteraktioner til interne operationer, opdager udviklere og sikkerhedsprofessionelle nye sårbarheder – og måder at imødegå dem på.

2023-listen var en stor succes med at øge bevidstheden og bygge et grundlag for sikker LLM-brug, men vi har lært endnu mere siden da. I denne nye 2025-version har vi arbejdet med en større, mere forskelligartet gruppe af bidragydere verden over, som alle har været med til at forme denne liste. Processen involverede brainstormsessioner, afstemning og feedback fra den virkelige verden fra fagfolk i spidsen af ​​LLM-applikationssikkerhed, hvad enten det var ved at bidrage eller forfine disse poster gennem feedback. Hver stemme var afgørende for at gøre denne nye udgivelse så grundig og praktisk som muligt.

### Hvad er nyt i 2025 Top 10

2025-listen afspejler en bedre forståelse af eksisterende risici og introducerer kritiske opdateringer om, hvordan LLM'er bruges i virkelige applikationer i dag. For eksempel udvider **Ubundet forbrug** det, der tidligere var Denial of Service til at omfatte risici omkring ressourcestyring og uventede omkostninger – et presserende problem i storstilede LLM-implementeringer.

Indgangen **Vector and Embeddings** reagerer på fællesskabets anmodninger om vejledning om sikring af Retrieval-Augmented Generation (RAG) og andre indlejringsbaserede metoder, nu kernepraksis for jording af modeloutput.

Vi har også tilføjet **System Prompt Leakage** for at adressere et område med virkelige udnyttelser, som var stærkt efterspurgt af fællesskabet. Mange applikationer antog, at prompter var sikkert isoleret, men nylige hændelser har vist, at udviklere ikke sikkert kan antage, at oplysningerne i disse prompter forbliver hemmelige.

**Excessive Agency** er blevet udvidet på grund af den øgede brug af agentiske arkitekturer, der kan give LLM mere autonomi.  Med LLM'er, der fungerer som agenter eller i plug-in-indstillinger, kan umarkerede tilladelser føre til utilsigtede eller risikable handlinger, hvilket gør denne post mere kritisk end nogensinde.

### Går fremad

Ligesom selve teknologien er denne liste et produkt af open source-fællesskabets indsigt og erfaringer. Det er blevet formet af bidrag fra udviklere, dataforskere og sikkerhedseksperter på tværs af sektorer, der alle er forpligtet til at bygge sikrere AI-applikationer. Vi er stolte af at dele denne 2025-version med dig, og vi håber, at den giver dig værktøjerne og viden til at sikre LLM'er effektivt.

Tak til alle, der hjalp med at bringe dette sammen, og dem, der fortsætter med at bruge og forbedre det. Vi er taknemmelige for at være en del af dette arbejde sammen med dig.

###@ Steve Wilson
Project Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: https://www.linkedin.com/in/wilsonsd/

###@ Ads Dawson
Technical Lead & Vulnerability Entries Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: https://www.linkedin.com/in/adamdawson0/
