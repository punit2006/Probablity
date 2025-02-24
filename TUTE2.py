# 1A
import random
def toss_coin():
    heads, tails = 0, 0
    for _ in range(10000):
        outcome = random.choice(['heads', 'tails'])
        if outcome == 'heads':
            heads += 1
        else:
            tails += 1
    probability_heads = heads / 10000
    probability_tails = tails / 10000
    print(f"Probability of heads: {probability_heads}")
    print(f"Probability of tails: {probability_tails}")

toss_coin()

# 1B
def roll_dice():
    sum_seven = 0
    total_rolls = 10000
    for _ in range(total_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 + dice2 == 7:
            sum_seven += 1
    probability_seven = sum_seven / total_rolls
    print(f"Probability of getting sum of 7: {probability_seven}")

roll_dice()

# 2
def est_six_probability():
    trials = 10000
    success_count = 0
    
    for _ in range(trials):
        rolls = [random.randint(1, 6) for _ in range(10)]
        if 6 in rolls:
            success_count += 1
            
    probability = success_count / trials
    print(f"Estimated probability of getting at least one '6' in 10 rolls: {probability}")

est_six_probability()

# 3
def est_conditional_probability():
    red, green, blue = 5, 7, 8
    total_balls = red + green + blue
    trials = 1000
    previous_blue = 0
    red_given_blue = 0

    for _ in range(trials):
        first_draw = random.choice(['red']*red + ['green']*green + ['blue']*blue)
        second_draw = random.choice(['red']*red + ['green']*green + ['blue']*blue)
        
        if first_draw == 'blue':
            previous_blue += 1
            if second_draw == 'red':
                red_given_blue += 1
    
    probability = red_given_blue / previous_blue if previous_blue else 0
    print(f"Conditional probability of drawing a red ball given previous was blue: {probability}")

est_conditional_probability()

# 4
import numpy as np

def discrete_random_variable():
    probabilities = [0.25, 0.35, 0.4]
    values = [1, 2, 3]
    sample = np.random.choice(values, size=1000, p=probabilities)
    
    mean = np.mean(sample)
    variance = np.var(sample)
    std_deviation = np.std(sample)
    
    print(f"Empirical mean: {mean}")
    print(f"Empirical variance: {variance}")
    print(f"Empirical standard deviation: {std_deviation}")

discrete_random_variable()

# 5
import matplotlib.pyplot as plt
import numpy as np

def exp_distribution():
    sample_size = 2000
    mean = 5
    data = np.random.exponential(scale=mean, size=sample_size)
    
    # Histogram
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # PDF
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    pdf = (1 / mean) * np.exp(-x / mean)
    plt.plot(x, pdf, 'k', linewidth=2)
    
    plt.title("Exponential Distribution with Mean = 5")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.show()

exp_distribution()

# 6
def central_limit_theorem():
    # Step a: Generate 10,000 random numbers from a uniform distribution
    uniform_data = np.random.uniform(low=0, high=1, size=10000)
    
    # Step b: Draw 1000 samples of size n = 30
    sample_means = []
    for _ in range(1000):
        sample = np.random.choice(uniform_data, size=30)
        sample_means.append(np.mean(sample))
    
    # Plot uniform distribution and sample means
    plt.subplot(1, 2, 1)
    plt.hist(uniform_data, bins=30, density=True, alpha=0.6, color='b')
    plt.title("Uniform Distribution")
    
    plt.subplot(1, 2, 2)
    plt.hist(sample_means, bins=30, density=True, alpha=0.6, color='r')
    plt.title("Sample Means Distribution")
    
    plt.show()

central_limit_theorem()
