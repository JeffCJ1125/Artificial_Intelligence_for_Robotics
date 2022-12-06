import Probability as prob


# Bayes theorem reminder:
# P(A|B) = P(B|A)*P(A) / P(B)
# P(B) = sum of P(B|A)*P(A)


pCancer = 0.001
PCancerfree = 0.999
pPositive_withCancer = 0.8
pPositive_withoutCancer = 0.1

pCancer_withPositive = (
    pPositive_withCancer
    * pCancer
    / (pPositive_withCancer * pCancer + pPositive_withoutCancer * PCancerfree)
)
print(pCancer_withPositive)
