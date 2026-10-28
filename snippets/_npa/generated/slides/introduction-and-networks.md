\ifndef{npaGenSlidesIntroductionAndNetworks}
\define{npaGenSlidesIntroductionAndNetworks}

\newslide{Introduction and Background}

\slides{* Queueing theory dates back to the beginning of the 20th Century and the pioneering work of Agner Krarup Erlang (1878-1929).
* Erlang was a Danish Telecoms Engineer who published the first paper on queueing theory [@Erlang:theory09].}

\newslide{Introduction and Background (continued)}

\slides{* Initially, telephone call routing was achieved manually.
* The invention of the *automatic telephone exchange* (through the Strowger switch) in 1891 brought about the need for a theoretical study of the operation of telephone exchanges.
* Erlang's provided theoretical studies of these circuit switching networks.}

\newslide{Computer Networks}

\slides{* Circuit switched networks were designed for telephone communication between two correspondents.
* By the early 1960s *packet switching networks* came into being.
* ARPANET was predecessor of the internet.}

\slides{\figure{\includepng{\diagramsDir/npa/1975_net_map}{80%}}{The ARPANET in 1975, image courtesy of the Computer History Museum, [http://www.computerhistory.org](http://www.computerhistory.org).}{1975-net-map}}

\newslide{Network Performance Analysis}

\slides{* In this course we will introduce you to the tools for design and analysis of telecommunications networks.
* The core tools of this analysis are probability based: there is an assumption that the traffic in the system is stochastic.
* The techniques we will cover are applicable beyond the design and analysis of telecommunication networks. *e.g.* compute servers dealing with submitted jobs and databases handling queries, cashpoints queues, supermarket queues, telephone call centres *etc*..}

\newslide{Practical Considerations}

\slides{* Broadly speaking we need to focus on two interrelated areas in our analysis:}

\newslide{Practical Considerations (continued)}

\slides{1. **Design Issues**: when building or buying a router how much memory should we allow for? How much bandwidth do we need between routers? How much processing power should the router have so that it may exploit that bandwidth effectively?
2. **Quality Issues**: what will be the average delay for end users given our network design? What is the worst case delay? How likely is the system to drop packets?
* These are important because resources are finite, there are limitations on the available bandwidth, processor speeds and memory.}

\newslide{Terminology}

\slides{* A series of communications between two users/computers is known as a *session*.
* The interactions themselves consist of *messages* each of which may be split into *packets*.}

\newslide{Session Characteristics}

\slides{* Characteristics of the session vary according to protocol:
* **Message arrival rate**. We can seek to model the arrivals as: *Poisson arrivals*, *deterministic arrivals*, *uniform arrivals* or as coming from a more general class of distributions.
* **Session holding time**: The length of a session.
* **Expected message length** and **length distribution**, message lengths can be modeled as *exponential distributions*,*uniform length*.}

\newslide{Session Characteristics (continued)}

\slides{* **Allowable delay** - acceptable expected delays vary. The acceptable delay is low for VoIP and quite high for FTP.
* **Reliability** - FTP *must* be error free but VoIP can have some bit errors or packet loss without major consequences.
* **Message and packet ordering** - Some sessions will require that the packets arrive in the order they are sent: for example database requests.
* In this course we will be particularly interested in the first five of these characteristics.}

\newslide{Network Types}

\slides{* **Circuit\** Switching: used for telephone routing. Guarantees an open `channel' between two peers.
* **Packet\** Switching or Store and Forward Switching: used for data. May operate via
* **Dynamic\** Routing Each packet of the message moves through the network independently.
* **Virtual\** Circuit\  Routing A fixed path through the network is provided for the entire message.}

\newslide{Network Types (continued)}

\slides{* The character of the two approaches are quite different.}

\newslide{Circuit\  Switching}

\slides{* wasteful in terms of bandwidth. Nodes may not be using all the available bandwidth reserved for them.
* a guaranteed channel is provided with a known communication delay associated with it.}

\newslide{Circuit\  Switching (continued)}

\slides{* the sum of rates for all sessions using a link cannot exceed the total capacity of the link. New sessions must be rejected when the link capacity is reached.
* used for telephone networks where the session rate, $r_{s}$, is the same for each session. Switching would be more complex for data networks and the nature of transmission would also mean that the links are inefficiently used.}

\newslide{Packet Switching}

\slides{* Packet switching makes efficient use of bandwidth because, whilst communication between two nodes may be idle for a period of time, packets from another communication may be sent along the same line.
* Because it is unknown *a priori* how much bandwidth will be available it is difficult to guarantee a maximum delay.}

\newslide{Communication Media}

\slides{* Circuit switching networks may share a communication through multiplexing (*e.g.* time division multiplexing or frequency division multiplexing.)
* Both are not 100% efficient (time multiplexing requires a small amount of time for switching to occur, and frequency division multiplexing requires a small `buffer' band of frequencies between each session.}

\newslide{Communication Media (continued)}

\slides{* Packet switching networks dedicate communication bandwidth to each channel as required. In a simple `first in, first out' (FIFO) system, packets arrive and, if the queue is empty, they are transmitted. Otherwise they are stored and await their turn for transmission.
  \footnote{Also known as `first come, first served' (FCFS).}
* In packet switching there are two delays: a queueing delay and a transmission delay. The queueing delay is variable, transmission delay will be fixed .}

\newslide{The Road Ahead}

\slides{* **Probability\** Review Review of probability theory.
* **Simple\** Queuing\  models Simple models of queues based on probability theory. Little's formula, $M/M/1$ queue, $M/M/\ensuremath{\infty}$, $M/M/m$, $M/M/m/m$ and $M/G/1$.
* **Simulation** Simulation of queueing systems.}

\newslide{Examples}

\slides{1. As a simple example let's consider a database (perhaps MySQL). We are constructing it from existing parts. We have two CPU/motherboard systems and two separate disk systems, their expected characteristics are shown in Table\  \ref{cap:SQLserver}. Which should we match with which? Are we better off building one faster system and one slower system? Or should we build two systems that have a similar performance?
2. You are starting an e-commerce company.
3. You have a tight budget.
4. You have:

$$
\begin{aligned}
5. two disk systems (1 & 2).
6. two CPU systems (A & B).
\end{aligned}
$$}

\newslide{Examples (continued)}

\slides{1. Which should you combine to make your two servers?
  % empty table
2. Answer
3. You should match A with 2 and B with 1.
4. This avoids bottlenecks:
5. Disk 1 would wait for CPU A to process about 50% of the time.
6. CPU B would wait for disk 2 to access about 50% of the time.}

\endif
