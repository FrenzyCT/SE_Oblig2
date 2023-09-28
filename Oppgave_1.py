#Ta et tall fra brukeren på følgende måte: input("Hva er meningen med livet?").
# Konverter inputen til int og lag en if-test som sjekker om verdien er lik 42.
# Hvis dette er tilfellet, skriv ut "Det stemmer, meningen med livet er 42!", hvis ikke; skriv ut "FEIL!".
#Legge til én ekstra sjekk i denne if-testen som sjekker om input-tallet er mellom 30 og 50,
# altså større enn 30 og mindre enn 50 på samme tid (hint: logiske operatorer).
# Hvis dette er tilfellet, skriv ut "Nærme, men feil."


number= input("Hva er meningen med livet? ")

number= int(number)
if number == 42:
    print(" Det stemmer, meningen med livet er 42!")
elif number > 30 and number <50:
    print("Nærme, men feil.")

else:
    print("FEIL")


    print("Nærme, men feil.")