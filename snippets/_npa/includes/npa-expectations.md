\ifndef{npaExpectations}
\define{npaExpectations}

\section{Expectations}

\notes{A probabilistic model summarises our beliefs about a system. To say more we often summarise the model by its expectations.}

\notes{The expected value of a function $f(x)$ under a distribution $P(x)$ is
$$
\left\langle f(x)\right\rangle_{P(x)}=\sum_{x}P(x)\,f(x).
$$
You will also see $E\{f(x)\}$ for the same quantity.}

\slides{* Expectation: $\langle f(x)\rangle_{P(x)}=\sum_x P(x)f(x)$
* Also written $E\{f(x)\}$
* Mean = first moment; variance from first and second moments}

\subsection{A Small Discrete Example}

\notes{Suppose $X$ takes values $0,1,2$ and $f(x)=x^2$.}

$x$ | 0 | 1 | 2
--- | --- | --- | ---
$P(x)$ | 0.2 | 0.5 | 0.3
$f(x)=x^2$ | 0 | 1 | 4

\notes{Then
$$
\langle x^2\rangle = 0\times 0.2 + 1\times 0.5 + 4\times 0.3 = 1.7,
$$
and
$$
\langle x\rangle = 0\times 0.2 + 1\times 0.5 + 2\times 0.3 = 1.1.
$$
The expectation of $x$ is the first moment, or *mean*: the centre of probability mass. The expectation of $x^2$ is the second moment.}

\subsection{Variance}

\notes{Variance is the second moment minus the square of the mean,
$$
\sigma^2 = \langle x^2\rangle - \langle x\rangle^2.
$$
It is always non-negative. Its square root is the standard deviation. For the table above,
$$
\sigma^2 = 1.7 - (1.1)^2 = 0.49, \qquad \sigma = 0.7.
$$}

\endif
