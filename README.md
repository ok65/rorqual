# rorqual
Requirements management 


## Artefact Content organisation: 
single db
+ documents are notional makes it easier to retrieve data from any document
- difficult to allow multiple users editing different documents, issues with storing data in git

multiple json
+ separate documents can be edited and uprev'd in git without conflict
- more difficult to grab data between documents (i.e linkage text from one doc to another) 

## Linkage organisation
linkage data centralised
+ one single place for all links, after doc is loaded can grab all relevant links in one go
- conflict/multiple users working on diff docs.

linkage data stored in the source doc
+ multiple users can edit doc/links in their own docs without issue.
- would have to scan every single doc to find dest links - very tedious