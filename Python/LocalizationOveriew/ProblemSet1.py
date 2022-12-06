# Quiz1
# p(x) = 0.2 what is p(not x)?
pX = 0.2
pNotX = 1 - 0.2
# p(x) = 0.2 , p(y) = 0.2 , x,y are independent what is p(x,y)?
pX = 0.2
pY = 0.2
pXandY = pX * pY
# p(x) = 0.2 , p(y|x) = 0.6 , p(y| not x) = 0.6 , what is p(y)?
pX = 0.2
pYwithX = 0.6
pYwithNotX = 0.6

pY = pYwithX * pX + pYwithNotX * pNotX
print(pY)

# Bayes' Rule
# the probability of house get fire p(F) = 0.001
# your neighbor say Yes it burns , but sometime your neighbor lie with probability 0.1
# what is the non-normalize probability p(F|B) , p(noF|B) and the normalize probability p(F|B) , p(noF|B)

pFire = 0.001
pNeighbor_lie = 0.1

non_normalize_pFire_Neighbor = pFire * (1 - pNeighbor_lie)
print(non_normalize_pFire_Neighbor)
non_normalize_pNotFire_Neighbor = (1 - pFire) * (pNeighbor_lie)
print(non_normalize_pNotFire_Neighbor)

pFire_Neighbor = non_normalize_pFire_Neighbor / (
    non_normalize_pFire_Neighbor + non_normalize_pNotFire_Neighbor
)
print(pFire_Neighbor)
pNotFire_Neighbor = non_normalize_pNotFire_Neighbor / (
    non_normalize_pFire_Neighbor + non_normalize_pNotFire_Neighbor
)
print(pNotFire_Neighbor)
