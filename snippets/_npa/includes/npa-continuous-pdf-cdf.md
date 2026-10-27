\ifndef{npaContinuousPdfCdf}
\define{npaContinuousPdfCdf}

\section{Continuous Variables}

\notes{So far $x$ and $y$ have been discrete. For a continuous quantity — the height of a computer-science student — we could discretise into bins, as the pictorial definition already did. That is awkward if we want to answer *any* question about height. A *probability density function* (PDF) does not give probabilities directly; we derive them from it by integration.}

\slides{* Discrete: capital $P$
* Continuous: density $p(\cdot)$, probabilities by integration
* $P(\text{exactly } 2\,\mathrm{m})=0$ is a consequence of querying a set of width zero}

\figure{\includepng{\diagramsDir/npa/pdfOfHeight}{60%}}{A Gaussian PDF representing heights of computer scientists.}{height-pdf}

\notes{We write a density with a small $p(\cdot)$ and a discrete distribution with a capital $P(\cdot)$. A density is a positive function whose integral over the region of interest is one. The Gaussian above is a model of height. The probability that a student is taller than $2\,\mathrm{m}$ is the integral from 2 to $\infty$. Because the total area is one and the function is positive, that probability lies in $(0,1)$. The probability of being *exactly* $2\,\mathrm{m}$ is zero: that is the limit of a region whose width tends to zero.}

\subsection{Manipulating Densities}

\notes{The same rules apply. We take as given
$$
p(y\mid x)=\frac{p(x\mid y)\,p(y)}{p(x)},
$$
with $p(x,y)=p(x\mid y)p(y)$ and $p(x)=\int p(x,y)\,dy$. Discrete and continuous variables may be mixed. Expectations under a density use an integral,
$$
\langle f(x)\rangle_{p(x)}=\int f(x)\,p(x)\,dx.
$$}

\subsection{Cumulative Distribution Functions}

\notes{A common question is $P(x<y)$. The function that stores the answer for every $y$ is the cumulative distribution function (CDF),
$$
P(x<y)=\int_{-\infty}^{y} p(x)\,dx
$$
when the density is supported on the whole line, or from $0$ when the support is the positive reals. Then $P(x>y)=1-P(x<y)$. The PDF is the derivative of the CDF.}

\figure{\includepng{\diagramsDir/npa/cdfOfHeight}{60%}}{CDF (thick) and PDF (thin) for the heights of computer science students.}{height-cdf}

\endif
