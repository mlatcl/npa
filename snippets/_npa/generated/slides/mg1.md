\ifndef{npaGenSlidesMg1}
\define{npaGenSlidesMg1}

\newslide{$M$/$G$/$1$ Queue}

\slides{* Service times are *generally*distributed: cannot use the birth death process to analyse the system.
* We introduce a different type of analysis based on the mean residual service time.}

\newslide{$M$/$G$/$1$ Queue (continued)}

\slides{* We will derive the Pollaczek-Khinchin formula.
* This gives the expected queueing time for any distribution of service times with *finite variance*.}

\newslide{Pollaczek-Khinchin formula}

\slides{* The Pollaczek-Khinchin formula is given as}

\newslide{Pollaczek-Khinchin formula (continued)}

\slides{* $\ensuremath{\bar{W}}$ is expected waiting time,
* $\left\langle X^{2}\right\rangle =\left\langle X^{2}\right\rangle _{p(X)}$ is the second moment under the service time distribution,
* utilisation factor is given as $\ensuremath{\rho}=\ensuremath{\lambda\bar{X}}$ and
* $\ensuremath{\bar{X}}=\left\langle X\right\rangle _{p(X)}$ is the mean under the service time distribution.}

\newslide{Proof of Pollaczek-Khinchin Formula}

\slides{* Proof of the Pollaczek-Khinchin formula.
* In our proof we will make three assumptions
* The queue is FIFO queue, *i.e.*customers are served in the order they arrive. This assumption may be relaxed but it will simplify our proof.}

\newslide{Proof of Pollaczek-Khinchin Formula (continued)}

\slides{* The arrival times are statistically independent of the service times.
* The service time distribution has a variance which is finite.
* To formulate the proof we introduce a concept known as the mean residual service time.}

\newslide{The Residual Service Time\label{sub:theResidualServiceTime}}

\slides{* The residual service time is
    ... the amount of service time that remains for the customer under service from the perspective of a customer who has just arrived in the queue.
* The first part of the proof occurs from the perspective of the arriving customer.
* The arriving customer is considered to be the $i$th customer.}

\newslide{Simple Definitions and Schematic}

\slides{\figure{\includepng{\diagramsDir/npa/residualServiceOverview}{100%}}{Schematic representation of residual service time.}{cap:schemeaticRST}}

\newslide{Simple Definitions and Schematic (continued)}

\slides{* Example 1 in the Notes
* We introduce some simple definitions of terms.
* This enables us to draw a simple schematic of the system as it is perceived by the $i$th arrival. This is shown in Figure\  \ref{cap:schemeaticRST}.}

\slides{| $W_{i}$ | = | Waiting time in queue of $i$th customer. |
| --- | --- | --- |
| $R_{i}$ | = | `Residual service time' seen by the $i$th customer. |
| $X_{i}$ | = | Service time of the $i$th customer. |
| $k_{i}$ | = | Number of customers in the system when the $i$th customer arrives. |}

\newslide{Wait for *i*th Customer}

\slides{\figure{\includepng{\diagramsDir/npa/residualServiceOverview}{100%}}{Schematic representation of residual service time.}{cap:schemeaticRST}}

\newslide{Wait for *i*th Customer (continued)}

\slides{* From the figure the wait for the $i$th customer will be given by$$
W_{i}=R_{i}+\sum_{j=i-(k_{i}-1)}^{i-1}X_{j}$$
* Summing over both sides (*i.e.*for all the arriving customers up to the $I$th) $$
\sum_{i=1}^{I}W_{i}=\sum_{i=1}^{I}R_{i}+\sum_{i=1}^{I}\sum_{j=i-(k_{i}-1)}^{i-1}X_{j}$$
* Dividing through by $I$ gives us $$
\sum_{i=1}^{I}\ensuremath{\frac{W_{i}}{I}}=\sum_{i=1}^{I}\ensuremath{\frac{R_{i}}{I}}+\sum_{i=1}^{I}\sum_{j=i-(k_{i}-1)}^{i-1}\ensuremath{\frac{X_{j}}{I}}$$
* In the limit as $I\ensuremath{\rightarrow\infty}$ this becomes $$
\lim_{I\ensuremath{\rightarrow\infty}}\sum_{i=1}^{I}\ensuremath{\frac{W_{i}}{I}}=\lim_{I\ensuremath{\rightarrow\infty}}\sum_{i=1}^{I}\ensuremath{\frac{R_{i}}{I}}+\lim_{I\ensuremath{\rightarrow\infty}}\sum_{i=1}^{I}\ensuremath{\frac{(k_{i}-1)X_{i}}{I}}$$
* The terms of which are recognised as *time averages*.}

\newslide{Time Average Equivalence}

\slides{* If we assume *time averages* are equivalent to *steady state averages* this gives $$
\left\langle W\right\rangle =\left\langle R\right\rangle +\left\langle \left(k-1\right)X\right\rangle .$$
* The length of the queue as seen by the $i$th arrival is independent of the $i$th arrival's length (our second assumption)}

\newslide{Time Average Equivalence (continued)}

\slides{* this means $\left\langle (k-1)X\right\rangle =\left\langle k-1\right\rangle \left\langle X\right\rangle$ and since $(k-1)$ is the length of the queue we may write $$
\ensuremath{\bar{W}}=\ensuremath{\bar{R}}+\ensuremath{\bar{N}_{Q}\bar{X}}$$
* Using Little's theorem for the queue we have$$
\ensuremath{\bar{N}_{Q}}=\ensuremath{\lambda\bar{W}}$$
* Substituting back in we have$$
\ensuremath{\bar{W}}=\ensuremath{\bar{R}}+\ensuremath{\lambda\bar{X}\bar{W}}.$$}

\newslide{Wait in Terms of Residual Service Time}

\slides{* From the previous slide:$$
\ensuremath{\bar{W}}=\ensuremath{\bar{R}}+\ensuremath{\lambda\bar{X}\bar{W}}.$$
* And the fact that $\ensuremath{\rho}=\ensuremath{\lambda\bar{X}}$ (which stems from Little's formula for the service) gives us $$
\ensuremath{\bar{W}}=\ensuremath{\bar{R}}+\ensuremath{\rho\bar{W}}$$}

\newslide{Wait in Terms of Residual Service Time (continued)}

\slides{* Leading to 
\ensuremath{\bar{W}}=\ensuremath{\frac{\bar{R}}{1-\rho}\label{eqn:arrivals}}
* We now have the average queueing time in terms of the mean residual service time. To complete the Pollaczek-Khinchin formula we simply need to calculate $\ensuremath{\bar{R}}$.}

\newslide{Mean Residual Service Time from Departures Perspective}

\slides{\figure{\includepng{\diagramsDir/npa/residualTime}{100%}}{Graphical computation of mean residual time. $M\left(t\right)$ is the number of service completions in the interval $[0,\, t]$.}{cap:meanResidualGraphical}}

\newslide{Mean Residual Service Time from Departures Perspective (continued)}

\slides{* We again turn to a graphical proof to obtain the value of the mean residual service time.}

\newslide{Residual Service Time}

\slides{* The time average of the mean residual service time can then be calculated in terms of the area under the curve, $A(t)$.
* This is given by the area under each of the triangles, $$
A(t)=1\sum_{i=1}^{M(t)}X_{i}^{2}.$$}

\slides{\figure{\includepng{\diagramsDir/npa/residualTime}{100%}}{residualTime}{residualTime}}

\newslide{Residual Service Time}

\slides{* The average service time is the area divided by time, $t$, $$
A(t)=1\sum_{i=1}^{M(t)}X_{i}^{2}.$$ 
* we have introduced the number of arrivals after time $t$, as $M\left(t\right)$.
* As $t\ensuremath{\rightarrow\infty}$, *if the variance is finite*, we find that $M(t)\ensuremath{\rightarrow\infty}$ and we obtain$$
\ensuremath{\bar{R}}=1\ensuremath{\lambda\left\langle} X^{2}\right\rangle .$$

| \ensuremath{\frac{A(t)}{t}} | = | \ensuremath{\frac{M(t)}{t}\frac{A(t)}{M(t)}} |
| --- | --- | --- |
|  | = | 1\ensuremath{\frac{M(t)}{t}\frac{\sum_{i=1}^{M(t)}X_{i}^{2}}{M(t)}}. |}

\newslide{Pollaczek-Khinchin Formula}

\slides{* Again assuming that time averages and ensemble averages are equal we substitute back into (\ref{eqn:arrivals}) to obtain the Pollaczek-Khinchin formula $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}}.$$
* This implies that the total waiting time in the system is $$
\ensuremath{\bar{T}}=\ensuremath{\bar{X}}+\ensuremath{\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}}$$ and through Little's formula we can obtain the expected queue length, $\ensuremath{\bar{N}_{Q}}$, and the expected number in the system, $\ensuremath{\bar{N}}$.}

\newslide{Sanity Check --- Markov Service times}

\slides{* The exponentially distributed service times, $$
P\left(X\right)=\ensuremath{\mu\exp\left(}-\ensuremath{\mu} X\right),$$have a mean of $$
\ensuremath{\bar{X}}=\ensuremath{\frac{1}{\mu}}$$ and a variance of $\ensuremath{\frac{1}{\mu^{2}}}$ leading to a second moment$$
\left\langle X^{2}\right\rangle =\ensuremath{\frac{2}{\mu^{2}}}$$
* Substituting into the Pollaczek-Khinchin formula we obtain 

| \ensuremath{\bar{W}} | = | \ensuremath{\frac{\rho}{\mu\left(1-\rho\right)}} |
| --- | --- | --- |
|  | = | \ensuremath{\frac{\rho}{\mu-\lambda}}which is identical to those we derived for the $M/M/1$ queue. |}

\newslide{Deterministic Service --- $M/D/1$}

\slides{* Some systems have deterministic service times. For example, transmission of fixed length packets over a channel with a fixed bandwidth.
* We represent a `deterministic distribution' as$$
P\left(X\right)=\delta\left(X-\ensuremath{\frac{1}{\mu}\right)}$$where $\delta\left(\ensuremath{\cdot\right)}$is the Dirac delta function.
* For this system $$
\left\langle X\right\rangle =\ensuremath{\frac{1}{\mu}}$$and $$
\left\langle X^{2}\right\rangle =\ensuremath{\frac{1}{\mu^{2}}}$$*i.e.* the variance is zero.}

\newslide{P-K Formula for Deterministic Systems}

\slides{* For this system $$
\left\langle X\right\rangle =\ensuremath{\frac{1}{\mu}}$$and $$
\left\langle X^{2}\right\rangle =\ensuremath{\frac{1}{\mu^{2}}}$$*i.e.* the variance is zero.
* Substituting into the Pollaczek-Khinchin formula we obtain $$
\ensuremath{\bar{W}}=\ensuremath{\frac{\rho}{2\mu\left(1-\rho\right)}}.$$}

\newslide{Table of Delays and Average Numbers in System}

\slides{* In fact we may derive the full range of results for these distributions.}

\newslide{Table of Delays and Average Numbers in System (continued)}

\slides{| Expected value | General | Exponential | Deterministic |
| --- | --- | --- | --- |
| $\ensuremath{\bar{W}}$ | $\ensuremath{\frac{\lambda}{2(1-\rho)}\left\langle} X^{2}\right\rangle$ | $\ensuremath{\frac{\rho}{\mu(1-\rho)}}$ | $\ensuremath{\frac{\rho}{2\mu(1-\rho)}}$ |
| $\ensuremath{\bar{T}}=\ensuremath{\bar{W}}+\ensuremath{\frac{1}{\mu}}$ | $\ensuremath{\frac{\lambda}{2(1-\rho)}\left\langle} X^{2}\right\rangle +\ensuremath{\frac{1}{\mu}}$ | $\ensuremath{\frac{1}{\mu(1-\rho)}}$ | $\ensuremath{\frac{2-\rho}{2\mu(1-\rho)}}$ |
| $\ensuremath{\bar{N_{Q}}}=\ensuremath{\lambda\bar{W}}$ | $\ensuremath{\frac{\lambda^{2}}{2(1-\rho)}\left\langle} X^{2}\right\rangle$ | $\ensuremath{\frac{\rho^{2}}{(1-\rho)}}$ | $\ensuremath{\frac{\rho^{2}}{2(1-\rho)}}$ |
| $\ensuremath{\bar{N}}=\ensuremath{\lambda\bar{W}}+\ensuremath{\rho}=$ | $\ensuremath{\frac{\lambda^{2}}{2(1-\rho)}\left\langle} X^{2}\right\rangle +\ensuremath{\rho}$ | $\ensuremath{\frac{\rho}{1-\rho}}$ | $\ensuremath{\frac{\rho(2-\rho)}{2(1-\rho)}}$ |}

\newslide{Example --- Uniform Service Times}

\slides{* Uniform Service Times --- $M/U/1$.
* Consider a uniform probability distribution is defined between 0 and $b$ for $X>0$ as$$
U\left(X|b\right)=\begin{array}{cc}
\ensuremath{\frac{1}{b}} & 0<X\ensuremath{\leq} b\\
0 & X>b\end{array}$$show that the man of this uniform distribution is given by $b$ and its variance by $b^{2}$ and find the expected waiting time for an $M/U/1$ queue?}

\newslide{Answer}

\slides{* For the mean we have
\\\\\\\\

| \left\langle X\right\rangle | = | \int_{0}^{\ensuremath{\infty}}Xp\left(X\right)dX |
| --- | --- | --- |}

\newslide{Answer}

\slides{* For the mean we have
\\\\\\

| \left\langle X\right\rangle | = | \int_{0}^{\ensuremath{\infty}}Xp\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{\ensuremath{\infty}}XU\left(X|b\right)dX |}

\newslide{Answer}

\slides{* For the mean we have
\\\\

| \left\langle X\right\rangle | = | \int_{0}^{\ensuremath{\infty}}Xp\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{\ensuremath{\infty}}XU\left(X|b\right)dX |
|  | = | \int_{0}^{b}\ensuremath{\frac{X}{b}}dX |}

\newslide{Answer}

\slides{* For the mean we have
\\

| \left\langle X\right\rangle | = | \int_{0}^{\ensuremath{\infty}}Xp\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{\ensuremath{\infty}}XU\left(X|b\right)dX |
|  | = | \int_{0}^{b}\ensuremath{\frac{X}{b}}dX |
|  | = | \left[\ensuremath{\frac{X^{2}}{2b}\right]_{0}^{b}} |}

\newslide{Answer}

\slides{* For the mean we have

| \left\langle X\right\rangle | = | \int_{0}^{\ensuremath{\infty}}Xp\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{\ensuremath{\infty}}XU\left(X|b\right)dX |
|  | = | \int_{0}^{b}\ensuremath{\frac{X}{b}}dX |
|  | = | \left[\ensuremath{\frac{X^{2}}{2b}\right]_{0}^{b}} |
|  | = | \ensuremath{\frac{b^{2}}{2b}}-0 |}

\newslide{Answer}

\slides{* For the mean we have

| \left\langle X\right\rangle | = | \int_{0}^{\ensuremath{\infty}}Xp\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{\ensuremath{\infty}}XU\left(X|b\right)dX |
|  | = | \int_{0}^{b}\ensuremath{\frac{X}{b}}dX |
|  | = | \left[\ensuremath{\frac{X^{2}}{2b}\right]_{0}^{b}} |
|  | = | \ensuremath{\frac{b^{2}}{2b}}-0 |
|  | = | b |}

\newslide{Answer}

\slides{* For the mean we have

| \left\langle X\right\rangle | = | \int_{0}^{\ensuremath{\infty}}Xp\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{\ensuremath{\infty}}XU\left(X|b\right)dX |
|  | = | \int_{0}^{b}\ensuremath{\frac{X}{b}}dX |
|  | = | \left[\ensuremath{\frac{X^{2}}{2b}\right]_{0}^{b}} |
|  | = | \ensuremath{\frac{b^{2}}{2b}}-0 |
|  | = | b |}

\newslide{Variance}

\slides{* For the variance we also require 
\\\\\\

| \left\langle X^{2}\right\rangle | = | \int_{0}^{\ensuremath{\infty}}X^{2}p\left(X\right)dX |
| --- | --- | --- |}

\newslide{Variance}

\slides{* For the variance we also require 
\\\\

| \left\langle X^{2}\right\rangle | = | \int_{0}^{\ensuremath{\infty}}X^{2}p\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{b}\ensuremath{\frac{X^{2}}{b}}dX |}

\newslide{Variance}

\slides{* For the variance we also require 
\\

| \left\langle X^{2}\right\rangle | = | \int_{0}^{\ensuremath{\infty}}X^{2}p\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{b}\ensuremath{\frac{X^{2}}{b}}dX |
|  | = | \left[\ensuremath{\frac{X^{3}}{3b}\right]_{0}^{b}} |}

\newslide{Variance}

\slides{* For the variance we also require 

| \left\langle X^{2}\right\rangle | = | \int_{0}^{\ensuremath{\infty}}X^{2}p\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{b}\ensuremath{\frac{X^{2}}{b}}dX |
|  | = | \left[\ensuremath{\frac{X^{3}}{3b}\right]_{0}^{b}} |
|  | = | \ensuremath{\frac{b^{3}}{3b}}-0 |}

\newslide{Variance}

\slides{* For the variance we also require 

| \left\langle X^{2}\right\rangle | = | \int_{0}^{\ensuremath{\infty}}X^{2}p\left(X\right)dX |
| --- | --- | --- |
|  | = | \int_{0}^{b}\ensuremath{\frac{X^{2}}{b}}dX |
|  | = | \left[\ensuremath{\frac{X^{3}}{3b}\right]_{0}^{b}} |
|  | = | \ensuremath{\frac{b^{3}}{3b}}-0 |
|  | = | b^{2} |}

\newslide{Variance}

\slides{* For the variance we also require $$
\begin{aligned}
\left\langle X^{2}\right\rangle  & = & \int_{0}^{\ensuremath{\infty}}X^{2}p\left(X\right)dX\\
 & = & \int_{0}^{b}\ensuremath{\frac{X^{2}}{b}}dX\\
 & = & \left[\ensuremath{\frac{X^{3}}{3b}\right]_{0}^{b}\\}
 & = & \ensuremath{\frac{b^{3}}{3b}}-0\\
 & = & b^{2}
\end{aligned}
$$The variance is $\left\langle X^{2}\right\rangle -\left\langle X\right\rangle ^{2}=b^{2}-\left(b\right)=b^{2}$.}

\newslide{Putting it Together}

\slides{* For simplicity we consider $\ensuremath{\mu}=\ensuremath{\frac{1}{\left\langle X\right\rangle }}.$ So $\ensuremath{\mu}=\ensuremath{\frac{2}{b}}$ and thus $b=\ensuremath{\frac{2}{\mu}}$.
* So we can write the second moment in terms of $\ensuremath{\mu}$. $\left\langle X^{2}\right\rangle =b^{2}$.}

\newslide{Putting it Together (continued)}

\slides{* Substituting in $b=\ensuremath{\frac{2}{\mu}}$ we have $\left\langle X^{2}\right\rangle =\ensuremath{\frac{4}{3\mu^{2}}}$.
* Substituting in to the Pollaczek-Khinchin formula we recover$$
\ensuremath{\bar{W}}=\ensuremath{\frac{2\rho}{3\mu\left(1-\rho\right)}}.$$}

\endif
