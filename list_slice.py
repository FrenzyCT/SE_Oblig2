#<liste>[<start>:<stop>]

movies = ["The matrix", "12 angry men", "pulp fiction", "into the wild", "wall-E"]

print(movies[1:4])
#print(movies[-4:-1])

#merk at elementet på start-indexen blir med men ikke slutten

#liste med steg (annenhver)
print(movies[1:4:2]) #hvert andre element fra og med start-indexen til, men ikke med, slutt-indexen

print(movies[2:]) #printer fra slutten og fram til 2
print(movies[:2]) #printer fra slutten og fram til 2#printer med starten av indexen og fram til 2