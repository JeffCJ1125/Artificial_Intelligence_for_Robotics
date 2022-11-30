import Probability as prob

# Write code that outputs p after multiplying each entry
# by pHit or pMiss at the appropriate places. Remember that
# the red cells 1 and 2 are hits and the other green cells
# are misses.
p = prob.get_uniform_distribution(5)
# p = [0, 1, 0, 0, 0]
# p = [0.05,0.05,0.05,0.8,0.05]
# print(prob.get_entropy(p))
world = ["green", "red", "red", "green", "green"]
measurements = ["red", "red"]
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, Z):
    q = p
    for i in range(len(p)):
        if Z == world[i]:
            q[i] *= pHit
        else:
            q[i] *= pMiss
    q = prob.normalize(q)
    return q


def move(p, U):
    q = [0] * len(p)
    for i in range(len(p)):
        Exact_index = (i + U) % len(p)
        q[Exact_index] += p[i] * pExact
        Overshoot_index = (i + U + 1) % len(p)
        q[Overshoot_index] += p[i] * pOvershoot
        Undershoot_index = (i + U - 1) % len(p)
        q[Undershoot_index] += p[i] * pUndershoot
    return q


for i in range(len(measurements)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])
print(p)

# for i in range(len(measurements)):
#     p = sense(p,measurements[i])
# print(p)

# #Enter code here
# for i in range(len(p)):
#     if i == 1 or i == 2:
#         p[i] *= pHit
#     else:
#         p[i] *= pMiss
# p = prob.normalize(p)
# print("posterior probability: ",p)
