% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenNotesProbabilityReview}
\define{npaGenNotesProbabilityReview}

\notes{\section{A Pictorial Definition of Probability}}

\notes{A solid understanding of the fundamentals of probability will be one of the keys to understanding the material in course. We will therefore quickly review what each of these distributions means with a simple pictorial demonstration. In Figure\  \ref{cap:aJointDistribution} we summarise the outcomes of a series of $N$ trials in a two dimensional graph.}

\figure{\includepng{\diagramsDir/npa/probDiagram}{80%}}{Representation of joint and conditional probabilities. In this figure the crosses are the outcomes of the trials. They live in a discrete space of boxes given by the grid. The two events, $X$ and $Y$ are shown across the two axes of the plot.There six possible outcomes for event $X$, $X=1\dots6$, and five possible outcomes for event $Y$, $Y=1\dots5$. The small $n$s in the top left hand corner of each thick lined box denote how many crosses fall inside that box.}{cap:aJointDistribution}

\notes{For Figure\  \ref{cap:aJointDistribution} the outcome of a trial is plotted on a two dimensional graph. We have drawn three further boxes on the graph (solid, dotted and dashed lines), each box is defined by the outcomes it covers. We have denoted the number of events in each box with a small $n$. Probabilities are defined in the limit as we take the number of trials $N$ to infinity.}

\notes{\subsection{Notational Details}}

\notes{Strictly speaking, when we write probability distributions we should write them out in full (*e.g. * for the joint distribution, $P\left(X=x,Y=y\right)$). However, in practice, we often use a shorthand notation: $P\left(x,y\right)$. This is convenient, but it can lead to confusion. It looks very much like we might write a multivariate function, *e.g. *$f\left(x,y\right)=\frac{x}{y}$. For a multivariate function though, $f\left(x,y\right)\neq f\left(y,x\right)$ in general. However, for our probability shorthand $P\left(x,y\right)=P\left(y,x\right)$ because $P\left(X=x,Y=y\right)=P\left(Y=y,X=x\right)$.
We have denoted the probability distribution with a capital $P$. In *these notes* we will use capital $P$s consistently to denote discrete distributions. Later, when we come on to continuous probability density functions, we will turn to small letters.}

\notes{\section{Probability Rules}}

\notes{From the simple definitions we've given above we can derive some straightforward rules associated with manipulating probability distributions.}

\notes{\subsection{Normalisation}}

\notes{The first point to note is that probability distributions are normalised, the sum over the distribution across each of its possible value is 1. This is clear from the fact that $\sum_{x}n_{X=x}=N$, which gives $$
\sum_{x}P\left(x\right)=\lim_{N\rightarrow\infty}\frac{\sum_{x}n_{X=x}}{N}=\lim_{N\rightarrow\infty}\frac{N}{N}=1.$$A similar result can be derived for the marginal and conditional distributions.}

\notes{\subsection{The Sum Rule}}

\notes{The sum rule describes how we can obtain a marginal distribution from the joint distribution. The distribution is called the marginal distribution because one of the variables in the joint distribution is* marginalised*, *i.e. * it is removed from the distribution (you can think of it being written in the margin). The marginal probability $P\left(y\right)$ is given by $\lim_{N\rightarrow\infty}\frac{n_{Y=y}}{N}$ and the joint distribution $P\left(x,y\right)$ is given by $\lim_{N\rightarrow\infty}\frac{n_{X=x,Y=y}}{N}$. Now we note (using Figure\  \ref{cap:aJointDistribution}) that $n_{Y=y}=\sum_{x}n_{X=x,Y=y}$, where the sum is over all possible values of $X$. We therefore find that$$
\lim_{N\rightarrow\infty}\frac{n_{Y=y}}{N}=\lim_{N\rightarrow\infty}\sum_{x}\frac{n_{X=x,Y=y}}{N},$$or in other words$$
P\left(y\right)=\sum_{x}P\left(x,y\right).$$This is known as the sum rule of probability.}

\notes{\subsection{The Product Rule}}

\notes{The product rule describes how we obtain a joint distribution from a conditional distribution and a marginal. Recall that the conditional distribution $P\left(x|y\right)$ is given by $\lim_{N\rightarrow\infty}\frac{n_{X=x,Y=y}}{n_{Y=y}}$. This can be related to the joint distribution over $x$ and $y$ and the marginal distribution over $x$ using the fact that $P\left(x,y\right)$ is given by $$
\lim_{N\rightarrow\infty}\frac{n_{X=x,Y=y}}{N}=\lim_{N\rightarrow\infty}\frac{n_{X=x,Y=y}}{n_{Y=y}}\frac{n_{Y=y}}{N}$$or in other words$$
P\left(x,y\right)=P\left(x|y\right)P\left(y\right).$$This is known as the product rule of probability.}

\notes{\subsection{Bayes' Rule}}

\notes{Less relevant to our work on queueing theory, but worth pointing out since we've come so far is Bayes' Rule or Bayes' Theorem. Since the joint distribution is commutative in its arguments we have, from the product rule,$$
P\left(x,y\right)=P\left(y,x\right)=P\left(y|x\right)P\left(x\right),$$ it naturally follows that we can write$$
P\left(x|y\right)P\left(y\right)=P\left(y|x\right)P\left(x\right)$$which leads to Bayes' Rule, which relates the two conditional probabilities associated with the variables:$$
P\left(x|y\right)=\frac{P\left(y|x\right)P\left(x\right)}{P\left(y\right)}.$$}

\notes{\subsection{Independence}}

\notes{In the course we will often state that two or more variables are assumed to be independent. Probabilistically independence refers to the affect of the knowledge of one variable on the distribution of another. Mathematically this means that our probability distribution over $x$ is not affected by the value of $y$, or in other words$$
P\left(x\right)=P\left(x|y\right),$$the conditional distribution of $x$ given $y$ is equal to the marginal distribution of $x$. This in turn implies that the joint distribution factorises,$$
P\left(x,y\right)=P\left(x|y\right)P\left(y\right)=P\left(x\right)P\left(y\right),$$and furthermore that $$
P\left(y|x\right)=P\left(y\right).$$The factorisation of the joint distribution when variables are independent turns out to be a very important property which makes a lot of analysis tractable.}

\notes{\section{Expectations\label{sec:expectations}}}

\notes{A probabilistic model of a system may summarise our beliefs about the system, but to develop further understandings of the model often want to summarise the model by its expectations.
The expected value of a function, $f\left(x\right)$, under a probability distribution $P\left(x\right)$ is $$
\left\langle f\left(x\right)\right\rangle _{P\left(x\right)}=\sum_{x}P\left(x\right)f\left(x\right).$$Here we have introduced a particular notation for the expectation, you will also see expectations written in the form $E\left\{ f\left(x\right)\right\} $.}

\notes{\subsection{Expectations under a Simple Distribution}}

\notes{Suppose that $X$ can be $0,\,1,$ or $2$ and $f\left(x\right)=x^{2}$. We define a distribution over $x$ in Table\  \ref{cap:simpleXDistribution}.
From the definition of an expectation we gave we can compute $$
\left\langle f\left(x\right)\right\rangle =\left\langle x^{2}\right\rangle =0\times0.2+1\times0.5+4\times0.3=1.7,$$where we have dropped the subscript $P\left(x\right)$, as we consider it clear from the context what the expectation is considered to be over. We can also see that the expectation of $x$ under this distribution is$$
\left\langle x\right\rangle =0\times0.2+1\times0.5+2\times0.3=1.1.$$The expectation of $x$ under a distribution is known as the first moment of the distribution or its *mean*. The mean can be thought of as the `centre of probability mass' of the distribution. The expectation of $x^{2}$ is known as the second moment, it is normally used in combination with the mean to obtain the variance.}

\notes{\subsection{Variance}}

\notes{The variance of the distribution is given by the difference between the second moment and the square of the mean. It is often denoted by $\sigma^{2}$.$$
\sigma^{2}=\left\langle x^{2}\right\rangle -\left\langle x\right\rangle ^{2}.$$It is always positive and it expresses the degree of variation around the mean value. Its square root is known as the standard deviation$$
\sigma=\sqrt{\left\langle x^{2}\right\rangle -\left\langle x\right\rangle ^{2}},$$for our example above the variance is given by$$
1.7-\left(1.1\right)^{2}=0.49,$$the standard deviation is therefore$$
\sqrt{1.7-\left(1.1\right)^{2}}=0.7.$$}

\notes{\section{Distributions as Functions\label{sec:distributionAsFunction}}}

\notes{In the above example we defined a probability distribution with a simple table, making sure that the values summed to 1. A more compact way to represent a distribution is in terms of a function. As an example of this we will consider the Poisson distribution.}

\notes{\subsection{The Poisson Distribution}}

\notes{The Poisson distribution was first published by \textbf{Sim\i \'{e} on Denis Poisson} (1781-1840) in 1837. It is defined over the space of all non-negative integers. Since this set is countably infinite in size it is impossible to write all the numbers down that would define the distribution. The Poisson distribution is therefore defined as\begin{equation}
P\left(k|\mu\right)=\frac{\mu^{k}}{k!}\exp\left(-\mu\right).\label{eq:poissonDist}\end{equation}where $k$ is any integer from $0$ to $\infty$, and $\mu$ is a parameter of the distribution. In these notes we place $\mu$ on the right of the conditioning bar to indicate that it is a parameter. Note that in [@Bertsekas:data92] a slightly different notation is used. To work out the probability of a particular value, $k$, in a Poisson distribution with a particular parameter, $\mu$, we simply substitute the parameter and the value $n$ into (\ref{eq:poissonDist}). For example, with $\mu=2$ we can start filling a table (Table \ref{cap:poissonTable}).
As we mentioned in Section\  \ref{sec:expectations}, the expectations under a distribution are important for summarising the distributions characteristics. Expectations of distributions that take the form of a function can also be computed. Typically we expect the resulting expectation to be a function of the distributions parameters. In the Examples section at the end of this chapter we compute the mean of a Poisson distribution.}

\notes{\section{Continuous Variables}}

\notes{So far we have discussed a value for discrete values of $x$ or $y$. We now turn to a continuous models. First though we introduce the probability distribution's sister, the *probability density function* (PDF). In the discrete case, we defined probability distributions over a discrete number of states. However, if we wish to model a continuous value, such as the height of a computer science student, how do we represent it as a probability distribution? One way would be to `discretise' the continuous value by splitting it into discrete regions. We effectively did this in the example in Figure\  \ref{cap:aJointDistribution}. So, for our height example, we could model the probability that your height was between $1.6\textrm{m}$ and $1.7\textrm{m}$, or alternatively we could ask what is the probability that you are over $1.8\textrm{m}$ given that you are a computer scientist? However, remodelling for each of these questions would be rather tedious. It would be more convenient if we could develop a representation which could answer *any *question we chose to ask about a computer scientist's height. This is what a probability density function represents. It does not represent probabilities directly, but from it they may be derived.}

\figure{\includepng{\diagramsDir/npa/pdfOfHeight}{60%}}{A Gaussian PDF representing heights of computer scientists.}{cap:heightPDF}

\notes{We represent a probability density function with a small $p\left(\cdot\right)$ to differentiate it from a probability distribution which we have denoted with a large $P\left(\cdot\right)$. We define it to be a positive function whose integral over the region of interest is one. One example is the Gaussian, shown above to represent a model of a computer science student's height. We can query the distribution by integrating over regions of it. If we wish to ask the question `What is the probability that a computer science student is over $2\textrm{m}$ tall?' The answer, which we denote $P\left(y>2\right)$ is given by integrating from 2 to $\infty$. Since the total area under the curve is always one, and the function is always positive, the answer will always be less than 1 and greater than 0. This fulfils our definition of probabilities. The answer to the inverse question will be $1-P\left(y>2\right)$. Note that this implies that the probability of a student being exactly $2\textrm{m}$ tall is zero. This may seem odd, but is a consequence of querying the system in the limit as a region tends to zero.
\footnote{In what follows we shall use the word distribution to refer to both discrete probabilities and continuous probability density functions.}}

\notes{\subsection{Manipulating PDFs}}

\notes{The same rules that apply to probability distributions may also be applied to PDFs. We won't derive this here, but take it as given that$$
p\left(y|x\right)=\frac{p\left(x|y\right)p\left(y\right)}{p\left(x\right)}$$where $p\left(x,y\right)=p\left(x|y\right)p\left(y\right)$ and for continuous variables $p\left(x\right)=\int p\left(x,y\right)dy$. Here the integral is over the region for which our PDF for $y$ is defined (*e.g. *all real numbers or all positive real numbers). Additionally we may mix discrete and continuous variables. If, for example $y$ is discrete and $x$ is continuous, then we may write$$
P\left(y|x\right)=\frac{p\left(x|y\right)P\left(y\right)}{p\left(x\right)}.$$Finally expectations under a PDF are also computed using the integral instead of the sum so $$
\left\langle f\left(x\right)\right\rangle _{p\left(x\right)}=\int f\left(x\right)p\left(x\right)dx$$where the integral is over the region for which our PDF for $x$ is defined.}

\notes{\subsection{Cumulative Distribution Functions\label{sub:CDFs}}}

\notes{We've discussed how a PDF doesn't represent probabilities directly, but it is a mechanism by which questions about the random variable can be answered. One very common question is: what is the probability that $x<y$? It can be useful to have a function which stores the answer to this question for all $y$. This function is known as the cumulative distribution function (CDF). The CDF is given by the integral of the PDF across all values of $x$ less than $y$. So if the probability distribution is valid in the range $-\infty<x<\infty$ the CDF is given by$$
P\left(x<y\right)=\int_{-\infty}^{y}p\left(x\right)dx,$$alternatively, if the distribution is defined in the range $0\leq x<\infty$ then the CDF is given by$$
P\left(x<y\right)=\int_{0}^{y}p\left(x\right)dx.$$To complete the distribution we need the probability that $x>y$ (which is the other possibility). This is easy to compute because we know the distribution must be normalised, $P\left(x>y\right)=1-P\left(x<y\right)$.
In Figure\  \ref{cap:heightPDF} we give an example of a cumulative distribution function. We show the CDF associated with the PDF of the computer science students' height.}

\figure{\includepng{\diagramsDir/npa/cdfOfHeight}{60%}}{The cumulative distribution function (CDF) for the heights of computer science students. The thick curve gives the CDF and the thinner curve the associated PDF.}{cdfOfHeight}

\notes{Finally, we note that since the cumulative density function is the integral of the probability density function the PDF can be recovered from the CDF through differentiation.}

\notes{\section{Sample Based Approximations}}

\notes{Recall from Section\  \ref{sec:expectations} that expectation of any given function, $f\left(k\right)$, under a distribution, $P\left(k\right)$, can be written as $$
\left\langle f\left(k\right)\right\rangle _{P\left(k\right)}=\sum_{k}f\left(k\right)P\left(k\right)$$which is also written as $E\left\{ f\left(k\right)\right\} $. Recall our definition of probability from Table\  \ref{cap:aJointDistribution}. $$
P\left(k\right)=\lim_{S\rightarrow\infty}\frac{s_{k}}{S}$$where we have now used $S$ (instead of $N$) as the total number of samples or trials from a system and $s_{k}$ is the number that have state $k$. When we make *sample based approximations *we hope that $S$ is `large enough' such that it is a good approximation to say$$
\left\langle f\left(k\right)\right\rangle _{P\left(k\right)}\approx\sum_{k}f\left(k\right)\frac{s_{k}}{S}.$$This formula may be rewritten as:$$
\sum_{k}f\left(k\right)\frac{s_{k}}{S}=\frac{1}{S}\sum_{k}f\left(k\right)s_{k}.$$Now if $\mathbf{k}$ is a vector of samples from $P\left(k\right)$with elements $k_{i}$ and length $S$ then we can rewrite the above$$
\frac{1}{S}\sum_{k}f\left(k\right)s_{k}=\frac{1}{S}\sum_{i=1}^{S}f\left(k_{i}\right)$$which provides us with a sample based approximation to the true expectation: $$
\left\langle f\left(k\right)\right\rangle _{P\left(k\right)}\approx\frac{1}{S}\sum_{i=1}^{S}f\left(k_{i}\right).$$Some well know special cases of this include the *sample mean, *often denoted by $\bar{k}$, and computed as$$
\bar{k}=\frac{1}{S}\sum_{i=1}^{S}k_{i},$$this sample based mean is an approximation to the true distribution mean$$
\left\langle k\right\rangle \approx\bar{k}.$$The same approximations can be used in the context of continuous PDFs, so we have\begin{eqnarray*}
\left\langle f\left(x\right)\right\rangle _{p\left(x\right)} & = & \int f\left(x\right)p\left(x\right)dx\\
 & \approx & \frac{1}{S}\sum_{i=1}^{S}f\left(x_{i}\right),\end{eqnarray*}where $x_{i}$ are independently obtained samples from the distribution $p\left(x\right)$.
\footnote{How large $S$ need be is dependent on both the function whose expectation we are estimating and the distribution under which we are taking the expectation.}
The approximation gets better for increasing $S$ and worse if the samples from $P\left(k\right)$ are *not *independent.}

\notes{\paragraph{Sample Means for Student Heights}}

\notes{Returning to our example concerning the height of computer science students. If we don't know the true underlying distribution of their heights, $p\left(h\right)$, we cannot compute the mean of the distribution, but we can approximate it with the sample mean: so if we want the mean, $f\left(h\right)=h$, we use$$
\int_{0}^{\infty}hp\left(h\right)dh\approx\frac{1}{S}\sum_{i=1}^{S}f\left(k_{i}\right).$$}

\notes{\paragraph{Sample and Distribution Means}}

\notes{In most texts the word mean is used interchangeably to describe sample based means and the true mean of a distribution. However, you should always bear in mind the important difference between the two. Later in the course we will also come across time based averages and assumptions will be made that the time based average is equal to the average under a `steady state distribution'.}

\notes{\subsection{Mean and Variance\label{sub:poissonMeanVar}}}

\notes{We compute the mean of a Poisson in the following example. The variance is an exercise in the first tutorial sheet.}

\notes{## Examples}

\notes{1. Compute the mean of the Poisson distribution, *i.e. *the expectation of $k$ under the distribution $P\left(k|\mu\right)=\frac{\mu^{k}}{k!}e^{-\mu}$.
  [0]
    The mean is given by $$
\left\langle k\right\rangle _{P\left(k|\mu\right)}=\sum_{k=0}^{\infty}k\frac{\mu^{k}}{k!}e^{-\mu}$$ To make progress with this we first pull out $\mu e^{-\mu}$ and the first $k$ in the factorial, $\frac{k}{k!}=\frac{k}{k(k-1)!}=\frac{1}{(k-1)!}$. We can also remove the first term from the sum because it is multiplied by $k$ which is zero for the first term.
    This leads to$$
\left\langle k\right\rangle =e^{-\mu}\mu\sum_{k=1}^{\infty}\frac{\mu^{(k-1)}}{(k-1)!}$$ Now we make the following substitution: $m=k-1$. 
\left\langle k\right\rangle =e^{-\mu}\mu\sum_{m=0}^{\infty}\frac{\mu^{m}}{m!}\label{eq:poissonMean2} We now make use of the following geometric series,$$
e^{\mu}=\sum_{m=0}^{\infty}\frac{\mu^{m}}{m!}$$ Substituting this result back into (\ref{eq:poissonMean2}) we find 
\left\langle k\right\rangle =\mu\label{eq:poissonMean3}
  
  *The variance of a Poisson is an exercise in Tutorial Sheet 1.*}

\notes{#### Answer}

\endif
