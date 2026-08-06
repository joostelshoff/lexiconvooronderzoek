---
type: richtlijn
preferred_term: abstract_level
status: concept
language: nl
scope: Nederlands hoger onderwijs
domains:
  - onderzoek
owners:
  - "[[Lexicon redactie]]"
tags:
  - lexicon
  - richtlijn
  - metadata
created: 06-08-2026
updated: 06-08-2026 15:57
---

# Richtlijn - abstract_level

## Doel

Het veld `abstract_level` geeft aan **hoe algemeen of specifiek een begrip is** binnen het lexicon.

Dit helpt gebruikers om:
- termen op een passend detailniveau te vergelijken;
- bredere en smallere termen consistenter te ordenen;
- informatiemodellen, beleidstermen en praktijktermen beter van elkaar te onderscheiden.

`abstract_level` zegt dus **niet** hoe belangrijk een term is, maar hoe **conceptueel algemeen of concreet** die term is.

## Interpretatie

We gebruiken een schaal van **1 tot en met 5**:

| Niveau | Interpretatie | Type begrip | Voorbeeld |
|---|---|---|---|
| 1 | Zeer abstract | fundamenteel domeinbegrip of overkoepelend principe | Onderzoek, Open Science |
| 2 | Abstract | breed organiserend begrip of hoofdconcept | Datamanagement, Onderzoeksoutput |
| 3 | Middenniveau | gangbaar zelfstandig begrip dat in beleid en administratie direct bruikbaar is | Onderzoeksproject, Dataset, Publicatie |
| 4 | Specifiek | afgebakende deelterm of gespecialiseerde variant | Datamanagementplan, Ethische toetsing, Subsidieaanvraag |
| 5 | Zeer specifiek | concrete rol, subtype, instrument of lokaal sterk afgebakend begrip | Lector, METC, DOI |

## Werkwijze bij toekenning

Kies het abstractieniveau door te vragen:

1. Is dit begrip een **breed overkoepelend concept**?
   - Dan ligt niveau 1 of 2 voor de hand.

2. Is dit begrip een **zelfstandig herkenbare kernterm** in beleid, administratie of systemen?
   - Dan ligt niveau 3 voor de hand.

3. Is dit begrip een **specifieke uitwerking, subtype of procedurele variant** van een bredere term?
   - Dan ligt niveau 4 of 5 voor de hand.

## Vuistregels

- Een **bredere term** heeft meestal een **lager abstract_level-nummer** dan een smallere term.
- Een term met veel subtypen zit meestal op niveau 2 of 3.
- Een sterk contextgebonden of specialistische term zit meestal op niveau 4 of 5.
- Gebruik `abstract_level` alleen als hulpmiddel; de **definitie en termrelaties blijven leidend**.

## Voorbeelden

### Onderzoeksactiviteit
- `Onderzoek` → niveau 1
- `Onderzoeksproject` → niveau 3
- `Subsidieaanvraag` → niveau 4

### Onderzoeksrollen
- `Onderzoeker` → niveau 3 of 4
- `Lector` → niveau 5
- `Data steward` → niveau 4 of 5

### Datamanagement
- `Datamanagement` → niveau 2
- `Dataset` → niveau 3
- `Datamanagementplan` → niveau 4
- `DOI` → niveau 5

## Wat abstract_level niet is

`abstract_level` is niet:
- een maat voor belang;
- een maat voor frequent gebruik;
- een kwaliteitslabel;
- een vaste wetenschappelijke taxonomie.

Het is een **redactioneel hulpmiddel** om termen consistenter te ordenen.

## Open vragen

- Willen we niveau 1 uitsluitend reserveren voor domeinbrede kernbegrippen?
- Willen we per archetype ijkvoorbeelden vastleggen?
- Willen we validatieregels opnemen voor consistent gebruik?
