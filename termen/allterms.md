```dataview
table preferred_term, archetype, abstract_level, status, updated
from "Lexicon/Termen"
where type = "term"
sort archetype asc, abstract_level desc, preferred_term asc
