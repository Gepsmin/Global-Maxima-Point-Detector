import numpy as np


def g(x, noise=0):
    r = (p5*np.exp(-np.power(x+p1, 2.)/(2*np.power(p3, 2.)))
         + np.exp(-np.power(x-p2, 2.)/(2*np.power(p4, 2.))))
    return r + (noise*(np.random.random()-0.5)/10)


def sample_range(sample):
    return max(sample) - min(sample)


def find_sample(mu=0, var=0.5):
    sample = []
    while len(sample) < 15:
        random_x = np.random.normal(loc=mu, scale=var, size=1)[0]
        if 1 > random_x > -1:
            sample.append(random_x)
    return sample


true_cases = 0
total_diff = 0
for test_number in range(1000):
    p1 = np.random.uniform(low=0.1, high=0.5, size=1)
    p2 = np.random.uniform(low=0.1, high=0.5, size=1)
    p3 = np.random.uniform(low=0.1, high=0.25, size=1)
    p4 = np.random.uniform(low=0.1, high=0.25, size=1)
    p5 = np.random.uniform(low=0.5, high=1.5, size=1)

    line = np.linspace(-1, 1, 200)
    noise = np.random.normal(loc=1, scale=1, size=200)
    noise_value = 0
    y = g(line, noise_value)

    sample_space = find_sample()
    sample_space_y = g(sample_space, noise_value)

    s_range = sample_range(sample_space)
    iteration = 1

    while s_range > 0.01:
        neu_space = []
        sample_number = 12 - (iteration * 2)
        if sample_number < 1:
            sample_number = 1
        ind = np.argpartition(sample_space_y, -sample_number)[-sample_number:]
        max_point = np.argpartition(sample_space_y, -1)[-1:]
        for i in ind:
            neu_space.append(sample_space[i])
        neu_mu = np.mean(neu_space)
        neu_var = np.var(neu_space)
        neu_range = sample_range(neu_space)
        value = neu_range**0.5
        if value <= 0.00001:
            value = 0.00001
        sample_space = find_sample((neu_mu+sample_space[max_point[0]])/2, neu_var * (sample_number**0.5) * 2/(value))
        sample_space_y = g(sample_space, noise_value)
        iteration += 1
        s_range = sample_range(sample_space)

    if -0.01 < max(y) - max(sample_space_y) < 0.01:
        true_cases += 1
    total_diff += abs(max(y) - max(sample_space_y))

print(true_cases, "cases are true from 1000 experiments")
print("average difference between maximal points is", total_diff/1000)
