# Complete Statistics + SciPy Study Notes
## For Data Science / Machine Learning / AI

---

# How to Use These Notes

Each topic follows this structure:

**Concept → Intuition → Formula → Manual Example → Python/SciPy → Interpretation → Common Mistakes → When to Use**

> **Philosophy:** Statistics first, SciPy second. Never run a function without understanding what it computes and why.

---

# PART 1 — FOUNDATIONS OF STATISTICS

## 1.1 What is Statistics?

**Concept:** Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data to make informed decisions under uncertainty.

**Intuition:** You cannot measure everything. Statistics helps you make reliable conclusions from limited information.

**Two branches:**

| Branch | Purpose | Example |
|--------|---------|---------|
| **Descriptive** | Summarize observed data | Average height of 30 students |
| **Inferential** | Generalize from sample to population | Predict average height of all students in a university |

## 1.2 Population vs Sample

| Term | Definition | Symbol |
|------|-----------|--------|
| **Population** | Entire group of interest | $N$ |
| **Sample** | Subset of population | $n$ |
| **Parameter** | Numerical summary of population | $\mu, \sigma, p$ |
| **Statistic** | Numerical summary of sample | $\bar{x}, s, \hat{p}$ |

**Real-world example:** You want to know the average salary of all 50,000 employees in a company (population). You survey 500 employees (sample). The sample mean $\bar{x}$ estimates the population mean $\mu$.

**Census vs Sample:** A census measures every unit; a sample measures a subset. Census is accurate but expensive; sampling is cheaper but has uncertainty.

## 1.3 Types of Data

```
Data
├── Qualitative (Categorical)
│   ├── Nominal (no order): eye color, city
│   └── Ordinal (ordered): education level, rating
└── Quantitative (Numerical)
    ├── Discrete (countable): number of children
    └── Continuous (measurable): height, temperature
```

## 1.4 Levels of Measurement

| Level | Properties | Example | Allowed Operations |
|-------|-----------|---------|-------------------|
| **Nominal** | Labels only | Blood type | Count, mode |
| **Ordinal** | Order, no fixed interval | Likert scale | Median, rank |
| **Interval** | Equal intervals, no true zero | Temperature (°C) | +, −, mean |
| **Ratio** | Equal intervals + true zero | Weight, income | ×, ÷, all stats |

**Common mistake:** Treating Likert scale (ordinal) as interval and computing means. Means of ordinal data can be misleading.

## 1.5 Variables

- **Independent variable (X):** The input/predictor
- **Dependent variable (Y):** The output/response
- **Confounding variable:** Affects both X and Y, creating spurious association

**Example:** Ice cream sales and drowning deaths are correlated. Confounder: temperature.

## 1.6 Frequency Distributions

**Frequency:** Count of observations in each category/bin.
**Relative frequency:** $\frac{f_i}{n}$
**Cumulative frequency:** Running total of frequencies.

```python
import numpy as np
data = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
values, counts = np.unique(data, return_counts=True)
relative = counts / len(data)
cumulative = np.cumsum(counts)
for v, c, r, cu in zip(values, counts, relative, cumulative):
    print(f"Value {v}: freq={c}, rel={r:.2f}, cum={cu}")
```

---

### Chapter 1 — Key Points
- Population vs sample distinction is fundamental
- Data types determine which statistics are valid
- Confounders create false causality

### 5 Quick Revision Questions
1. What is the difference between a parameter and a statistic?
2. Give an example of ordinal data.
3. Why can't we compute a mean for nominal data?
4. What is a confounding variable?
5. What is the difference between discrete and continuous data?

---

# PART 2 — DESCRIPTIVE STATISTICS

## 2.1 Central Tendency

### Arithmetic Mean

**Formula:** $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$

**Manual example:** $[2, 4, 6, 8]$ → $\bar{x} = (2+4+6+8)/4 = 5$

```python
import numpy as np
from scipy import stats

x = np.array([2, 4, 6, 8])
print(np.mean(x))        # 5.0
print(stats.tmean(x))    # 5.0 (trimmed mean with no trimming)
```

**Sensitivity:** Highly sensitive to outliers.

### Weighted Mean

**Formula:** $\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$

**Example:** Grades: 80 (weight 2), 90 (weight 3) → $(80×2 + 90×3)/5 = 86$

```python
x = np.array([80, 90])
w = np.array([2, 3])
print(np.average(x, weights=w))  # 86.0
```

**Use in DS:** Weighted metrics, survey weights, ensemble models.

### Geometric Mean

**Formula:** $G = \left(\prod_{i=1}^{n} x_i\right)^{1/n}$

**Use:** Growth rates, ratios, multiplicative processes.

```python
x = np.array([1.10, 1.20, 1.15])  # growth factors
print(stats.gmean(x))  # ≈ 1.149
```

### Harmonic Mean

**Formula:** $H = \frac{n}{\sum 1/x_i}$

**Use:** Rates, speeds, F1-score (harmonic mean of precision & recall).

```python
x = np.array([2, 4, 8])
print(stats.hmean(x))  # ≈ 3.43
```

### Median

**Definition:** Middle value when sorted. For even n, average of two middle values.

```python
x = np.array([1, 3, 5, 7, 100])
print(np.median(x))  # 5 (robust to outlier)
```

### Mode

**Definition:** Most frequent value.

```python
x = np.array([1, 2, 2, 3, 4])
print(stats.mode(x))  # ModeResult(mode=2, count=2)
```

### Trimmed Mean

**Definition:** Mean after removing a percentage from each tail.

```python
x = np.array([1, 2, 3, 4, 5, 6, 100])
print(stats.trim_mean(x, proportiontocut=0.2))  # removes 20% each side
```

**Summary Table:**

| Measure | Outlier Sensitivity | Use When |
|---------|-------------------|----------|
| Mean | High | Symmetric data |
| Median | Low | Skewed data |
| Mode | Low | Categorical data |
| Geometric mean | Low | Growth rates |
| Trimmed mean | Low | Robust central tendency |

---

## 2.2 Measures of Dispersion

### Range
$R = x_{max} - x_{min}$

### Variance

**Population:** $\sigma^2 = \frac{1}{N}\sum(x_i - \mu)^2$

**Sample:** $s^2 = \frac{1}{n-1}\sum(x_i - \bar{x})^2$

> **Why n−1?** Bessel's correction: sample mean is estimated, so deviations are smaller than from true mean. Dividing by n−1 makes $s^2$ unbiased.

```python
x = np.array([2, 4, 6, 8])
print(np.var(x, ddof=0))   # population: 5.0
print(np.var(x, ddof=1))   # sample: 6.67
print(stats.tvar(x))       # sample variance
```

### Standard Deviation
$\sigma = \sqrt{\sigma^2}$, $s = \sqrt{s^2}$

### Coefficient of Variation
$CV = \frac{s}{\bar{x}} \times 100\%$

**Use:** Compare variability across different units/scales.

```python
print(stats.variation(x))  # CV as fraction
```

### Interquartile Range
$IQR = Q_3 - Q_1$

```python
print(stats.iqr(x))
```

### Mean Absolute Deviation
$MAD_{mean} = \frac{1}{n}\sum|x_i - \bar{x}|$

### Median Absolute Deviation
$MAD = \text{median}(|x_i - \text{median}(x)|)$

```python
print(stats.median_abs_deviation(x))
```

### Standard Error
$SE = \frac{s}{\sqrt{n}}$

**Key distinction:**

| Measure | What it measures | Formula |
|---------|-----------------|---------|
| SD | Spread of individual data | $\sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}$ |
| SEM | Precision of sample mean | $\frac{s}{\sqrt{n}}$ |

```python
print(stats.sem(x))
```

**Common mistake:** Confusing SD with SEM. SD describes data; SEM describes the estimate of the mean.

---

## 2.3 Position Measures

### Percentiles, Quartiles, Deciles

- **Percentile:** $P_k$ = value below which k% of data falls
- **Quartiles:** $Q_1=P_{25}$, $Q_2=P_{50}$, $Q_3=P_{75}$
- **Deciles:** $D_1=P_{10}, \ldots, D_9=P_{90}$

```python
x = np.arange(1, 101)
print(np.percentile(x, 25))  # Q1
print(np.percentile(x, 50))  # median
print(np.percentile(x, 75))  # Q3
print(stats.scoreatpercentile(x, 90))  # SciPy alternative
```

**Percentile vs Percentage:** Percentage is a fraction (e.g., 80%). Percentile is a position in a distribution (e.g., 80th percentile).

### Five-Number Summary
Min, Q1, Median, Q3, Max

```python
print(np.percentile(x, [0, 25, 50, 75, 100]))
```

### Z-Score

**Formula:** $z = \frac{x - \mu}{\sigma}$ (population) or $z = \frac{x - \bar{x}}{s}$ (sample)

**Interpretation:** How many standard deviations a value is from the mean.

```python
x = np.array([2, 4, 6, 8, 10])
print(stats.zscore(x))
```

**In ML:** Standardization (`StandardScaler`) uses z-scores. Critical for PCA, SVM, k-means, neural networks.

---

## 2.4 Outliers

### IQR Method
Outlier if $x < Q_1 - 1.5 \cdot IQR$ or $x > Q_3 + 1.5 \cdot IQR$

```python
def iqr_outliers(x):
    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5*iqr, q3 + 1.5*iqr
    return x[(x < lower) | (x > upper)]
```

### Z-Score Method
Outlier if $|z| > 3$ (or 2.5)

### MAD Method
Outlier if $\frac{0.6745 \cdot |x - \text{median}|}{MAD} > 3.5$

**When to remove vs retain:**
- **Remove:** Data entry error, measurement error
- **Retain:** Genuine extreme values (e.g., CEO salary in income data)
- **Transform:** Skewed data → log transform

---

## 2.5 Shape of Distribution

### Moments

| Moment | Formula | Meaning |
|--------|---------|---------|
| 1st raw | $E[X]$ | Mean |
| 2nd central | $E[(X-\mu)^2]$ | Variance |
| 3rd central | $E[(X-\mu)^3]$ | Skewness |
| 4th central | $E[(X-\mu)^4]$ | Kurtosis |

### Skewness
$g_1 = \frac{E[(X-\mu)^3]}{\sigma^3}$

- **Positive skew:** Right tail longer (income, house prices)
- **Negative skew:** Left tail longer (exam scores with easy test)
- **Zero:** Symmetric

```python
from scipy import stats
x = np.random.exponential(2, 1000)  # right-skewed
print(stats.skew(x))  # > 0
```

### Kurtosis
$g_2 = \frac{E[(X-\mu)^4]}{\sigma^4} - 3$ (excess kurtosis)

| Type | Excess Kurtosis | Meaning |
|------|----------------|---------|
| Mesokurtic | ≈ 0 | Normal-like |
| Leptokurtic | > 0 | Heavy tails, peaked |
| Platykurtic | < 0 | Light tails, flat |

```python
print(stats.kurtosis(x))  # excess kurtosis
print(stats.kurtosis(x, fisher=False))  # Pearson kurtosis
```

### ASCII Diagrams

**Positive Skew:**
```
    █
   ██
  ███
 ████
███████___
```

**Negative Skew:**
```
       █
      ██
     ███
    ████
___███████
```

**Normal:**
```
     █
    ███
   █████
  ███████
 █████████
```

---

### Chapter 2 — Key Points
- Mean is sensitive to outliers; median is robust
- Sample variance uses n−1
- SD ≠ SEM
- Z-score standardizes; used everywhere in ML
- Skewness and kurtosis describe shape

### Important Formulas
- $\bar{x} = \frac{1}{n}\sum x_i$
- $s^2 = \frac{\sum(x_i-\bar{x})^2}{n-1}$
- $CV = s/\bar{x}$
- $z = (x-\bar{x})/s$

### Important SciPy Functions
`tmean`, `gmean`, `hmean`, `mode`, `trim_mean`, `tvar`, `tstd`, `sem`, `variation`, `iqr`, `median_abs_deviation`, `zscore`, `skew`, `kurtosis`, `moment`

### 5 Quick Revision Questions
1. Why do we divide by n−1 in sample variance?
2. When is geometric mean preferred over arithmetic mean?
3. What does a z-score of −2 mean?
4. How does IQR detect outliers?
5. What does positive skew indicate about the mean vs median?

---

# PART 3 — PROBABILITY

## 3.1 Basic Concepts

- **Sample space (S):** Set of all possible outcomes
- **Event (A):** Subset of sample space
- **Complement:** $A^c$ or $\bar{A}$ — event not occurring
- **Union:** $A \cup B$ — A or B
- **Intersection:** $A \cap B$ — A and B
- **Mutually exclusive:** $A \cap B = \emptyset$

### Addition Rule
$P(A \cup B) = P(A) + P(B) - P(A \cap B)$

If mutually exclusive: $P(A \cup B) = P(A) + P(B)$

### Multiplication Rule
$P(A \cap B) = P(A) \cdot P(B|A)$

If independent: $P(A \cap B) = P(A) \cdot P(B)$

### Conditional Probability
$P(A|B) = \frac{P(A \cap B)}{P(B)}$

**Example:** P(rain | cloudy) = P(rain and cloudy) / P(cloudy)

### Independence
$A \perp B \iff P(A \cap B) = P(A)P(B)$

### Total Probability Theorem
$P(B) = \sum_i P(B|A_i)P(A_i)$

### Bayes Theorem
$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$

**Symbols:**
- $P(A)$ = prior
- $P(B|A)$ = likelihood
- $P(A|B)$ = posterior
- $P(B)$ = evidence

**Medical Testing Example:**

- Disease prevalence: $P(D) = 0.01$
- Sensitivity: $P(+|D) = 0.99$
- Specificity: $P(-|D^c) = 0.95$ → $P(+|D^c) = 0.05$

$P(D|+) = \frac{0.99 \times 0.01}{0.99 \times 0.01 + 0.05 \times 0.99} = \frac{0.0099}{0.0594} \approx 0.167$

**Interpretation:** Even with a positive test, only ~17% chance of disease. This is the base rate fallacy.

**Spam Classification (Naive Bayes):**
$P(\text{spam}|\text{words}) \propto P(\text{spam}) \prod_i P(\text{word}_i|\text{spam})$

---

### Chapter 3 — Key Points
- Bayes theorem updates beliefs with evidence
- Base rate matters enormously
- Independence simplifies calculations

### 5 Quick Revision Questions
1. State Bayes theorem.
2. What does conditional probability mean?
3. If P(A)=0.3, P(B)=0.4, and independent, what is P(A∩B)?
4. Why can a positive medical test still mean low disease probability?
5. What is the difference between mutually exclusive and independent?

---

# PART 4 — RANDOM VARIABLES

## 4.1 Definition

A **random variable** is a function mapping outcomes to real numbers.

- **Discrete:** Countable values (0, 1, 2, ...)
- **Continuous:** Any value in an interval

## 4.2 PMF, PDF, CDF

| Function | For | Definition | SciPy |
|----------|-----|-----------|-------|
| **PMF** | Discrete | $P(X=x)$ | `.pmf(x)` |
| **PDF** | Continuous | $f(x)$, density | `.pdf(x)` |
| **CDF** | Both | $F(x)=P(X \leq x)$ | `.cdf(x)` |
| **SF** | Both | $1-F(x)$ | `.sf(x)` |
| **PPF** | Both | Inverse CDF | `.ppf(q)` |

**Why $P(X=x)=0$ for continuous:** Probability is area under density. A single point has zero width, hence zero area.

```python
from scipy import stats
# Normal
print(stats.norm.pdf(0))      # density at 0
print(stats.norm.cdf(0))      # P(X ≤ 0) = 0.5
print(stats.norm.ppf(0.975))  # 1.96
print(stats.norm.sf(0))       # P(X > 0) = 0.5
```

## 4.3 Expectation & Variance

- $E[X] = \sum x P(X=x)$ or $\int x f(x) dx$
- $\text{Var}(X) = E[(X-\mu)^2] = E[X^2] - (E[X])^2$
- $E[aX+b] = aE[X]+b$
- $\text{Var}(aX+b) = a^2\text{Var}(X)$

## 4.4 Covariance & Correlation

$\text{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)]$

$\rho = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$

## 4.5 Conditional Expectation

$E[X|Y=y] = \sum_x x P(X=x|Y=y)$

**In ML:** Regression predicts $E[Y|X]$ — conditional expectation.

---

### Chapter 4 — Key Points
- PMF for discrete, PDF for continuous
- CDF gives cumulative probability
- PPF is inverse CDF (critical values)
- $E[X]$ is long-run average

### 5 Quick Revision Questions
1. Why is P(X=x)=0 for continuous variables?
2. What does PPF compute?
3. State the variance formula in terms of E[X²].
4. What is the difference between PMF and PDF?
5. What does conditional expectation represent in regression?

---

# PART 5 — PROBABILITY DISTRIBUTIONS

## 5.1 Discrete Distributions

### Bernoulli
- **Models:** Single yes/no trial
- **PMF:** $P(X=1)=p$, $P(X=0)=1-p$
- **Mean:** $p$, **Variance:** $p(1-p)$
- **SciPy:** `stats.bernoulli(p)`

```python
from scipy import stats
b = stats.bernoulli(0.3)
print(b.pmf(1))  # 0.3
print(b.mean(), b.var())  # 0.3, 0.21
```

### Binomial
- **Models:** Number of successes in n independent Bernoulli trials
- **PMF:** $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$
- **Mean:** $np$, **Variance:** $np(1-p)$
- **SciPy:** `stats.binom(n, p)`

```python
b = stats.binom(10, 0.5)
print(b.pmf(5))  # P(X=5)
print(b.cdf(5))  # P(X≤5)
```

**DS Example:** Click-through rate, conversion counts, A/B test successes.

### Geometric
- **Models:** Number of trials until first success
- **PMF:** $P(X=k) = (1-p)^{k-1}p$
- **Mean:** $1/p$, **Variance:** $(1-p)/p^2$
- **SciPy:** `stats.geom(p)`

### Negative Binomial
- **Models:** Number of trials until r successes
- **PMF:** $P(X=k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}$
- **Mean:** $r/p$
- **SciPy:** `stats.nbinom(r, p)`

### Poisson
- **Models:** Number of events in fixed interval
- **PMF:** $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$
- **Mean = Variance =** $\lambda$
- **SciPy:** `stats.poisson(mu)`

```python
p = stats.poisson(3)
print(p.pmf(2))  # P(X=2)
print(p.cdf(3))
```

**DS Example:** Website visits per minute, defects per batch.

### Hypergeometric
- **Models:** Sampling without replacement from finite population
- **PMF:** $P(X=k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$
- **SciPy:** `stats.hypergeom(M, n, N)`

### Multinomial
- **Models:** Generalized binomial with >2 categories
- **PMF:** $P(X_1=x_1,\ldots) = \frac{n!}{x_1!\cdots x_k!} p_1^{x_1}\cdots p_k^{x_k}$
- **SciPy:** `stats.multinomial(n, p)`

---

## 5.2 Continuous Distributions

### Uniform
- **PDF:** $f(x) = \frac{1}{b-a}$ for $a \leq x \leq b$
- **Mean:** $(a+b)/2$, **Variance:** $(b-a)^2/12$
- **SciPy:** `stats.uniform(loc=a, scale=b-a)`

### Normal (Gaussian)
- **PDF:** $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
- **Mean:** $\mu$, **Variance:** $\sigma^2$
- **SciPy:** `stats.norm(loc=mu, scale=sigma)`

```python
n = stats.norm(0, 1)
print(n.pdf(0))       # 0.399
print(n.cdf(1.96))    # 0.975
print(n.ppf(0.975))   # 1.96
print(n.rvs(5))       # 5 random samples
```

**68-95-99.7 Rule:**
- 68% within 1σ
- 95% within 2σ
- 99.7% within 3σ

### Standard Normal
$\mu=0, \sigma=1$. Z-score transforms any normal to standard normal.

### Exponential
- **Models:** Time between Poisson events
- **PDF:** $f(x) = \lambda e^{-\lambda x}$
- **Mean:** $1/\lambda$, **Variance:** $1/\lambda^2$
- **SciPy:** `stats.expon(scale=1/λ)`

### Gamma
- **PDF:** $f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}$
- **Mean:** $\alpha/\beta$, **Variance:** $\alpha/\beta^2$
- **SciPy:** `stats.gamma(a=α, scale=1/β)`

### Beta
- **PDF:** $f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$
- **Mean:** $\frac{\alpha}{\alpha+\beta}$
- **Use:** Modeling probabilities, Bayesian priors
- **SciPy:** `stats.beta(a, b)`

### Lognormal
- If $X \sim \text{Normal}$, then $e^X \sim \text{Lognormal}$
- **Use:** Income, stock prices, survival times
- **SciPy:** `stats.lognorm(s=σ, scale=e^μ)`

### Weibull
- **PDF:** $f(x) = \frac{k}{\lambda}(\frac{x}{\lambda})^{k-1} e^{-(x/\lambda)^k}$
- **Use:** Reliability, survival analysis
- **SciPy:** `stats.weibull_min(c=k, scale=λ)`

### Chi-Square
- **Definition:** Sum of squares of k independent standard normals
- **Mean:** $k$, **Variance:** $2k$
- **Use:** Goodness-of-fit, independence tests, variance estimation
- **SciPy:** `stats.chi2(df=k)`

### Student's t
- **Definition:** $T = \frac{Z}{\sqrt{V/k}}$ where $Z \sim N(0,1)$, $V \sim \chi^2_k$
- **Use:** Small samples, unknown σ
- **SciPy:** `stats.t(df)`

### F Distribution
- **Definition:** Ratio of two chi-square variables
- **Use:** ANOVA, comparing variances
- **SciPy:** `stats.f(dfn, dfd)`

### Cauchy
- **PDF:** $f(x) = \frac{1}{\pi(1+x^2)}$
- **No mean, no variance!**
- **SciPy:** `stats.cauchy()`

### Logistic
- **Use:** Logistic regression link function
- **SciPy:** `stats.logistic()`

### Laplace
- **Use:** Robust statistics, double exponential
- **SciPy:** `stats.laplace()`

### Pareto
- **Use:** Wealth distribution, extreme events
- **SciPy:** `stats.pareto(b)`

### Gumbel / GEV / Generalized Pareto
- **Use:** Extreme value theory
- **SciPy:** `stats.gumbel_r()`, `stats.genextreme()`, `stats.genpareto()`

### Rayleigh
- **Use:** Signal amplitude, wind speed
- **SciPy:** `stats.rayleigh()`

---

## 5.3 Multivariate Distributions

### Multivariate Normal
- **PDF:** $f(\mathbf{x}) = \frac{1}{(2\pi)^{k/2}|\Sigma|^{1/2}} e^{-\frac{1}{2}(\mathbf{x}-\mu)^T\Sigma^{-1}(\mathbf{x}-\mu)}$
- **SciPy:** `stats.multivariate_normal(mean, cov)`

```python
mean = [0, 0]
cov = [[1, 0.5], [0.5, 2]]
mvn = stats.multivariate_normal(mean, cov)
print(mvn.pdf([0, 0]))
print(mvn.rvs(3))
```

### Dirichlet
- **Use:** Topic modeling (LDA), compositional data
- **SciPy:** `stats.dirichlet(alpha)`

### Multivariate t
- **Use:** Robust multivariate analysis
- **SciPy:** `stats.multivariate_t(loc, shape, df)`

---

## 5.4 Distribution Relationships

```
Bernoulli → Binomial (n trials)
Exponential → Gamma (sum of exponentials)
Normal² → Chi-square (sum of squares)
Normal + sample variance → t
Chi-square ratio → F
Binomial → Poisson (n large, p small)
Poisson → Normal (λ large)
```

## 5.5 Distribution Selection Table

| Scenario | Distribution |
|----------|-------------|
| Yes/no outcome | Bernoulli |
| # successes in n trials | Binomial |
| Trials until success | Geometric |
| Events per interval | Poisson |
| Time between events | Exponential |
| Sum of exponentials | Gamma |
| Probability (0 to 1) | Beta |
| Income, stock price | Lognormal |
| Reliability/lifetime | Weibull |
| Variance inference | Chi-square |
| Small sample mean | t |
| Variance ratio | F |
| Extreme values | GEV/GPD |
| Correlated normals | Multivariate Normal |

---

### Chapter 5 — Key Points
- Each distribution models a specific data-generating process
- Mean and variance formulas differ by distribution
- SciPy provides `pmf/pdf`, `cdf`, `ppf`, `rvs` for all
- Relationships connect distributions

### 5 Quick Revision Questions
1. When do you use Poisson vs Binomial?
2. What is the relationship between Exponential and Gamma?
3. Why does t-distribution have heavier tails than Normal?
4. What distribution models time until failure?
5. What is the mean of a Beta(2,3)?

---

# PART 6 — SAMPLING

## 6.1 Key Concepts

- **Sampling frame:** List of all units in population
- **Sampling bias:** Systematic error in selection
- **Random sampling:** Every unit has known probability

## 6.2 Sampling Methods

| Method | Description | Pros | Cons |
|--------|-------------|------|------|
| Simple random | Every unit equally likely | Unbiased | Needs full frame |
| Stratified | Divide into strata, sample each | Ensures representation | Needs stratum info |
| Cluster | Sample entire clusters | Cheap | Higher variance |
| Systematic | Every k-th unit | Easy | Periodicity risk |
| Convenience | Easy to reach | Fast | Biased |

## 6.3 Sampling Distribution

The **sampling distribution** of a statistic is its distribution over repeated samples.

**Sampling distribution of mean:**
- Mean: $\mu_{\bar{x}} = \mu$
- SE: $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$

**Sampling distribution of proportion:**
- Mean: $p$
- SE: $\sqrt{\frac{p(1-p)}{n}}$

## 6.4 Central Limit Theorem (CLT)

**Statement:** For i.i.d. random variables with mean μ and finite variance σ², as $n \to \infty$:

$\bar{X}_n \sim N\left(\mu, \frac{\sigma^2}{n}\right)$ approximately

**Intuition:** Sums/averages of many independent effects tend toward normality.

```python
import numpy as np
import matplotlib.pyplot as plt

# Population: heavily skewed
population = np.random.exponential(1, 100000)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for i, n in enumerate([1, 5, 30]):
    means = [np.mean(np.random.choice(population, n)) for _ in range(5000)]
    axes[i].hist(means, bins=30, density=True)
    axes[i].set_title(f'n={n}')
plt.show()
```

## 6.5 Law of Large Numbers (LLN)

As $n \to \infty$, $\bar{X}_n \to \mu$ (in probability).

**CLT vs LLN:**
- LLN: Sample mean converges to population mean
- CLT: Distribution of sample mean becomes normal

---

### Chapter 6 — Key Points
- Sampling distribution is the bridge from sample to population
- CLT works for n ≥ 30 typically (less for symmetric)
- SE decreases with √n

### 5 Quick Revision Questions
1. What is the standard error of the mean?
2. State the Central Limit Theorem.
3. What is the difference between stratified and cluster sampling?
4. Why does SE decrease as √n?
5. What is sampling bias?

---

# PART 7 — ESTIMATION

## 7.1 Point Estimation

An **estimator** is a rule; an **estimate** is the value.

**Properties:**
- **Unbiased:** $E[\hat{\theta}] = \theta$
- **Efficient:** Lowest variance among unbiased estimators
- **Consistent:** Converges to true value as n → ∞
- **Sufficient:** Uses all information in sample

**MSE:** $\text{MSE}(\hat{\theta}) = \text{Bias}^2 + \text{Variance}$

## 7.2 Maximum Likelihood Estimation (MLE)

**Likelihood:** $L(\theta) = \prod_i f(x_i|\theta)$
**Log-likelihood:** $\ell(\theta) = \sum_i \log f(x_i|\theta)$

**MLE:** $\hat{\theta}_{MLE} = \arg\max_\theta \ell(\theta)$

**Bernoulli MLE:**
$\ell(p) = \sum x_i \log p + (n - \sum x_i)\log(1-p)$
$\frac{d\ell}{dp} = 0 \implies \hat{p} = \bar{x}$

**Normal MLE:**
$\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i-\bar{x})^2$ (biased!)

```python
from scipy import stats
import numpy as np

data = np.random.normal(5, 2, 1000)
mu, sigma = stats.norm.fit(data)
print(f"MLE: μ={mu:.3f}, σ={sigma:.3f}")
```

---

### Chapter 7 — Key Points
- MLE finds parameters that maximize likelihood
- MLE is consistent but can be biased
- SciPy `.fit()` uses MLE

### 5 Quick Revision Questions
1. What is the difference between an estimator and an estimate?
2. What does unbiased mean?
3. Derive the MLE for Bernoulli p.
4. What is the MSE decomposition?
5. Is the MLE of normal variance biased?

---

# PART 8 — CONFIDENCE INTERVALS

## 8.1 Concept

A 95% CI is an interval constructed such that 95% of such intervals (from repeated sampling) contain the true parameter.

**Correct interpretation:** "If we repeated this sampling procedure many times, 95% of the intervals would contain μ."

**Wrong interpretation:** "95% probability that μ is in this interval." (Frequentist μ is fixed.)

## 8.2 Formulas

**Mean (σ known):** $\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$

**Mean (σ unknown):** $\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$

**Proportion:** $\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

**Variance:** $\left(\frac{(n-1)s^2}{\chi^2_{1-\alpha/2}}, \frac{(n-1)s^2}{\chi^2_{\alpha/2}}\right)$

## 8.3 Python Example

```python
import numpy as np
from scipy import stats

data = np.random.normal(5, 2, 30)
n = len(data)
xbar = np.mean(data)
s = np.std(data, ddof=1)
se = s / np.sqrt(n)

# t-based 95% CI
t_crit = stats.t.ppf(0.975, df=n-1)
ci = (xbar - t_crit*se, xbar + t_crit*se)
print(f"95% CI: {ci}")
```

## 8.4 Bootstrap CI

```python
from scipy import stats
data = np.random.exponential(3, 100)
res = stats.bootstrap((data,), np.mean, confidence_level=0.95, n_resamples=10000)
print(res.confidence_interval)
```

---

### Chapter 8 — Key Points
- CI quantifies uncertainty in estimation
- t-based for small samples/unknown σ
- Bootstrap for non-normal statistics
- Never say "95% probability parameter is inside"

### 5 Quick Revision Questions
1. What does a 95% CI actually mean?
2. When do you use t vs z?
3. How does sample size affect CI width?
4. What is the bootstrap CI?
5. Why is the common interpretation of CI wrong?

---

# PART 9 — HYPOTHESIS TESTING

## 9.1 Framework

1. **Null hypothesis (H₀):** No effect, no difference
2. **Alternative (H₁):** Effect exists
3. **Significance level (α):** Usually 0.05
4. **Test statistic:** Computed from data
5. **p-value:** P(data or more extreme | H₀ true)
6. **Decision:** Reject H₀ if p < α

## 9.2 Errors

| | H₀ True | H₀ False |
|---|---|---|
| Reject H₀ | Type I error (α) | Correct |
| Fail to reject | Correct | Type II error (β) |

**Power = 1 − β**

## 9.3 p-value

**Correct:** Probability of observing data as extreme or more extreme, assuming H₀ is true.

**Wrong:** Probability that H₀ is true.

## 9.4 Complete Worked Example

**Question:** Does a new drug reduce blood pressure?

- H₀: μ = 0 (no change)
- H₁: μ < 0 (reduction)
- α = 0.05

```python
import numpy as np
from scipy import stats

np.random.seed(42)
# Sample: 20 patients, mean reduction 3, sd 5
data = np.random.normal(-3, 5, 20)
t_stat, p_val = stats.ttest_1samp(data, 0, alternative='less')
print(f"t={t_stat:.3f}, p={p_val:.4f}")
# If p < 0.05: reject H₀
```

**Interpretation:**
- Statistical: p < 0.05 → significant evidence against H₀
- Practical: Effect size (Cohen's d) matters
- Wrong: "There's a 95% chance the drug works"

---

### Chapter 9 — Key Points
- p-value ≠ P(H₀ true)
- Type I vs Type II errors
- Power depends on effect size, n, α
- Statistical ≠ practical significance

### 5 Quick Revision Questions
1. What is a p-value?
2. What is the difference between Type I and Type II errors?
3. What is statistical power?
4. Why is p < 0.05 not proof of practical importance?
5. When do you use a one-sided vs two-sided test?

---

# PART 10 — PARAMETRIC TESTS

## 10.1 Z-Test

**One-sample:** $z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$

**Two-sample:** $z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$

**Assumptions:** Normal population, known σ, large n.

```python
# SciPy doesn't have a dedicated z-test; use formula or statsmodels
from statsmodels.stats.weightstats import ztest
z, p = ztest(data, value=0)
```

## 10.2 t-Tests

### One-Sample t-Test
$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$, df = n−1

```python
t, p = stats.ttest_1samp(data, 0)
```

### Independent Two-Sample t-Test (Pooled)
$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}$

where $s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$

```python
t, p = stats.ttest_ind(group1, group2)  # equal_var=True default
```

### Welch's t-Test (Unequal Variances)
$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}}$

df approximated by Welch–Satterthwaite.

```python
t, p = stats.ttest_ind(group1, group2, equal_var=False)
```

> **Recommendation:** Use Welch's by default unless variances are known equal.

### Paired t-Test
$t = \frac{\bar{d}}{s_d/\sqrt{n}}$, df = n−1

```python
t, p = stats.ttest_rel(before, after)
```

---

### Chapter 10 — Key Points
- t-test for unknown σ, small samples
- Welch's is safer than pooled
- Paired for dependent samples

### 5 Quick Revision Questions
1. When do you use z vs t?
2. What is pooled variance?
3. When is Welch's t-test preferred?
4. What is a paired t-test used for?
5. What are the assumptions of a t-test?

---

# PART 11 — PROPORTION TESTS

## One-Sample Proportion

$z = \frac{\hat{p} - p_0}{\sqrt{p_0(1-p_0)/n}}$

## Binomial Exact Test

```python
from scipy import stats
# H0: p = 0.5, observed 15 successes in 20 trials
result = stats.binomtest(15, 20, 0.5)
print(result.pvalue)
print(result.proportion_ci())
```

## Two-Proportion Test

```python
# Using proportions_ztest from statsmodels
from statsmodels.stats.proportion import proportions_ztest
count = np.array([15, 25])
nobs = np.array([50, 60])
z, p = proportions_ztest(count, nobs)
```

**Exact vs Approximate:** Use exact (binomial) for small samples; approximate (z) for large.

---

### Chapter 11 — Key Points
- `binomtest` for exact inference
- z-test for large samples
- CI for proportion uses Wilson or Clopper-Pearson

### 5 Quick Revision Questions
1. When use exact vs approximate proportion test?
2. What is `binomtest`?
3. How do you test two proportions?
4. What is the CI for a proportion?
5. What sample size is needed for normal approximation?

---

# PART 12 — CHI-SQUARE METHODS

## 12.1 Goodness-of-Fit

$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$

df = k − 1 − (estimated parameters)

```python
observed = np.array([30, 20, 50])
expected = np.array([33.3, 33.3, 33.3])
chi2, p = stats.chisquare(observed, expected)
```

## 12.2 Independence

```python
table = np.array([[10, 20], [30, 40]])
chi2, p, dof, expected = stats.chi2_contingency(table)
```

## 12.3 Fisher's Exact Test

```python
oddsratio, p = stats.fisher_exact(table)
```

**When:** Small sample sizes (expected counts < 5).

## 12.4 Barnard's / Boschloo's Tests

More powerful than Fisher's for 2×2 tables. Available in `scipy.stats` (Barnard via `barnard_exact`, Boschloo via `boschloo_exact` in newer SciPy).

---

### Chapter 12 — Key Points
- Chi-square for categorical association
- Fisher's exact for small samples
- Expected counts ≥ 5 rule for chi-square

### 5 Quick Revision Questions
1. What is the chi-square goodness-of-fit test?
2. What are the assumptions of chi-square?
3. When use Fisher's exact?
4. What is a contingency table?
5. What is the df for a 3×4 table?

---

# PART 13 — ANOVA

## 13.1 Why ANOVA?

Comparing 3+ means with t-tests inflates Type I error. ANOVA tests all at once.

## 13.2 One-Way ANOVA

- **Between-group variation:** $SSB = \sum n_i(\bar{x}_i - \bar{x})^2$
- **Within-group variation:** $SSW = \sum \sum (x_{ij} - \bar{x}_i)^2$
- **Total:** $SST = SSB + SSW$
- **F:** $\frac{MSB}{MSW} = \frac{SSB/(k-1)}{SSW/(N-k)}$

```python
from scipy import stats
group1 = [1, 2, 3, 4]
group2 = [2, 3, 4, 5]
group3 = [3, 4, 5, 6]
F, p = stats.f_oneway(group1, group2, group3)
```

## 13.3 Post-Hoc

Tukey HSD for pairwise comparisons after significant ANOVA. Use `statsmodels`.

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=data, groups=labels, alpha=0.05)
print(tukey)
```

## 13.4 Two-Way ANOVA

Tests two factors and interaction. Use `statsmodels`:

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols
model = ols('y ~ C(A) + C(B) + C(A):C(B)', data=df).fit()
sm.stats.anova_lm(model, typ=2)
```

---

### Chapter 13 — Key Points
- ANOVA tests equality of 3+ means
- F = between/within variance
- Post-hoc needed after significant F
- statsmodels for two-way and Tukey

### 5 Quick Revision Questions
1. Why not use multiple t-tests?
2. What does the F-statistic measure?
3. What is post-hoc testing?
4. What is interaction in two-way ANOVA?
5. What are ANOVA assumptions?

---

# PART 14 — NONPARAMETRIC STATISTICS

## 14.1 Why Nonparametric?

When normality or other assumptions fail.

| Parametric | Nonparametric |
|-----------|---------------|
| t-test (1 sample) | Wilcoxon signed-rank |
| t-test (2 sample) | Mann-Whitney U |
| ANOVA | Kruskal-Wallis |
| Repeated ANOVA | Friedman |
| Pearson | Spearman/Kendall |

## 14.2 Tests

### Mann-Whitney U
```python
u, p = stats.mannwhitneyu(group1, group2)
```

### Wilcoxon Signed-Rank
```python
w, p = stats.wilcoxon(before, after)
```

### Kruskal-Wallis
```python
h, p = stats.kruskal(g1, g2, g3)
```

### Friedman
```python
f, p = stats.friedmanchisquare(g1, g2, g3)
```

### Spearman
```python
rho, p = stats.spearmanr(x, y)
```

### Kendall
```python
tau, p = stats.kendalltau(x, y)
```

## 14.3 Test Selection Rule

| Data | Parametric | Nonparametric |
|------|-----------|---------------|
| 1 sample mean | t-test | Wilcoxon |
| 2 independent | t-test | Mann-Whitney |
| 2 paired | paired t | Wilcoxon signed-rank |
| 3+ independent | ANOVA | Kruskal-Wallis |
| 3+ paired | RM-ANOVA | Friedman |
| Correlation | Pearson | Spearman/Kendall |

---

### Chapter 14 — Key Points
- Nonparametric = rank-based, fewer assumptions
- Less power if parametric assumptions hold
- Use when normality fails or ordinal data

### 5 Quick Revision Questions
1. When use Mann-Whitney vs t-test?
2. What is the nonparametric alternative to ANOVA?
3. What does Spearman measure?
4. When use Friedman test?
5. What is the cost of using nonparametric tests?

---

# PART 15 — NORMALITY AND DISTRIBUTION TESTING

## 15.1 Visual Methods

- **Histogram:** Shape
- **Q-Q plot:** Quantiles vs theoretical quantiles
- **P-P plot:** CDF comparison

```python
import matplotlib.pyplot as plt
from scipy import stats
stats.probplot(data, dist="norm", plot=plt)
plt.show()
```

## 15.2 Tests

| Test | H₀ | SciPy |
|------|-----|-------|
| Shapiro-Wilk | Data normal | `stats.shapiro` |
| D'Agostino-Pearson | Data normal | `stats.normaltest` |
| Anderson-Darling | Data from dist | `stats.anderson` |
| Jarque-Bera | Data normal | `stats.jarque_bera` |
| Kolmogorov-Smirnov | Data from dist | `stats.kstest` |

```python
stat, p = stats.shapiro(data)
print(f"Shapiro: stat={stat:.3f}, p={p:.4f}")
```

**Important:** With large n, even trivial deviations are "significant." Always combine visual + test + context.

---

### Chapter 15 — Key Points
- Q-Q plot is most informative
- Normality tests are sensitive to n
- "Passing" ≠ proof of normality

### 5 Quick Revision Questions
1. What does a Q-Q plot show?
2. Which normality test is best for small samples?
3. Why do large samples often fail normality tests?
4. What is the KS test?
5. Does normality matter for large samples?

---

# PART 16 — HOMOGENEITY / VARIANCE TESTS

| Test | Use When | SciPy |
|------|----------|-------|
| Bartlett | Normal data | `stats.bartlett` |
| Levene | Robust to non-normality | `stats.levene` |
| Fligner-Killeen | Very robust | `stats.fligner` |

```python
stat, p = stats.levene(g1, g2, g3)
stat, p = stats.bartlett(g1, g2, g3)
stat, p = stats.fligner(g1, g2, g3)
```

**Homoscedasticity:** Equal variances.
**Heteroscedasticity:** Unequal variances → use Welch's t-test.

---

### Chapter 16 — Key Points
- Levene is default robust choice
- Bartlett assumes normality
- Fligner-Killeen most robust

### 5 Quick Revision Questions
1. What is homoscedasticity?
2. When use Levene vs Bartlett?
3. What to do if variances are unequal?
4. What is the Fligner-Killeen test?
5. Why does variance equality matter for t-tests?

---

# PART 17 — CORRELATION

## 17.1 Covariance

$\text{Cov}(X,Y) = \frac{1}{n-1}\sum(x_i-\bar{x})(y_i-\bar{y})$

## 17.2 Pearson Correlation

$r = \frac{\text{Cov}(X,Y)}{s_X s_Y}$

- Measures **linear** relationship
- Range: [−1, 1]

```python
r, p = stats.pearsonr(x, y)
```

## 17.3 Spearman Correlation

Rank-based, measures **monotonic** relationship.

```python
rho, p = stats.spearmanr(x, y)
```

## 17.4 Kendall's Tau

Concordant/discordant pairs. More robust for small samples.

```python
tau, p = stats.kendalltau(x, y)
```

## 17.5 Point-Biserial

Correlation between continuous and binary variable.

```python
r, p = stats.pointbiserialr(binary, continuous)
```

## 17.6 Comparison

| Method | Measures | Robust | Use When |
|--------|----------|--------|----------|
| Pearson | Linear | No | Both continuous, normal |
| Spearman | Monotonic | Yes | Ordinal or non-normal |
| Kendall | Monotonic | Yes | Small samples, ties |

**Correlation ≠ Causation.**

---

### Chapter 17 — Key Points
- Pearson for linear, Spearman for monotonic
- Correlation measures association, not causation
- Always visualize before trusting r

### 5 Quick Revision Questions
1. What is the difference between Pearson and Spearman?
2. What does r = 0 mean?
3. When use Kendall's tau?
4. What is point-biserial correlation?
5. Why doesn't correlation imply causation?

---

# PART 18 — REGRESSION

## 18.1 Simple Linear Regression

**Model:** $y = \beta_0 + \beta_1 x + \epsilon$

**Least squares:** Minimize $\sum(y_i - \hat{y}_i)^2$

**Slope:** $\hat{\beta}_1 = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2} = r\frac{s_y}{s_x}$

**Intercept:** $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$

## 18.2 Decomposition

- **SST** = $\sum(y_i-\bar{y})^2$
- **SSR** = $\sum(\hat{y}_i-\bar{y})^2$
- **SSE** = $\sum(y_i-\hat{y}_i)^2$
- SST = SSR + SSE

**R²:** $1 - \frac{SSE}{SST}$

## 18.3 SciPy

```python
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(f"y = {intercept:.2f} + {slope:.2f}x, R²={r_value**2:.3f}")
```

## 18.4 Theil-Sen Regression

Robust to outliers.

```python
from scipy import stats
res = stats.theilslopes(y, x)
print(res)
```

## 18.5 Assumptions

- Linearity
- Independence of errors
- Homoscedasticity
- Normality of residuals (for inference)

**Use statsmodels for advanced regression** (multiple, logistic, etc.).

---

### Chapter 18 — Key Points
- Least squares minimizes SSE
- R² = proportion of variance explained
- Check residual diagnostics
- Theil-Sen for robust regression

### 5 Quick Revision Questions
1. What does R² measure?
2. What are the assumptions of linear regression?
3. How is the slope related to correlation?
4. When use Theil-Sen?
5. Why use statsmodels over SciPy for regression?

---

# PART 19 — EFFECT SIZE

| Measure | Formula | Interpretation |
|---------|---------|---------------|
| Cohen's d | $\frac{\bar{x}_1-\bar{x}_2}{s_p}$ | 0.2 small, 0.5 medium, 0.8 large |
| Pearson r | | 0.1 small, 0.3 medium, 0.5 large |
| Odds ratio | $\frac{a/b}{c/d}$ | 1 = no effect |
| Relative risk | $\frac{P(E|T)}{P(E|C)}$ | 1 = no effect |
| Cramér's V | $\sqrt{\frac{\chi^2}{n\min(k-1,r-1)}}$ | 0–1 |
| Eta squared | $\frac{SSB}{SST}$ | Proportion variance explained |

**Statistical significance ≠ practical significance.**

```python
def cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    s_p = np.sqrt(((n1-1)*np.var(g1, ddof=1) + (n2-1)*np.var(g2, ddof=1))/(n1+n2-2))
    return (np.mean(g1) - np.mean(g2)) / s_p
```

---

### Chapter 19 — Key Points
- Effect size measures magnitude, not just existence
- Always report effect size with p-value
- Large n can make tiny effects significant

### 5 Quick Revision Questions
1. What is Cohen's d?
2. Interpret d = 0.5.
3. What is an odds ratio?
4. Why report effect size?
5. What is Cramér's V used for?

---

# PART 20 — RESAMPLING

## 20.1 Bootstrap

**Idea:** Resample with replacement from data to estimate sampling distribution.

```python
from scipy import stats
data = np.random.exponential(3, 100)
res = stats.bootstrap((data,), np.mean, n_resamples=10000, confidence_level=0.95)
print(res.confidence_interval)
```

**CI Types:** Percentile, Basic, BCa.

## 20.2 Permutation Test

**Idea:** Shuffle labels to break association, compute test statistic distribution.

```python
def diff_means(x, y):
    return np.mean(x) - np.mean(y)

res = stats.permutation_test((g1, g2), diff_means, n_resamples=10000)
print(res.pvalue)
```

## 20.3 Monte Carlo Test

Simulate data under H₀ many times, compare observed statistic.

```python
res = stats.monte_carlo_test(data, rvs=stats.norm.rvs, statistic=np.mean)
```

## 20.4 Comparison

| Method | Purpose | Assumption |
|--------|---------|-----------|
| Bootstrap | CI, SE | Representative sample |
| Permutation | p-value | Exchangeability |
| Monte Carlo | p-value | Known null distribution |

---

### Chapter 20 — Key Points
- Bootstrap estimates uncertainty without formulas
- Permutation tests exact under exchangeability
- Monte Carlo simulates null distribution

### 5 Quick Revision Questions
1. How does bootstrap work?
2. What is exchangeability?
3. When use permutation vs bootstrap?
4. What is a Monte Carlo test?
5. What are the limitations of bootstrap?

---

# PART 21 — MULTIPLE HYPOTHESIS TESTING

## 21.1 Problem

Testing many hypotheses inflates false positives.

**FWER:** Probability of at least one Type I error.

## 21.2 Corrections

- **Bonferroni:** $\alpha_{adj} = \alpha/m$ (conservative)
- **Holm:** Step-down Bonferroni (more powerful)
- **Benjamini-Hochberg (FDR):** Controls expected proportion of false discoveries

```python
from scipy import stats
pvals = [0.01, 0.02, 0.03, 0.04, 0.05]
adjusted = stats.false_discovery_control(pvals, method='bh')
print(adjusted)
```

**When FDR > FWER:** Genomics, neuroimaging, exploratory analysis — where false negatives are costly.

---

### Chapter 21 — Key Points
- Multiple testing inflates false positives
- Bonferroni controls FWER, BH controls FDR
- FDR more powerful for large-scale testing

### 5 Quick Revision Questions
1. What is the multiple testing problem?
2. What is FWER?
3. How does Bonferroni work?
4. What is FDR?
5. When prefer FDR over FWER?

---

# PART 22 — DISTRIBUTION FITTING

## 22.1 Process

1. Choose candidate distributions
2. Fit parameters (MLE)
3. Assess goodness-of-fit
4. Compare with AIC/BIC

```python
from scipy import stats
data = np.random.gamma(2, 2, 1000)

# Fit gamma
a, loc, scale = stats.gamma.fit(data)
print(f"Gamma: a={a:.2f}, loc={loc:.2f}, scale={scale:.2f}")

# Compare with normal
mu, sigma = stats.norm.fit(data)
# Compute log-likelihood
ll_gamma = np.sum(stats.gamma.logpdf(data, a, loc, scale))
ll_norm = np.sum(stats.norm.logpdf(data, mu, sigma))
print(f"Log-lik Gamma: {ll_gamma:.1f}, Normal: {ll_norm:.1f}")
```

## 22.2 AIC/BIC

$AIC = 2k - 2\ln(L)$
$BIC = k\ln(n) - 2\ln(L)$

Lower is better. BIC penalizes complexity more.

---

### Chapter 22 — Key Points
- `.fit()` uses MLE
- Compare candidates with AIC/BIC
- Q-Q plot for visual check

### 5 Quick Revision Questions
1. How does SciPy fit distributions?
2. What is AIC?
3. What is BIC?
4. How to check goodness-of-fit?
5. What is the difference between AIC and BIC?

---

# PART 23 — TRANSFORMATIONS

| Transform | Formula | Use When |
|-----------|---------|----------|
| Log | $y = \log(x)$ | Right skew, multiplicative |
| Square root | $y = \sqrt{x}$ | Count data, moderate skew |
| Reciprocal | $y = 1/x$ | Extreme skew |
| Box-Cox | $y = \frac{x^\lambda-1}{\lambda}$ | Positive data, find optimal λ |
| Yeo-Johnson | Extension of Box-Cox | Allows zero/negative |

```python
from scipy import stats
data = np.random.exponential(2, 100)

# Box-Cox (requires positive data)
transformed, lambda_ = stats.boxcox(data)
print(f"Optimal λ: {lambda_:.3f}")

# Yeo-Johnson (allows negative)
transformed_yj, lambda_yj = stats.yeojohnson(data)
print(f"YJ λ: {lambda_yj:.3f}")
```

**When useful:** Stabilize variance, make data more normal, linearize relationships.

**Limitations:** Changes interpretation, not always invertible, can create zeros.

---

### Chapter 23 — Key Points
- Transformations fix skewness/variance
- Box-Cox finds optimal power transform
- Yeo-Johnson works with negatives

### 5 Quick Revision Questions
1. When use log transform?
2. What does Box-Cox do?
3. What is the difference between Box-Cox and Yeo-Johnson?
4. What are the limitations of transformations?
5. How do you interpret transformed coefficients?

---

# PART 24 — KDE AND EMPIRICAL DISTRIBUTIONS

## 24.1 Kernel Density Estimation (KDE)

**Formula:** $\hat{f}(x) = \frac{1}{nh}\sum_{i=1}^n K\left(\frac{x-x_i}{h}\right)$

- $K$ = kernel (usually Gaussian)
- $h$ = bandwidth (smoothing)

```python
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)
kde = stats.gaussian_kde(data)

x_grid = np.linspace(-4, 4, 200)
plt.hist(data, bins=30, density=True, alpha=0.5)
plt.plot(x_grid, kde(x_grid))
plt.show()

# Bandwidth
print(f"Bandwidth: {kde.factor:.3f}")
```

## 24.2 ECDF

**Definition:** $\hat{F}(x) = \frac{1}{n}\sum_{i=1}^n I(x_i \leq x)$

```python
ecdf = stats.ecdf(data)
ecdf.cdf.plot()
plt.show()
```

**Comparison:**

| Method | Smoothness | Parameters | Use |
|--------|-----------|-----------|-----|
| Histogram | Binned | bin width | Quick look |
| KDE | Smooth | bandwidth | Density estimation |
| ECDF | Step function | None | Exact cumulative |

---

### Chapter 24 — Key Points
- KDE smooths histogram into continuous density
- Bandwidth controls smoothness
- ECDF is exact cumulative distribution

### 5 Quick Revision Questions
1. What does KDE estimate?
2. What is bandwidth?
3. What is ECDF?
4. How does KDE differ from histogram?
5. When use ECDF vs KDE?

---

# PART 25 — SURVIVAL ANALYSIS

## 25.1 Concepts

- **Time-to-event data:** Time until event (death, failure)
- **Censoring:** Event not observed (still alive, lost to follow-up)
- **Survival function:** $S(t) = P(T > t)$
- **Hazard function:** $h(t) = \lim_{\Delta t \to 0} \frac{P(t \leq T < t+\Delta t | T \geq t)}{\Delta t}$

## 25.2 SciPy

- Weibull: `stats.weibull_min`
- Exponential: `stats.expon`
- Log-normal: `stats.lognorm`

```python
# Weibull survival
shape, loc, scale = 1.5, 0, 10
t = np.linspace(0, 30, 100)
survival = stats.weibull_min.sf(t, shape, loc, scale)
```

**For full survival analysis:** Use `lifelines` library (Kaplan-Meier, Cox regression, log-rank test).

---

### Chapter 25 — Key Points
- Survival analysis handles censored data
- SciPy has distributions; lifelines has full toolkit
- Hazard is instantaneous risk

### 5 Quick Revision Questions
1. What is censoring?
2. What is the survival function?
3. What is the hazard function?
4. Which SciPy distributions are used in survival?
5. What library for Kaplan-Meier?

---

# PART 26 — INFORMATION THEORY

## 26.1 Entropy

$H(X) = -\sum p(x)\log p(x)$

Measures uncertainty. Max for uniform.

```python
from scipy import stats
p = np.array([0.25, 0.25, 0.25, 0.25])
print(stats.entropy(p))  # log(4) = 1.386
```

## 26.2 KL Divergence

$D_{KL}(P||Q) = \sum p(x)\log\frac{p(x)}{q(x)}$

Asymmetric. Measures information lost when Q approximates P.

```python
p = np.array([0.5, 0.5])
q = np.array([0.9, 0.1])
print(stats.entropy(p, q))  # KL(P||Q)
```

## 26.3 Cross-Entropy

$H(P,Q) = -\sum p(x)\log q(x) = H(P) + D_{KL}(P||Q)$

**In ML:** Cross-entropy loss for classification.

```python
# Cross-entropy
print(stats.entropy(p, q))  # same as KL for normalized
```

## 26.4 Mutual Information

$I(X;Y) = H(X) - H(X|Y)$

**In ML:** Feature selection, decision trees.

---

### Chapter 26 — Key Points
- Entropy = uncertainty
- KL = information gain/loss
- Cross-entropy = standard ML loss

### 5 Quick Revision Questions
1. What is entropy?
2. What is KL divergence?
3. Why is KL asymmetric?
4. What is cross-entropy in ML?
5. What is mutual information?

---

# PART 27 — MULTIVARIATE STATISTICS

## 27.1 Mean Vector & Covariance Matrix

$\mathbf{\mu} = [\mu_1, \ldots, \mu_p]^T$

$\Sigma = \begin{bmatrix} \sigma_1^2 & \sigma_{12} & \cdots \\ \sigma_{21} & \sigma_2^2 & \cdots \\ \vdots & & \ddots \end{bmatrix}$

```python
data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 2]], 1000)
print(np.mean(data, axis=0))    # mean vector
print(np.cov(data.T))           # covariance matrix
print(np.corrcoef(data.T))      # correlation matrix
```

## 27.2 Mahalanobis Distance

$D_M(\mathbf{x}) = \sqrt{(\mathbf{x}-\mu)^T\Sigma^{-1}(\mathbf{x}-\mu)}$

Accounts for correlations. Used in outlier detection.

```python
def mahalanobis(x, mean, cov):
    diff = x - mean
    return np.sqrt(diff @ np.linalg.inv(cov) @ diff.T)
```

## 27.3 Multivariate Normal

```python
mvn = stats.multivariate_normal([0, 0], [[1, 0.5], [0.5, 2]])
print(mvn.pdf([0, 0]))
samples = mvn.rvs(100)
```

---

### Chapter 27 — Key Points
- Covariance matrix captures pairwise relationships
- Mahalanobis accounts for correlations
- Multivariate normal is foundation

### 5 Quick Revision Questions
1. What is a covariance matrix?
2. What does Mahalanobis distance measure?
3. How does multivariate normal generalize normal?
4. What is the role of correlation matrix?
5. How to detect multivariate outliers?

---

# PART 28 — DIRECTIONAL STATISTICS

## 28.1 Why Special?

Angles (0° and 360° are the same) can't be averaged linearly.

## 28.2 Circular Mean

$\bar{\theta} = \text{atan2}\left(\frac{1}{n}\sum\sin\theta_i, \frac{1}{n}\sum\cos\theta_i\right)$

## 28.3 Circular Variance

$V = 1 - \bar{R}$ where $\bar{R} = \sqrt{\left(\frac{1}{n}\sum\cos\theta_i\right)^2 + \left(\frac{1}{n}\sum\sin\theta_i\right)^2}$

```python
from scipy import stats
angles = np.array([10, 20, 30, 350, 355])  # degrees
angles_rad = np.deg2rad(angles)
mean_angle = stats.circmean(angles_rad)
print(f"Circular mean: {np.rad2deg(mean_angle):.2f}°")
print(f"Circular variance: {stats.circvar(angles_rad):.4f}")
print(f"Circular std: {np.rad2deg(stats.circstd(angles_rad)):.2f}°")
```

**SciPy functions:** `circmean`, `circvar`, `circstd`, `circ_kappa`, `vonmises`

---

### Chapter 28 — Key Points
- Circular data needs special methods
- Circular mean uses vector addition
- SciPy has `circmean`, `circvar`, `circstd`

### 5 Quick Revision Questions
1. Why can't we average angles normally?
2. How is circular mean computed?
3. What is circular variance?
4. When use directional statistics?
5. What distribution models circular data?

---

# PART 29 — ADVANCED SCIpy.STATS TOPICS

| Topic | SciPy Function/Module | Use |
|-------|----------------------|-----|
| Quasi-Monte Carlo | `stats.qmc` | Low-discrepancy sequences |
| Random variable sampling | `.rvs()` | Simulation |
| Noncentral distributions | `stats.ncf`, `stats.nct`, `stats.ncchi2` | Power analysis |
| Extreme value | `stats.genextreme`, `stats.genpareto` | Risk management |
| Order statistics | `stats.order_stats` | Min/max distributions |
| Robust statistics | `stats.median_abs_deviation` | Outlier-resistant |
| Contingency measures | `stats.contingency` | Categorical association |
| Statistical distances | `stats.wasserstein_distance`, `stats.energy_distance` | Distribution comparison |

```python
# Wasserstein distance
from scipy import stats
x = np.random.normal(0, 1, 100)
y = np.random.normal(1, 1, 100)
print(stats.wasserstein_distance(x, y))

# Energy distance
print(stats.energy_distance(x, y))
```

---

# PART 30 — SCIpy.STATS API GUIDE

## Descriptive

| Function | Purpose | Syntax | Example |
|----------|---------|--------|---------|
| `describe` | Summary stats | `stats.describe(a)` | `stats.describe([1,2,3])` |
| `gmean` | Geometric mean | `stats.gmean(a)` | `stats.gmean([1,2,4])` |
| `hmean` | Harmonic mean | `stats.hmean(a)` | `stats.hmean([1,2,4])` |
| `mode` | Mode | `stats.mode(a)` | `stats.mode([1,2,2])` |
| `skew` | Skewness | `stats.skew(a)` | |
| `kurtosis` | Kurtosis | `stats.kurtosis(a)` | |
| `moment` | Moments | `stats.moment(a, order)` | |
| `iqr` | IQR | `stats.iqr(a)` | |
| `median_abs_deviation` | MAD | `stats.median_abs_deviation(a)` | |
| `sem` | Standard error | `stats.sem(a)` | |
| `variation` | CV | `stats.variation(a)` | |
| `trim_mean` | Trimmed mean | `stats.trim_mean(a, 0.1)` | |
| `zscore` | Z-scores | `stats.zscore(a)` | |

## Distributions (all follow same pattern)

```python
dist = stats.norm(loc=0, scale=1)
dist.pdf(x)    # density
dist.cdf(x)    # cumulative
dist.ppf(q)    # inverse CDF
dist.rvs(size) # random samples
dist.mean()    # mean
dist.var()     # variance
dist.fit(data) # MLE fit
```

Common distributions: `norm`, `binom`, `poisson`, `uniform`, `expon`, `gamma`, `beta`, `chi2`, `t`, `f`, `lognorm`, `weibull_min`, `bernoulli`, `geom`, `nbinom`, `hypergeom`, `multinomial`, `multivariate_normal`, `dirichlet`, `cauchy`, `logistic`, `laplace`, `pareto`, `gumbel_r`, `genextreme`, `genpareto`, `rayleigh`

## Tests

| Function | Purpose | Syntax |
|----------|---------|--------|
| `ttest_1samp` | One-sample t | `stats.ttest_1samp(a, popmean)` |
| `ttest_ind` | Two-sample t | `stats.ttest_ind(a, b)` |
| `ttest_rel` | Paired t | `stats.ttest_rel(a, b)` |
| `binomtest` | Exact binomial | `stats.binomtest(k, n, p)` |
| `chisquare` | Goodness-of-fit | `stats.chisquare(f_obs, f_exp)` |
| `chi2_contingency` | Independence | `stats.chi2_contingency(table)` |
| `fisher_exact` | Fisher exact | `stats.fisher_exact(table)` |
| `f_oneway` | ANOVA | `stats.f_oneway(g1, g2, g3)` |
| `mannwhitneyu` | Mann-Whitney | `stats.mannwhitneyu(a, b)` |
| `wilcoxon` | Wilcoxon | `stats.wilcoxon(a, b)` |
| `kruskal` | Kruskal-Wallis | `stats.kruskal(g1, g2, g3)` |
| `friedmanchisquare` | Friedman | `stats.friedmanchisquare(g1, g2, g3)` |
| `shapiro` | Shapiro-Wilk | `stats.shapiro(data)` |
| `normaltest` | D'Agostino | `stats.normaltest(data)` |
| `anderson` | Anderson-Darling | `stats.anderson(data)` |
| `jarque_bera` | Jarque-Bera | `stats.jarque_bera(data)` |
| `kstest` | KS test | `stats.kstest(data, 'norm')` |
| `ks_2samp` | Two-sample KS | `stats.ks_2samp(a, b)` |
| `bartlett` | Bartlett | `stats.bartlett(g1, g2)` |
| `levene` | Levene | `stats.levene(g1, g2)` |
| `fligner` | Fligner | `stats.fligner(g1, g2)` |
| `pearsonr` | Pearson | `stats.pearsonr(x, y)` |
| `spearmanr` | Spearman | `stats.spearmanr(x, y)` |
| `kendalltau` | Kendall | `stats.kendalltau(x, y)` |
| `linregress` | Linear regression | `stats.linregress(x, y)` |

## Resampling

| Function | Purpose | Syntax |
|----------|---------|--------|
| `bootstrap` | Bootstrap CI | `stats.bootstrap((data,), np.mean)` |
| `permutation_test` | Permutation | `stats.permutation_test((a,b), stat)` |
| `monte_carlo_test` | Monte Carlo | `stats.monte_carlo_test(data, rvs, stat)` |
| `power` | Power calculation | `stats.power(...)` |

## Other

| Function | Purpose |
|----------|---------|
| `false_discovery_control` | FDR correction |
| `combine_pvalues` | Combine p-values |
| `boxcox` | Box-Cox transform |
| `yeojohnson` | Yeo-Johnson transform |
| `gaussian_kde` | KDE |
| `ecdf` | Empirical CDF |
| `entropy` | Entropy/KL |
| `wasserstein_distance` | Wasserstein distance |
| `circmean`, `circvar`, `circstd` | Circular statistics |
| `theilslopes` | Theil-Sen regression |
| `siegelslopes` | Siegel regression |

---

# PART 31 — TEST SELECTION CHEAT SHEET

## Comparing Means

| Question | Groups | Independent? | Parametric? | Test |
|----------|--------|-------------|-------------|------|
| One mean vs known | 1 | — | Yes | One-sample t |
| Two means | 2 | Yes | Yes | Independent t / Welch |
| Two means | 2 | No | Yes | Paired t |
| 3+ means | 3+ | Yes | Yes | One-way ANOVA |
| 3+ means | 3+ | No | Yes | Repeated measures ANOVA |
| Two means | 2 | Yes | No | Mann-Whitney U |
| Two means | 2 | No | No | Wilcoxon signed-rank |
| 3+ means | 3+ | Yes | No | Kruskal-Wallis |
| 3+ means | 3+ | No | No | Friedman |

## Comparing Categorical Variables

| Table | Test |
|-------|------|
| 2×2, large n | Chi-square |
| 2×2, small n | Fisher's exact |
| r×c | Chi-square |

## Testing Relationships

| Data | Test |
|------|------|
| Both continuous, normal | Pearson |
| Ordinal / non-normal | Spearman |
| Small sample / ties | Kendall |
| Continuous + binary | Point-biserial |

## Checking Distributions

| Question | Test |
|----------|------|
| Is data normal? | Shapiro-Wilk (small), D'Agostino (large) |
| Same distribution? | KS 2-sample |
| Specific distribution? | KS 1-sample |

## Comparing Variances

| Question | Test |
|----------|------|
| Normal data | Bartlett |
| Non-normal | Levene |
| Very non-normal | Fligner-Killeen |

---

# PART 32 — FORMULA SHEET

| Concept | Formula |
|---------|---------|
| Mean | $\bar{x} = \frac{1}{n}\sum x_i$ |
| Weighted mean | $\frac{\sum w_i x_i}{\sum w_i}$ |
| Geometric mean | $(\prod x_i)^{1/n}$ |
| Harmonic mean | $\frac{n}{\sum 1/x_i}$ |
| Variance (sample) | $s^2 = \frac{\sum(x_i-\bar{x})^2}{n-1}$ |
| SD | $s = \sqrt{s^2}$ |
| CV | $s/\bar{x}$ |
| IQR | $Q_3 - Q_1$ |
| MAD | $\text{median}(|x_i-\text{median}(x)|)$ |
| Z-score | $z = (x-\bar{x})/s$ |
| Covariance | $\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{n-1}$ |
| Pearson r | $\frac{\text{Cov}(X,Y)}{s_X s_Y}$ |
| P(A∪B) | P(A)+P(B)−P(A∩B) |
| P(A∩B) | P(A)P(B|A) |
| P(A|B) | P(A∩B)/P(B) |
| Bayes | $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$ |
| E[X] | $\sum xP(X=x)$ |
| Var(X) | $E[X^2]-(E[X])^2$ |
| Binomial PMF | $\binom{n}{k}p^k(1-p)^{n-k}$ |
| Poisson PMF | $\frac{\lambda^k e^{-\lambda}}{k!}$ |
| Normal PDF | $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ |
| Exponential PDF | $\lambda e^{-\lambda x}$ |
| Beta PDF | $\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$ |
| Gamma PDF | $\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}$ |
| CI (mean, σ known) | $\bar{x} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$ |
| CI (mean, σ unknown) | $\bar{x} \pm t_{\alpha/2,n-1}\frac{s}{\sqrt{n}}$ |
| t statistic | $\frac{\bar{x}-\mu_0}{s/\sqrt{n}}$ |
| z statistic | $\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}$ |
| Chi-square | $\sum\frac{(O-E)^2}{E}$ |
| F statistic | $\frac{MSB}{MSW}$ |
| ANOVA SSB | $\sum n_i(\bar{x}_i-\bar{x})^2$ |
| ANOVA SSW | $\sum\sum(x_{ij}-\bar{x}_i)^2$ |
| Regression slope | $r\frac{s_y}{s_x}$ |
| Regression intercept | $\bar{y}-\hat{\beta}_1\bar{x}$ |
| R² | $1-\frac{SSE}{SST}$ |
| Cohen's d | $\frac{\bar{x}_1-\bar{x}_2}{s_p}$ |
| Odds ratio | $\frac{a/b}{c/d}$ |
| Relative risk | $\frac{P(E|T)}{P(E|C)}$ |
| Entropy | $-\sum p\log p$ |
| KL divergence | $\sum p\log(p/q)$ |

---

# PART 33 — FINAL REVISION TABLES

## 1. All Distributions at a Glance

| Distribution | Type | Mean | Variance | Use |
|-------------|------|------|----------|-----|
| Bernoulli | Discrete | p | p(1−p) | Yes/no |
| Binomial | Discrete | np | np(1−p) | Successes |
| Geometric | Discrete | 1/p | (1−p)/p² | Trials to success |
| Poisson | Discrete | λ | λ | Events/interval |
| Uniform | Continuous | (a+b)/2 | (b−a)²/12 | Equal likelihood |
| Normal | Continuous | μ | σ² | Natural phenomena |
| Exponential | Continuous | 1/λ | 1/λ² | Time between events |
| Gamma | Continuous | α/β | α/β² | Sum of exponentials |
| Beta | Continuous | α/(α+β) | — | Probabilities |
| Chi-square | Continuous | k | 2k | Variance tests |
| t | Continuous | 0 | k/(k−2) | Small sample mean |
| F | Continuous | — | — | Variance ratio |

## 2. All Statistical Tests at a Glance

| Test | Purpose | SciPy |
|------|---------|-------|
| t-test | Compare means | `ttest_1samp`, `ttest_ind`, `ttest_rel` |
| ANOVA | Compare 3+ means | `f_oneway` |
| Chi-square | Categorical association | `chisquare`, `chi2_contingency` |
| Fisher exact | Small 2×2 | `fisher_exact` |
| Mann-Whitney | Nonparametric 2-sample | `mannwhitneyu` |
| Wilcoxon | Nonparametric paired | `wilcoxon` |
| Kruskal-Wallis | Nonparametric ANOVA | `kruskal` |
| Friedman | Nonparametric RM | `friedmanchisquare` |
| Shapiro-Wilk | Normality | `shapiro` |
| Levene | Variance equality | `levene` |
| Pearson | Linear correlation | `pearsonr` |
| Spearman | Monotonic correlation | `spearmanr` |
| Kendall | Rank correlation | `kendalltau` |

## 3. Which Test Should I Use?

```
Is the outcome continuous?
├── Yes → Comparing means?
│   ├── 1 group → t-test
│   ├── 2 groups → Independent? → t-test / Mann-Whitney
│   └── 3+ groups → ANOVA / Kruskal-Wallis
└── No (categorical) → Chi-square / Fisher
```

## 4. Parametric vs Nonparametric

| Parametric | Nonparametric |
|-----------|---------------|
| Assumes distribution | Distribution-free |
| More power if assumptions hold | Less power |
| t-test, ANOVA, Pearson | Mann-Whitney, Kruskal-Wallis, Spearman |

## 5. Pearson vs Spearman vs Kendall

| | Pearson | Spearman | Kendall |
|---|---------|----------|---------|
| Measures | Linear | Monotonic | Monotonic |
| Robust | No | Yes | Yes |
| Small samples | OK | OK | Better |
| Ties | Bad | OK | OK |

## 6. t-test vs z-test

| | t-test | z-test |
|---|--------|--------|
| σ | Unknown | Known |
| Sample | Small | Large |
| Distribution | t | Normal |

## 7. ANOVA vs Kruskal-Wallis

| | ANOVA | Kruskal-Wallis |
|---|-------|----------------|
| Parametric | Yes | No |
| Assumes normality | Yes | No |
| Power | Higher if normal | Lower if normal |

## 8. Chi-square vs Fisher Exact

| | Chi-square | Fisher |
|---|-----------|--------|
| Sample | Large | Small |
| Expected counts | ≥5 | <5 |
| Exact | No | Yes |

## 9. Bootstrap vs Permutation

| | Bootstrap | Permutation |
|---|-----------|-------------|
| Purpose | CI, SE | p-value |
| Resampling | With replacement | Without replacement (shuffle) |
| Assumption | Representative sample | Exchangeability |

## 10. SD vs SEM

| | SD | SEM |
|---|-----|-----|
| Measures | Data spread | Precision of mean |
| Formula | $\sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}$ | $s/\sqrt{n}$ |
| Decreases with n | No | Yes |

## 11. Variance vs SD

| | Variance | SD |
|---|----------|-----|
| Units | Squared | Original |
| Interpretability | Low | High |
| Formula | $s^2$ | $\sqrt{s^2}$ |

## 12. Confidence Interval vs Prediction Interval

| | CI | PI |
|---|-----|-----|
| Estimates | Parameter | Individual value |
| Width | Narrower | Wider |

## 13. Correlation vs Regression

| | Correlation | Regression |
|---|-------------|------------|
| Purpose | Measure association | Predict |
| Symmetric | Yes | No |
| Units | None | Slope has units |

## 14. Statistical vs Practical Significance

| | Statistical | Practical |
|---|-------------|-----------|
| Measured by | p-value | Effect size |
| Depends on n | Yes | No |
| Real-world impact | Not necessarily | Yes |

## 15. SciPy vs NumPy vs statsmodels vs scikit-learn

| Library | Use For |
|---------|---------|
| NumPy | Arrays, basic math |
| SciPy | Statistical distributions, tests |
| statsmodels | Regression, ANOVA, time series |
| scikit-learn | ML models, preprocessing |

---

# PART 34 — PRACTICAL DATA SCIENCE EXAMPLES

## A/B Testing

```python
# Conversion rates: A vs B
conversions = np.array([120, 150])
visitors = np.array([1000, 1000])

from statsmodels.stats.proportion import proportions_ztest
z, p = proportions_ztest(conversions, visitors)
print(f"z={z:.3f}, p={p:.4f}")

# Effect size: relative lift
lift = (150/1000 - 120/1000) / (120/1000)
print(f"Relative lift: {lift:.2%}")
```

## Customer Churn Prediction

```python
# Compare tenure between churned and retained
churned = np.random.exponential(10, 200)
retained = np.random.exponential(30, 800)

t, p = stats.ttest_ind(churned, retained, equal_var=False)
print(f"Welch t={t:.3f}, p={p:.4f}")

# Effect size
d = (np.mean(retained) - np.mean(churned)) / np.sqrt((np.var(churned)+np.var(retained))/2)
print(f"Cohen's d={d:.3f}")
```

## Medical Data

```python
# Diagnostic test evaluation
# TP=80, FP=20, FN=10, TN=890
table = np.array([[80, 20], [10, 890]])
oddsratio, p = stats.fisher_exact(table)
print(f"Odds ratio: {oddsratio:.2f}, p={p:.4f}")

sensitivity = 80 / (80 + 10)
specificity = 890 / (890 + 20)
print(f"Sensitivity: {sensitivity:.2%}, Specificity: {specificity:.2%}")
```

## Finance

```python
# Value at Risk (VaR) using normal assumption
returns = np.random.normal(0.001, 0.02, 1000)
var_95 = np.percentile(returns, 5)
print(f"95% VaR: {var_95:.4f}")

# Or using normal
var_95_norm = stats.norm.ppf(0.05, np.mean(returns), np.std(returns))
print(f"Normal VaR: {var_95_norm:.4f}")
```

## Manufacturing Quality Control

```python
# Control chart: monitor process mean
measurements = np.random.normal(100, 2, 50)
xbar = np.mean(measurements)
s = np.std(measurements, ddof=1)
ucl = xbar + 3 * s / np.sqrt(len(measurements))
lcl = xbar - 3 * s / np.sqrt(len(measurements))
print(f"Control limits: [{lcl:.2f}, {ucl:.2f}]")
```

## NLP / Text Classification

```python
# Naive Bayes: word count distribution
# Using multinomial distribution for word frequencies
from scipy import stats
# P(word count | class)
n_words = 100
p_word = 0.01
dist = stats.binom(n_words, p_word)
print(f"P(5 occurrences): {dist.pmf(5):.4f}")
```

---

# FINAL SECTION — COMPLETE LEARNING MAP

```
Statistics
├── Descriptive Statistics
│   ├── Central Tendency (mean, median, mode)
│   ├── Dispersion (variance, SD, IQR)
│   ├── Position (percentiles, z-scores)
│   ├── Outliers (IQR, z-score, MAD)
│   └── Shape (skewness, kurtosis)
├── Probability
│   ├── Basic rules
│   ├── Conditional probability
│   └── Bayes theorem
├── Random Variables
│   ├── Discrete (PMF)
│   ├── Continuous (PDF)
│   ├── CDF, SF, PPF
│   └── Expectation, Variance
├── Distributions
│   ├── Discrete (Binomial, Poisson, ...)
│   ├── Continuous (Normal, Exponential, ...)
│   └── Multivariate (MVN, Dirichlet, ...)
├── Sampling
│   ├── Methods
│   ├── Sampling distribution
│   └── CLT, LLN
├── Estimation
│   ├── Point estimation
│   └── MLE
├── Confidence Intervals
├── Hypothesis Testing
│   ├── Framework
│   ├── Parametric tests (t, z)
│   ├── Proportion tests
│   ├── Chi-square
│   ├── ANOVA
│   └── Nonparametric tests
├── Correlation
├── Regression
├── Effect Sizes
├── Resampling
│   ├── Bootstrap
│   ├── Permutation
│   └── Monte Carlo
├── Multiple Testing
├── Distribution Fitting
├── Transformations
├── KDE / ECDF
├── Survival Analysis
├── Information Theory
├── Multivariate Statistics
└── Advanced Modeling
```

---

## What I Must Memorize vs Understand vs Look Up

### Must Memorize

- Mean, variance, SD formulas
- Sample vs population variance (n−1)
- Z-score formula
- Normal PDF, Binomial PMF, Poisson PMF
- Bayes theorem
- CLT statement
- CI formulas (z and t)
- t-test, chi-square, F formulas
- Pearson correlation formula
- R² definition
- Cohen's d
- Entropy, KL divergence

### Must Understand

- Why n−1 for sample variance
- Difference between SD and SEM
- p-value meaning (and what it's NOT)
- Type I vs Type II errors
- When to use each test
- Assumptions and what happens when violated
- CLT intuition
- Bootstrap vs permutation
- Statistical vs practical significance
- Correlation vs causation

### Can Look Up

- Exact SciPy function syntax
- Full list of distributions
- Specific test variations
- Advanced multivariate methods
- Survival analysis functions
- Specialized nonparametric tests
- AIC/BIC formulas
- Box-Cox derivation
- Directional statistics details
- Extreme value theory details

---

## Final Words

> **Statistics is not about running functions. It is about understanding uncertainty, quantifying evidence, and making decisions under incomplete information.**

> **SciPy is your calculator. Your brain is your statistical reasoning engine.**

> **Always ask: What is the question? What is the data? What are the assumptions? What does the result mean in context?**

---

*End of Complete Statistics + SciPy Study Notes*
