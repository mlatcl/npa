% generated — do not edit; scripts/convert/run.py
\ifndef{npaGenSlidesMg1}
\define{npaGenSlidesMg1}

<!-- original A4 foil 147: $M$/$G$/$1$ Queue -->

\newslide{$M$/$G$/$1$ Queue}

\slides{* Service times are *generally *distributed: cannot use the birth death process to analyse the system.
* We introduce a different type of analysis based on the mean residual service time.}

<!-- original A4 foil 147: $M$/$G$/$1$ Queue -->

\newslide{$M$/$G$/$1$ Queue (continued)}

\slides{* We will derive the Pollaczek-Khinchin formula.
* This gives the expected queueing time for any distribution of service times with *finite variance*.}

<!-- original A4 foil 148: Pollaczek-Khinchin formula -->

\newslide{Pollaczek-Khinchin formula}

\slides{* The Pollaczek-Khinchin formula is given as}

<!-- original A4 foil 148: Pollaczek-Khinchin formula -->

\newslide{Pollaczek-Khinchin formula (continued)}

\slides{* $\bar{W}$ is expected waiting time,
* $\left\langle X^{2}\right\rangle =\left\langle X^{2}\right\rangle _{p(X)}$ is the second moment under the service time distribution,
* utilisation factor is given as $\rho=\lambda\bar{X}$ and
* $\bar{X}=\left\langle X\right\rangle _{p(X)}$ is the mean under the service time distribution.}

<!-- original A4 foil 149: Proof of Pollaczek-Khinchin Formula -->

\newslide{Proof of Pollaczek-Khinchin Formula}

\slides{* Proof of the Pollaczek-Khinchin formula.
* In our proof we will make three assumptions
* The queue is FIFO queue, *i.e. *customers are served in the order they arrive. This assumption may be relaxed but it will simplify our proof.}

<!-- original A4 foil 149: Proof of Pollaczek-Khinchin Formula -->

\newslide{Proof of Pollaczek-Khinchin Formula (continued)}

\slides{* The arrival times are statistically independent of the service times.
* The service time distribution has a variance which is finite.
* To formulate the proof we introduce a concept known as the mean residual service time.}

<!-- original A4 foil 150: The Residual Service Time\label{sub:theResidualServiceTime} -->

\newslide{The Residual Service Time\label{sub:theResidualServiceTime}}

\slides{* The residual service time is
    ... the amount of service time that remains for the customer under service from the perspective of a customer who has just arrived in the queue.
* The first part of the proof occurs from the perspective of the arriving customer.
* The arriving customer is considered to be the $i$th customer.}

<!-- original A4 foil 151: Simple Definitions and Schematic -->

\newslide{Simple Definitions and Schematic}

\figure{\includepng{\diagramsDir/npa/residualServiceOverview}{100%}}{Schematic representation of residual service time.}{cap:schemeaticRST}

<!-- original A4 foil 151: Simple Definitions and Schematic -->

\newslide{Simple Definitions and Schematic (continued)}

\slides{* Example 1 in the Notes
* We introduce some simple definitions of terms.
* This enables us to draw a simple schematic of the system as it is perceived by the $i$th arrival. This is shown in Figure\  \ref{cap:schemeaticRST}.}

| $W_{i}$ | = | Waiting time in queue of $i$th customer. |
| --- | --- | --- |
| $R_{i}$ | = | `Residual service time' seen by the $i$th customer. |
| $X_{i}$ | = | Service time of the $i$th customer. |
| $k_{i}$ | = | Number of customers in the system when the $i$th customer arrives. |

<!-- original A4 foil 152: Wait for \emph{i}th Customer -->

\newslide{Wait for *i*th Customer}

\figure{\includepng{\diagramsDir/npa/residualServiceOverview}{100%}}{Schematic representation of residual service time.}{cap:schemeaticRST}

<!-- original A4 foil 152: Wait for \emph{i}th Customer -->

\newslide{Wait for *i*th Customer (continued)}

\slides{* From the figure the wait for the $i$th customer will be given by$$
W_{i}=R_{i}+\sum_{j=i-(k_{i}-1)}^{i-1}X_{j}$$
* Summing over both sides (*i.e. *for all the arriving customers up to the $I$th) $$
\sum_{i=1}^{I}W_{i}=\sum_{i=1}^{I}R_{i}+\sum_{i=1}^{I}\sum_{j=i-(k_{i}-1)}^{i-1}X_{j}$$
* Dividing through by $I$ gives us $$
\sum_{i=1}^{I}\frac{W_{i}}{I}=\sum_{i=1}^{I}\frac{R_{i}}{I}+\sum_{i=1}^{I}\sum_{j=i-(k_{i}-1)}^{i-1}\frac{X_{j}}{I}$$
* In the limit as $I\rightarrow\infty$ this becomes $$
\lim_{I\rightarrow\infty}\sum_{i=1}^{I}\frac{W_{i}}{I}=\lim_{I\rightarrow\infty}\sum_{i=1}^{I}\frac{R_{i}}{I}+\lim_{I\rightarrow\infty}\sum_{i=1}^{I}\frac{(k_{i}-1)X_{i}}{I}$$
* The terms of which are recognised as *time averages*.}

<!-- original A4 foil 153: Time Average Equivalence -->

\newslide{Time Average Equivalence}

\slides{* If we assume *time averages* are equivalent to *steady state averages* this gives $$
\left\langle W\right\rangle =\left\langle R\right\rangle +\left\langle \left(k-1\right)X\right\rangle .$$
* The length of the queue as seen by the $i$th arrival is independent of the $i$th arrival's length (our second assumption)}

<!-- original A4 foil 153: Time Average Equivalence -->

\newslide{Time Average Equivalence (continued)}

\slides{* this means $\left\langle (k-1)X\right\rangle =\left\langle k-1\right\rangle \left\langle X\right\rangle $ and since $(k-1)$ is the length of the queue we may write $$
\bar{W}=\bar{R}+\bar{N}_{Q}\bar{X}$$
* Using Little's theorem for the queue we have$$
\bar{N}_{Q}=\lambda\bar{W}$$
* Substituting back in we have$$
\bar{W}=\bar{R}+\lambda\bar{X}\bar{W}.$$}

<!-- original A4 foil 154: Wait in Terms of Residual Service Time -->

\newslide{Wait in Terms of Residual Service Time}

\slides{* From the previous slide:$$
\bar{W}=\bar{R}+\lambda\bar{X}\bar{W}.$$
* And the fact that $\rho=\lambda\bar{X}$ (which stems from Little's formula for the service) gives us $$
\bar{W}=\bar{R}+\rho\bar{W}$$}

<!-- original A4 foil 154: Wait in Terms of Residual Service Time -->

\newslide{Wait in Terms of Residual Service Time (continued)}

\slides{* Leading to 
\bar{W}=\frac{\bar{R}}{1-\rho}\label{eqn:arrivals}
* We now have the average queueing time in terms of the mean residual service time. To complete the Pollaczek-Khinchin formula we simply need to calculate $\bar{R}$.}

<!-- original A4 foil 155: Mean Residual Service Time from Departures Perspective -->

\newslide{Mean Residual Service Time from Departures Perspective}

\figure{\includepng{\diagramsDir/npa/residualTime}{100%}}{Graphical computation of mean residual time. $M\left(t\right)$ is the number of service completions in the interval $[0,\, t]$.}{cap:meanResidualGraphical}

<!-- original A4 foil 155: Mean Residual Service Time from Departures Perspective -->

\newslide{Mean Residual Service Time from Departures Perspective (continued)}

\slides{* We again turn to a graphical proof to obtain the value of the mean residual service time.}

<!-- original A4 foil 156: Residual Service Time -->

\newslide{Residual Service Time}

\slides{* The time average of the mean residual service time can then be calculated in terms of the area under the curve, $A(t)$.
* This is given by the area under each of the triangles, $$
A(t)=\frac{1}{2}\sum_{i=1}^{M(t)}X_{i}^{2}.$$}

\figure{\includepng{\diagramsDir/npa/residualTime}{100%}}{residualTime}{residualTime}

<!-- original A4 foil 157: Residual Service Time -->

\newslide{Residual Service Time}

\slides{* The average service time is the area divided by time, $t$, $$
A(t)=\frac{1}{2}\sum_{i=1}^{M(t)}X_{i}^{2}.$$ 
\frac{A(t)}{t} & = & \frac{M(t)}{t}\frac{A(t)}{M(t)}\\
 & = & \frac{1}{2}\frac{M(t)}{t}\frac{\sum_{i=1}^{M(t)}X_{i}^{2}}{M(t)}.
* we have introduced the number of arrivals after time $t$, as $M\left(t\right)$.
* As $t\rightarrow\infty$, *if the variance is finite*, we find that $M(t)\rightarrow\infty$ and we obtain$$
\bar{R}=\frac{1}{2}\lambda\left\langle X^{2}\right\rangle .$$}

<!-- original A4 foil 158: Pollaczek-Khinchin Formula -->

\newslide{Pollaczek-Khinchin Formula}

\slides{* Again assuming that time averages and ensemble averages are equal we substitute back into (\ref{eqn:arrivals}) to obtain the Pollaczek-Khinchin formula $$
\bar{W}=\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}.$$
* This implies that the total waiting time in the system is $$
\bar{T}=\bar{X}+\frac{\lambda\left\langle X^{2}\right\rangle }{2(1-\rho)}$$ and through Little's formula we can obtain the expected queue length, $\bar{N}_{Q}$, and the expected number in the system, $\bar{N}$.}

<!-- original A4 foil 159: Sanity Check --- Markov Service times -->

\newslide{Sanity Check --- Markov Service times}

\slides{* The exponentially distributed service times, $$
P\left(X\right)=\mu\exp\left(-\mu X\right),$$have a mean of $$
\bar{X}=\frac{1}{\mu}$$ and a variance of $\frac{1}{\mu^{2}}$ leading to a second moment$$
\left\langle X^{2}\right\rangle =\frac{2}{\mu^{2}}$$
* Substituting into the Pollaczek-Khinchin formula we obtain 
\bar{W} & = & \frac{\rho}{\mu\left(1-\rho\right)}\\
 & = & \frac{\rho}{\mu-\lambda}which is identical to those we derived for the $M/M/1$ queue.}

<!-- original A4 foil 160: Deterministic Service --- $M/D/1$ -->

\newslide{Deterministic Service --- $M/D/1$}

\slides{* Some systems have deterministic service times. For example, transmission of fixed length packets over a channel with a fixed bandwidth.
* We represent a `deterministic distribution' as$$
P\left(X\right)=\delta\left(X-\frac{1}{\mu}\right)$$where $\delta\left(\cdot\right)$is the Dirac delta function.
* For this system $$
\left\langle X\right\rangle =\frac{1}{\mu}$$and $$
\left\langle X^{2}\right\rangle =\frac{1}{\mu^{2}}$$*i.e. * the variance is zero.}

<!-- original A4 foil 161: P-K Formula for Deterministic Systems -->

\newslide{P-K Formula for Deterministic Systems}

\slides{* For this system $$
\left\langle X\right\rangle =\frac{1}{\mu}$$and $$
\left\langle X^{2}\right\rangle =\frac{1}{\mu^{2}}$$*i.e. * the variance is zero.
* Substituting into the Pollaczek-Khinchin formula we obtain $$
\bar{W}=\frac{\rho}{2\mu\left(1-\rho\right)}.$$}

<!-- original A4 foil 162: Table of Delays and Average Numbers in System -->

\newslide{Table of Delays and Average Numbers in System}

\slides{* In fact we may derive the full range of results for these distributions.}

<!-- original A4 foil 162: Table of Delays and Average Numbers in System -->

\newslide{Table of Delays and Average Numbers in System (continued)}

| Expected value | General | Exponential | Deterministic |
| --- | --- | --- | --- |
| $\bar{W}$ | $\frac{\lambda}{2(1-\rho)}\left\langle X^{2}\right\rangle $ | $\frac{\rho}{\mu(1-\rho)}$ | $\frac{\rho}{2\mu(1-\rho)}$ |
| $\bar{T}=\bar{W}+\frac{1}{\mu}$ | $\frac{\lambda}{2(1-\rho)}\left\langle X^{2}\right\rangle +\frac{1}{\mu}$ | $\frac{1}{\mu(1-\rho)}$ | $\frac{2-\rho}{2\mu(1-\rho)}$ |
| $\bar{N_{Q}}=\lambda\bar{W}$ | $\frac{\lambda^{2}}{2(1-\rho)}\left\langle X^{2}\right\rangle $ | $\frac{\rho^{2}}{(1-\rho)}$ | $\frac{\rho^{2}}{2(1-\rho)}$ |
| $\bar{N}=\lambda\bar{W}+\rho=$ | $\frac{\lambda^{2}}{2(1-\rho)}\left\langle X^{2}\right\rangle +\rho$ | $\frac{\rho}{1-\rho}$ | $\frac{\rho(2-\rho)}{2(1-\rho)}$ |

<!-- original A4 foil 163: Example --- Uniform Service Times -->

\newslide{Example --- Uniform Service Times}

\slides{* Uniform Service Times --- $M/U/1$.
* Consider a uniform probability distribution is defined between 0 and $b$ for $X>0$ as$$
U\left(X|b\right)=\left\{ {cc}
\frac{1}{b} & 0<X\leq b\\
0 & X>b\right.$$show that the man of this uniform distribution is given by $\frac{b}{2}$ and its variance by $\frac{b^{2}}{12}$ and find the expected waiting time for an $M/U/1$ queue?}}

<!-- original A4 foil 164: Answer -->

\newslide{Answer}

\slides{* For the mean we have
\left\langle X\right\rangle  & = & \int_{0}^{\infty}Xp\left(X\right)dX\\
\\\\\\\\}

<!-- original A4 foil 165: Answer -->

\newslide{Answer}

\slides{* For the mean we have
\left\langle X\right\rangle  & = & \int_{0}^{\infty}Xp\left(X\right)dX\\
 & = & \int_{0}^{\infty}XU\left(X|b\right)dX\\
\\\\\\}

<!-- original A4 foil 166: Answer -->

\newslide{Answer}

\slides{* For the mean we have
\left\langle X\right\rangle  & = & \int_{0}^{\infty}Xp\left(X\right)dX\\
 & = & \int_{0}^{\infty}XU\left(X|b\right)dX\\
 & = & \int_{0}^{b}\frac{X}{b}dX\\
\\\\}

<!-- original A4 foil 167: Answer -->

\newslide{Answer}

\slides{* For the mean we have
\left\langle X\right\rangle  & = & \int_{0}^{\infty}Xp\left(X\right)dX\\
 & = & \int_{0}^{\infty}XU\left(X|b\right)dX\\
 & = & \int_{0}^{b}\frac{X}{b}dX\\
 & = & \left[\frac{X^{2}}{2b}\right]_{0}^{b}\\
\\}

<!-- original A4 foil 168: Answer -->

\newslide{Answer}

\slides{* For the mean we have
\left\langle X\right\rangle  & = & \int_{0}^{\infty}Xp\left(X\right)dX\\
 & = & \int_{0}^{\infty}XU\left(X|b\right)dX\\
 & = & \int_{0}^{b}\frac{X}{b}dX\\
 & = & \left[\frac{X^{2}}{2b}\right]_{0}^{b}\\
 & = & \frac{b^{2}}{2b}-0}

<!-- original A4 foil 169: Answer -->

\newslide{Answer}

\slides{* For the mean we have
\left\langle X\right\rangle  & = & \int_{0}^{\infty}Xp\left(X\right)dX\\
 & = & \int_{0}^{\infty}XU\left(X|b\right)dX\\
 & = & \int_{0}^{b}\frac{X}{b}dX\\
 & = & \left[\frac{X^{2}}{2b}\right]_{0}^{b}\\
 & = & \frac{b^{2}}{2b}-0\\
 & = & \frac{b}{2}}

<!-- original A4 foil 170: Answer -->

\newslide{Answer}

\slides{* For the mean we have
\left\langle X\right\rangle  & = & \int_{0}^{\infty}Xp\left(X\right)dX\\
 & = & \int_{0}^{\infty}XU\left(X|b\right)dX\\
 & = & \int_{0}^{b}\frac{X}{b}dX\\
 & = & \left[\frac{X^{2}}{2b}\right]_{0}^{b}\\
 & = & \frac{b^{2}}{2b}-0\\
 & = & \frac{b}{2}}

<!-- original A4 foil 171: Variance -->

\newslide{Variance}

\slides{* For the variance we also require 
\left\langle X^{2}\right\rangle  & = & \int_{0}^{\infty}X^{2}p\left(X\right)dX\\
\\\\\\}

<!-- original A4 foil 172: Variance -->

\newslide{Variance}

\slides{* For the variance we also require 
\left\langle X^{2}\right\rangle  & = & \int_{0}^{\infty}X^{2}p\left(X\right)dX\\
 & = & \int_{0}^{b}\frac{X^{2}}{b}dX\\
\\\\}

<!-- original A4 foil 173: Variance -->

\newslide{Variance}

\slides{* For the variance we also require 
\left\langle X^{2}\right\rangle  & = & \int_{0}^{\infty}X^{2}p\left(X\right)dX\\
 & = & \int_{0}^{b}\frac{X^{2}}{b}dX\\
 & = & \left[\frac{X^{3}}{3b}\right]_{0}^{b}\\
\\}

<!-- original A4 foil 174: Variance -->

\newslide{Variance}

\slides{* For the variance we also require 
\left\langle X^{2}\right\rangle  & = & \int_{0}^{\infty}X^{2}p\left(X\right)dX\\
 & = & \int_{0}^{b}\frac{X^{2}}{b}dX\\
 & = & \left[\frac{X^{3}}{3b}\right]_{0}^{b}\\
 & = & \frac{b^{3}}{3b}-0}

<!-- original A4 foil 175: Variance -->

\newslide{Variance}

\slides{* For the variance we also require 
\left\langle X^{2}\right\rangle  & = & \int_{0}^{\infty}X^{2}p\left(X\right)dX\\
 & = & \int_{0}^{b}\frac{X^{2}}{b}dX\\
 & = & \left[\frac{X^{3}}{3b}\right]_{0}^{b}\\
 & = & \frac{b^{3}}{3b}-0\\
 & = & \frac{b^{2}}{3}}

<!-- original A4 foil 176: Variance -->

\newslide{Variance}

\slides{* For the variance we also require \begin{eqnarray*}
\left\langle X^{2}\right\rangle  & = & \int_{0}^{\infty}X^{2}p\left(X\right)dX\\
 & = & \int_{0}^{b}\frac{X^{2}}{b}dX\\
 & = & \left[\frac{X^{3}}{3b}\right]_{0}^{b}\\
 & = & \frac{b^{3}}{3b}-0\\
 & = & \frac{b^{2}}{3}\end{eqnarray*}The variance is $\left\langle X^{2}\right\rangle -\left\langle X\right\rangle ^{2}=\frac{b^{2}}{3}-\left(\frac{b}{2}\right)=\frac{b^{2}}{12}$.}

<!-- original A4 foil 177: Putting it Together -->

\newslide{Putting it Together}

\slides{* For simplicity we consider $\mu=\frac{1}{\left\langle X\right\rangle }.$ So $\mu=\frac{2}{b}$ and thus $b=\frac{2}{\mu}$.
* So we can write the second moment in terms of $\mu$. $\left\langle X^{2}\right\rangle =\frac{b^{2}}{3}$.}

<!-- original A4 foil 177: Putting it Together -->

\newslide{Putting it Together (continued)}

\slides{* Substituting in $b=\frac{2}{\mu}$ we have $\left\langle X^{2}\right\rangle =\frac{4}{3\mu^{2}}$.
* Substituting in to the Pollaczek-Khinchin formula we recover$$
\bar{W}=\frac{2\rho}{3\mu\left(1-\rho\right)}.$$}

\endif
