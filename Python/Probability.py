import math

# print(math.log2(1/2500))


def get_uniform_distribution(size_of_list):
    return [1.0 / size_of_list for i in range(size_of_list)]


def normalize(input_list):
    denominator = sum(input_list)
    return [1 / denominator * x for x in input_list]


def get_entropy(prob_list):
    entropy = 0
    for i in range(len(prob_list)):
        entropy += -1 * prob_list[i] * math.log10(prob_list[i])
    return entropy
