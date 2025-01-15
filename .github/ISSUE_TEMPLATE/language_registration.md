---
name: Language registration
about: Request to support new language
title: 'Language Registration:'
labels: 'language registration'
assignees: ''

---

**Language Code:**
Please check the language codes already supported using "owsp_pdf -r" command first.

**Description:**
Why is the new language code required?

----------------------------------------
It should be ISO 639-2 language code and ISO 3166 region code joined by hyphen e.g. `en-US`. In the OWASP PDF system, there can be two or more language codes associated with one language.  Three factors drive language variations:

- Font glyphs
- Word spelling
- Paper size

For example, we have `en-US` and `en-GB` because of paper size and spelling.
We use not ISO 639-2 language code `ja` or `ko` alone but `ja-JP` and `ko-KR` for Japanese and Korean although they are the only Japanese and Korean language codes respectively. `en-ZZ` is reserved as *International English* which uses `en-US` glyphs and spelling and `A4` paper size.  `fr-CA` and `fr-FR` share the same glyphs and spelling, but they use different paper sizes: A4 for `fr-FR` and Letter for `fr-CA`.  `en-ZZ` is the source of every localization.

ISO References
1. [ISO 639-2 language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
2. [ISO 3166 region code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)
