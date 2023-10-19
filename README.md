# Har brukt koden fra SE_Oblig2 til å kjøre tester i git med actions
# det oppstod mange problemer underveis, som måtte fikses for å kunne validere testene:
# installerte poetry 
# Error: "No event triggers defined in "on" ", og Error: "No jobs defined in "jobs"
# disse var trolig pga space eller shift indenterings feil og måtte rettes på
# Hadde feil branch navn som også kan være en faktor for at jeg ikke fikk kjørt testene, da min het "master" og ikke "main" i yaml. fila
# Endret også koden fra unittest til pytest etter forrige tilbakemelding fra studass
# ImportError while importing test module: jeg løste problemet med å legge __init__.py i directory leapyear, det holdt ikke å ha en __init__ inni hver mappe for src og test.
# Hadde også problemer med laste opp i github og etter mye flytting fram og tilbake, valgte jeg å pushe opp til tidligere repository for oblig2
# fant ut etter jeg endret fra unittest til pytest at logikken ikke helt stemte, og endret koden
