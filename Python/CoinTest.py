import Probability as prob


# Bayes theorem reminder:
# P(A|B) = P(B|A)*P(A) / P(B)
# P(B) = sum of P(B|A)*P(A)


# filp a coin
# accept the result when the coin is up on tail
# if the coin is up on Heads, filp again then accept the result

pCoinTail = 0.5
pCoinHeads = 0.5

pResultHeads = pCoinHeads * pCoinHeads
print(pResultHeads)


# there are two coins.
# one is fair coin which p(heads) = p(tails) = 0.5
# one is loaded conin which p(Heads) = 0.1
# take a coin with 50% get fair coin , flip it and get a result with Head.
# what is the probability we flip the fair coin.

pFairCoin_Heads = 0.5
pLoadedCoin_Heads = 0.1

pTakeFairCoin = 0.5
pTakeLoadedCoin = 0.5

# P(Fair|Head) = P(Head|Fair)*P(Fair) / P(Head)

pFairCoin_withResultHead = (
    pFairCoin_Heads
    * pTakeFairCoin
    / (pFairCoin_Heads * pTakeFairCoin + pTakeLoadedCoin * pLoadedCoin_Heads)
)
print(pFairCoin_withResultHead)
