\ifndef{npaGenSlidesProbabilityReview}
\define{npaGenSlidesProbabilityReview}

\newslide{Probability Review}

\slides{* Health warning: Mathematics and Probability are FUNDAMENTAL to this course.
* We are interested in trials which result in two random variables, $X$ and $Y$, each of which has an `outcome' denoted by $x$ or $y$.
* We summarise the notation and terminology for these distributions in the following table.}

\newslide{A Pictorial Definition of Probability}

\slides{\figure{\includepng{\diagramsDir/npa/probDiagram}{80%}}{Representation of joint and conditional probabilities.}{cap:aJointDistribution}}

\newslide{A Pictorial Definition of Probability (continued)}

\slides{* Here is a review of what probabilities are in a two dimensional graph.}

\newslide{Different Distributions}

\newslide{Notational Details}

\slides{* Typically we should write out $P\left(X=x,Y=y\right)$.
* In practice, we often use $P\left(x,y\right)$.
* This looks very much like we might write a multivariate function, *e.g.*$f\left(x,y\right)=\ensuremath{\frac{x}{y}}$.
* For a multivariate function though, $f\left(x,y\right)\ensuremath{\neq} f\left(y,x\right)$.}

\newslide{Notational Details (continued)}

\slides{* However $P\left(x,y\right)=P\left(y,x\right)$ because $P\left(X=x,Y=y\right)=P\left(Y=y,X=x\right)$.
* We have denoted the probability distribution with a capital $P$.
* We will use capital $P$s consistently to denote discrete distributions.
* For continuous probability density functions, we will turn to small letters.
* We now consider some `rules of probability'.}

\newslide{Normalisation}

\slides{* All distributions are normalised. This is clear from the fact that $\sum_{x}n_{X=x}=N$, which gives $$
\sum_{x}P\left(x\right)=\lim_{N\ensuremath{\rightarrow\infty}}\ensuremath{\frac{\sum_{x}n_{X=x}}{N}}=\lim_{N\ensuremath{\rightarrow\infty}}\ensuremath{\frac{N}{N}}=1.$$A similar result can be derived for the marginal and conditional distributions.}

\newslide{The Sum Rule}

\slides{* The marginal probability $P\left(y\right)$ is given by $\lim_{N\ensuremath{\rightarrow\infty}}\ensuremath{\frac{n_{Y=y}}{N}}$.
* The joint distribution $P\left(x,y\right)$ is given by $\lim_{N\ensuremath{\rightarrow\infty}}\ensuremath{\frac{n_{X=x,Y=y}}{N}}$.
* $n_{Y=y}=\sum_{x}n_{X=x,Y=y}$ so$$
\lim_{N\ensuremath{\rightarrow\infty}}\ensuremath{\frac{n_{Y=y}}{N}}=\lim_{N\ensuremath{\rightarrow\infty}}\sum_{x}\ensuremath{\frac{n_{X=x,Y=y}}{N}},$$in other words$$
P\left(y\right)=\sum_{x}P\left(x,y\right).$$This is known as the sum rule of probability.}

\newslide{The Product Rule}

\slides{* $P\left(x|y\right)$ is given by $\lim_{N\ensuremath{\rightarrow\infty}}\ensuremath{\frac{n_{X=x,Y=y}}{n_{Y=y}}}$.
* $P\left(x,y\right)$ is given by $$
\lim_{N\ensuremath{\rightarrow\infty}}\ensuremath{\frac{n_{X=x,Y=y}}{N}}=\lim_{N\ensuremath{\rightarrow\infty}}\ensuremath{\frac{n_{X=x,Y=y}}{n_{Y=y}}\frac{n_{Y=y}}{N}}$$or in other words$$
P\left(x,y\right)=P\left(x|y\right)P\left(y\right).$$This is known as the product rule of probability.}

\newslide{Bayes' Rule}

\slides{* From the product rule,$$
P\left(x,y\right)=P\left(y,x\right)=P\left(y|x\right)P\left(x\right),$$
  so$$
P\left(x|y\right)P\left(y\right)=P\left(y|x\right)P\left(x\right)$$which leads to Bayes' Rule, $$
P\left(x|y\right)=\ensuremath{\frac{P\left(y|x\right)P\left(x\right)}{P\left(y\right)}}.$$}

\newslide{Independence}

\slides{* The variable $x$ is independent of $y$ if the distribution over $x$ is not affected by the value of $y$:$$
P\left(x\right)=P\left(x|y\right),$$the conditional distribution of $x$ given $y$ is equal to the marginal distribution of $x$. This in turn implies that the joint distribution factorises,$$
P\left(x,y\right)=P\left(x|y\right)P\left(y\right)=P\left(x\right)P\left(y\right),$$and furthermore that $$
P\left(y|x\right)=P\left(y\right).$$The factorisation of the joint distribution when variables are independent turns out to be a very important property which makes a lot of analysis tractable.}

\newslide{Expectations\label{sec:expectations}}

\slides{* A probabilistic model summarises our beliefs.
* Sometimes need to summarise the model by its expectations.
* Expected value of $f\left(x\right)$ under $P\left(x\right)$ is $$
\left\langle f\left(x\right)\right\rangle _{P\left(x\right)}=\sum_{x}P\left(x\right)f\left(x\right).$$Here we have introduced a particular notation for the expectation, you will also see expectations written in the form $E\left\lbrace f\left(x\right)\right\rbrace$.}

\newslide{Expectations under a Simple Distribution}

\slides{* Define a distribution over $x$ in Table\  \ref{cap:simpleXDistribution}.
  % empty table
* We can compute $$
\left\langle f\left(x\right)\right\rangle =\left\langle x^{2}\right\rangle =0\times0.2+1\times0.5+4\times0.3=1.7,$$have dropped the subscript $P\left(x\right)$}

\newslide{Expectations under a Simple Distribution (continued)}

\slides{* We can also see that the expectation of $x$ is$$
\left\langle x\right\rangle =0\times0.2+1\times0.5+2\times0.3=1.1.$$
* The expectation of $x$ is known as the first moment of the distribution or its *mean*.}

\newslide{Variance of a Distribution}

\slides{* The expectation of $x^{2}$ is known as the second moment --- normally used to obtain the variance.
* Variance: given by the difference between the second moment and the square of the mean. It is often denoted by $\ensuremath{\sigma^{2}}$.$$
\ensuremath{\sigma^{2}}=\left\langle x^{2}\right\rangle -\left\langle x\right\rangle ^{2}.$$For our example above the variance is given by$$
1.7-\left(1.1\right)^{2}=0.49,$$
* Its square root is known as the standard deviation$$
\ensuremath{\sigma}=\sqrt{\left\langle x^{2}\right\rangle -\left\langle x\right\rangle ^{2}},$$$$
\sqrt{1.7-\left(1.1\right)^{2}}=0.7.$$}

\newslide{Distributions as Functions}

\slides{* Probability distribution with a simple table can be limiting.
* The Poisson Distribution --- a distribution a a function
* First published by \textbf{Sim\i \'{e} on Denis Poisson} (1781-1840) in 1837.}

\newslide{Distributions as Functions (continued)}

\slides{* Defined over the space of all non-negative integers.
* This set is countably infinite: impossible to summarise in a table!
* The Poisson distribution is therefore defined as
P\left(k|\ensuremath{\mu\right)}=\ensuremath{\frac{\mu^{k}}{k!}\exp\left(}-\ensuremath{\mu\right)}.\label{eq:poissonDist}where $k$ is any integer from $0$ to $\ensuremath{\infty}$, and $\ensuremath{\mu}$ is a parameter of the distribution.}

\newslide{A Poisson with $\mu=2$}

\slides{* To work out the probability of $k$ in a Poisson $\ensuremath{\mu}=2$ we can start filling a table.
* The values in a table are computed from (\ref{eq:poissonDist})
  % empty table}

\newslide{Mean and Variance}

\slides{* Example 1, Chapter 3: Mean and Variance of Poisson Distribution
  As we mentioned in Section\  \ref{sec:expectations}, the expectations under a distribution are important for summarising the distributions characteristics. Expectations of distributions that take the form of a function can also be computed. Typically we expect the resulting expectation to be a function of the distributions parameters.
* Mean of the Poisson process
    $$
\left\langle k\right\rangle _{P\left(k|\ensuremath{\mu\right)}}=\sum_{k=0}^{\ensuremath{\infty}}k\ensuremath{\frac{\mu^{k}}{k!}}e^{-\ensuremath{\mu}}$$ To make progress with this we first pull out $\ensuremath{\mu} e^{-\ensuremath{\mu}}$ and the first $k$ in the factorial, $\ensuremath{\frac{k}{k!}}=\ensuremath{\frac{k}{k(k-1)!}}=\ensuremath{\frac{1}{(k-1)!}}$. We can also remove the first term from the sum because it is multiplied by $k$ which is zero for the first term.
    This leads to$$
\left\langle k\right\rangle =e^{-\ensuremath{\mu}}\ensuremath{\mu\sum_{k=1}^{\infty}\frac{\mu^{(k-1)}}{(k-1)!}}$$ Now we make the following substitution: $m=k-1$. 
\left\langle k\right\rangle =e^{-\ensuremath{\mu}}\ensuremath{\mu\sum_{m=0}^{\infty}\frac{\mu^{m}}{m!}\label{eq:poissonMean2}} Finally we note that the geometric series $\sum_{m=0}^{\ensuremath{\infty}}\ensuremath{\frac{\mu^{m}}{m!}}=e^{\ensuremath{\mu}}$. Substituting this result back into (\ref{eq:poissonMean2}) we find 
\left\langle k\right\rangle =\ensuremath{\mu\label{eq:poissonMean3}}
* The variance of a Poisson is also $\ensuremath{\mu}$ --- see Tutorial 1.}

\newslide{Continuous Variables}

\slides{* So far discrete values of $x$ or $y$.
* For continuous models we introduce the *probability density function* (PDF).
* Discrete case: defined probability distributions over a discrete number of states.}

\newslide{Continuous Variables (continued)}

\slides{* How do we represent continuous as probability?
* Computer science student's height:
* Develop a representation which could answer *any*question we chose to ask about a computer scientist's height.}

\newslide{Gaussian PDF}

\slides{\figure{\includepng{\diagramsDir/npa/pdfOfHeight}{80%}}{A Gaussian PDF representing heights of computer scientists.}{cap:heightPDF}}

\newslide{Gaussian PDF (continued)}

\slides{* One example is the Gaussian: we can query the distribution by integrating over regions of it.
* Represent a PDF with a small $p\left(\ensuremath{\cdot\right)}$ to differentiate it from a probability distribution: $P\left(\ensuremath{\cdot\right)}$.
* It is a positive function, integral over the region of interest is one.
  \footnote{In what follows we shall use the word distribution to refer to both discrete probabilities and continuous probability density functions.}}

\newslide{Manipulating PDFs}

\slides{* Same rules for PDFs as distributions *e.g.*$$
p\left(y|x\right)=\ensuremath{\frac{p\left(x|y\right)p\left(y\right)}{p\left(x\right)}}$$where $p\left(x,y\right)=p\left(x|y\right)p\left(y\right)$ and for continuous variables $p\left(x\right)=\ensuremath{\int} p\left(x,y\right)dy$.
* Expectations under a PDF$$
\left\langle f\left(x\right)\right\rangle _{p\left(x\right)}=\ensuremath{\int} f\left(x\right)p\left(x\right)dx$$where the integral is over the region for which our PDF for $x$ is defined.}

\newslide{Cumulative Distribution Functions\label{sub:CDFs}}

\slides{* PDF doesn't represent probabilities directly
* One very common question is: what is the probability that $x<y$?
* The cumulative distribution function (CDF) represents the answer for $-\ensuremath{\infty}<x<\ensuremath{\infty}$ the CDF is given by$$
P\left(x>y\right)=\int_{-\ensuremath{\infty}}^{y}p\left(x\right)dx,$$for $0\ensuremath{\leq} x<\ensuremath{\infty}$ then the CDF is given by$$
P\left(x>y\right)=\int_{0}^{y}p\left(x\right)dx.$$}

\newslide{Gaussian PDF and CDF}

\slides{\figure{\includepng{\diagramsDir/npa/cdfOfHeight}{80%}}{The cumulative distribution function (CDF) for the heights of computer science students. The thick curve gives the CDF and the thinner curve the associated PDF.}{cdfOfHeight}}

\newslide{Gaussian PDF and CDF (continued)}

\slides{* In Figure\  \ref{cap:heightPDF} example of the CDF for the students' heights example.
* The PDF can be recovered from the CDF through differentiation.}

\newslide{Sample Based Approximations}

\slides{* Recall that expectation of any given function, $f\left(k\right)$, under a distribution, $P\left(k\right)$, can be written as $$
\left\langle f\left(k\right)\right\rangle _{P\left(k\right)}=\sum_{k}f\left(k\right)P\left(k\right)$$Recall our definition of probability from Table\  \ref{cap:aJointDistribution}. $$
P\left(k\right)=\lim_{S\ensuremath{\rightarrow\infty}}\ensuremath{\frac{s_{k}}{S}}$$where we have now used $S$ (instead of $N$)
* *Sample based approximations*hope that $S$ is `large enough' such that it to say$$
\left\langle f\left(k\right)\right\rangle _{P\left(k\right)}\ensuremath{\approx\sum_{k}}f\left(k\right)\ensuremath{\frac{s_{k}}{S}}.$$}

\newslide{Sample Based Approximations contd}

\slides{* This formula may be rewritten as:$$
\sum_{k}f\left(k\right)\ensuremath{\frac{s_{k}}{S}}=\ensuremath{\frac{1}{S}\sum_{k}}f\left(k\right)s_{k}.$$For $\mathbf{k}$ a vector of samples from $P\left(k\right)$with elements $k_{i}$ and length $S$ $$
\ensuremath{\frac{1}{S}\sum_{k}}f\left(k\right)s_{k}=\ensuremath{\frac{1}{S}\sum_{i=1}^{S}}f\left(k_{i}\right)$$
* This provides us with a sample based approximation $$
\left\langle f\left(k\right)\right\rangle _{P\left(k\right)}\ensuremath{\approx\frac{1}{S}\sum_{i=1}^{S}}f\left(k_{i}\right).$$
* Special cases of this include the *sample mean,*often denoted by $\ensuremath{\bar{k}}$, and computed as$$
\ensuremath{\bar{k}}=\ensuremath{\frac{1}{S}\sum_{i=1}^{S}}k_{i},$$}

\newslide{Sample Mean vs True Mean}

\slides{* This is an approximation to the true distribution mean$$
\left\langle k\right\rangle \ensuremath{\approx\bar{k}}.$$
* The same approximations can used for continuous PDFs, so we have
* Approximation gets better for increasing $S$ and worse if the samples from $P\left(k\right)$ are *not*independent.

| \left\langle f\left(x\right)\right\rangle _{p\left(x\right)} | = | \ensuremath{\int} f\left(x\right)p\left(x\right)dx |
| --- | --- | --- |
|  | \ensuremath{\approx} | \ensuremath{\frac{1}{S}\sum_{i=1}^{S}}f\left(x_{i}\right),where $x_{i}$ are independently obtained samples from the distribution $p\left(x\right)$. |}

\newslide{Note on Sample and Distribution Means}

\slides{* In most texts the word mean is used interchangeably to describe sample based means and the true mean of a distribution. However, you should always bear in mind the important difference between the two. Later in the course we will also come across time based averages and assumptions will be made that the time based average is equal to the average under a `steady state distribution'.}

\endif
