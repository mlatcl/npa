\ifndef{erlangAndMilestones}
\define{erlangAndMilestones}

\section{Introduction}

\notes{Welcome to Network Performance Analysis: sixteen lectures and two lab sessions on queueing theory and network simulation.}

\notes{Queueing theory dates from the beginning of the twentieth century and the work of **Agner Krarup Erlang** (1878–1929), a Danish telephone engineer who published the first paper on the subject [@Erlang:theory09].}

\slides{* Queueing theory: Erlang (1878–1929), Copenhagen Telephone Company
* This course: probability, Markov queues, Little, Erlang B/C, $M/G/1$, networks, ALOHA
* Sixteen lectures and two labs}

\notes{The first two chapters place that theory in the development of worldwide communication networks. For further reading see [Wikipedia](http://en.wikipedia.org) and the [Computer History Museum](http://www.computerhistory.org).}

\section{Early Milestones}

\notes{The first major development in telecommunications was the *telegraph*. **Samuel F. B. Morse** built an electrical telegraph that exploited the link between magnetism and electricity. His first working system sent a short message from Baltimore to Washington, D.C. on 24 May 1844: “What hath God wrought?” Ten years later there were 23,000 miles of wire across the United States.}

\notes{A key limitation of the telegraph was that it provided only one channel per wire. Work on using a single wire for multiple channels (multiplexing) led indirectly to the *telephone*, patented by **Alexander Graham Bell** (1847–1922) on 7 March 1876.}

\notes{**Guglielmo Marconi** (1874–1937) developed wireless telegraphy, patented in July 1897, and founded the Wireless Telegraph and Signal Company. By December 1901 short-wave transmission crossed the Atlantic between England and Canada (over 2,100 miles).}

\slides{* Telegraph: Morse, 1844, Baltimore to Washington
* Telephone: Bell, 1876 — multiplexing a wire led here
* Wireless: Marconi, 1897; transatlantic 1901}

\section{Automated Telephone Networks}

\notes{Early telephone routing was manual. Operators at the exchange used patch boards to connect callers. **Almon Strowger** (1839–1902) invented the automatic telephone exchange (the Strowger switch) in 1891, and that created a need for a theoretical study of how exchanges behave under demand.}

\notes{The network of interconnected phone lines is a *circuit switching* network: lines are switched between two subscribers to form a connection. Erlang’s contribution was to give theoretical studies of these networks that allowed exchanges to be designed to meet demand.}

\slides{* Strowger switch, 1891: automatic exchange
* Circuit switching: a reserved path between two subscribers
* Erlang: size the exchange to the offered load}

\section{Information Theory}

\notes{As telephone networks grew, so did the need for a theory of what they carry. Networks transmit “information”, but talk of channel capacity is empty without a definition. **Claude E. Shannon** (1916–2001) wrote *A Mathematical Theory of Communication* [@Shannon-info48], which founded information theory and gave a mathematical meaning to the capacity of a channel. We will not cover that theory here.}

\slides{* Shannon (1948): a mathematical theory of communication
* Channel capacity needs a definition of information
* Not examinable in this course, but it is why packet networks make sense}

\endif
