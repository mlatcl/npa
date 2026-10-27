---
title: "Tutorial 1"
practical: 1
layout: practical
assignment: True
notespdf: False
tex_template: exercise
posts: True
ipynb: True
reveal: False
docx: False
pptx: False
date: 2006-09-26
abstract: >
  Poisson counts for falling leaves, expectations under a small discrete
  distribution, the Poisson second moment, and sample means from Gaussian
  and exponential draws. Originally COM4290/6131 Tutorial 1; MATLAB
  calls are rewritten in Python.
---

\section{Tutorial 1}

\notes{COM4290/6131, University of Sheffield, 2006. Computational parts originally used MATLAB (`randn`, `plot`, `errorbar`, and `exponentialSamp.m`). Use the helpers in `python/npa_plots.py`.}

\include{snippets/_npa/includes/npa-python-setup.md}

\section{Falling leaves}

\notes{Leaves fall from a tree as a Poisson process at a rate of one every minute.}

\notes{1. You arrive at 16:00. During the next ten minutes, what is the probability that you see twelve leaves fall?}

\notes{2. What is the probability that you see $n$ leaves fall for $n=0,\ldots,20$? Plot the results.}

\code{from scipy.stats import poisson
lam, t = 1.0, 10.0
n = np.arange(0, 21)
p = poisson.pmf(n, lam * t)
print("P(k=12) =", poisson.pmf(12, lam * t))
plt.stem(n, p)
plt.xlabel("$n$")
plt.ylabel(r"$P(n\mid\lambda t=10)$")
plt.show()}

\notes{3. Where does the curve peak? Compare the peak with the expected value $\lambda t$.}

\section{A four-point distribution}

\notes{$X$ takes four values with probabilities}

$X$ | 1 | 2 | 3 | 4
--- | --- | --- | --- | ---
$P(X)$ | 0.05 | 0.2 | 0.3 | 0.45

\notes{1. What is the mean of $X$?}

\notes{2. What is the standard deviation of $X$?}

\notes{3. What is the expectation of $\ln X$?}

\section{Poisson second moment}

\notes{Show that
$$
\langle n^2\rangle=\lambda t\, e^{-\lambda t}\sum_{n=1}^{\infty}\frac{n(\lambda t)^{n-1}}{(n-1)!},
$$
where the expectation is under a Poisson distribution. Then, substituting $m=n-1$, show that
$$
\langle n^2\rangle=(\lambda t)^2+\lambda t.
$$
What, therefore, is the variance of a Poisson distribution?}

\notes{*Hint.* There are similarities with the proof of the Poisson mean from the lecture.}

\section{Gaussian samples}

\notes{This question needs a computer. Draw $N$ samples $\{x_n\}_{n=1}^N$ from a Gaussian with mean 0 and variance 1 (`numpy.random.randn` is the old MATLAB `randn`). For each $N$ in the table, compute the sample mean and the sample second moment.}

$N$ | 10 | 50 | 100 | 200 | 500 | 1000
--- | --- | --- | --- | --- | --- | ---
$\frac{1}{N}\sum_n x_n$ |  |  |  |  |  |
$\frac{1}{N}\sum_n x_n^2$ |  |  |  |  |  |

\code{Ns = [10, 50, 100, 200, 500, 1000]
rng = np.random.default_rng(1)
for N in Ns:
    x = rng.normal(size=N)
    print(N, x.mean(), np.mean(x**2))}

\notes{1. What is the true mean of the distribution you have sampled from?}

\notes{2. For each $N$, plot the squared difference between the sample mean and the true mean. What sort of trend do the points give? Is that trend consistent? When, typically, are the sample estimates of the mean worst?}

\notes{3. What is the true second moment of the distribution?}

\notes{4. For each $N$, plot the squared difference between the sample second moment and the true second moment. Is the trend similar to that of the sample mean? Are the second-moment estimates typically better or worse? Why?}

\notes{*Hint.* Repeat the experiment several times and summarise with means and standard deviations. `matplotlib.pyplot.errorbar` replaces MATLAB `errorbar`.}

\section{The exponential distribution}

\notes{Compute the mean and variance of
$$
p(x)=\lambda e^{-\lambda x},\qquad 0<x<\infty.
$$}

\notes{Repeat the sampling experiments of the previous question with an exponential of rate $\lambda=3$, using `npa_plots.exponential_sample` in place of the old `exponentialSamp.m`.}

\code{lam = 3.0
Ns = [10, 50, 100, 200, 500, 1000]
for N in Ns:
    x = npa_plots.exponential_sample(lam, size=N, rng=1)
    print(N, x.mean(), np.mean(x**2))}

\thanks

\references
