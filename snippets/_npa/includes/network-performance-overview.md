\ifndef{networkPerformanceOverview}
\define{networkPerformanceOverview}

\section{Network Performance Analysis}

\notes{This course introduces the tools for design and analysis of telecommunication networks. The core tools are probabilistic: we assume that traffic is stochastic.}

\notes{The same techniques apply beyond telecommunications. Queues form at compute servers, in databases handling queries, at cashpoints, in supermarkets, and in telephone call centres. The principles apply in each of those settings.}

\slides{* Traffic is stochastic: probability is the modelling language
* Same tools: routers, servers, call centres, supermarket checkouts}

\subsection{Design and Quality}

\notes{For network design we care about two related questions.}

\slidesincremental{
* Design: memory in the router, bandwidth between routers, processing power
* Quality: average delay, worst-case delay, probability of dropping a packet
* Resources are finite
}

\notes{**Design issues.** When building or buying a router, how much memory should we allow? How much bandwidth do we need between routers? How much processing power should the router have so that it can use that bandwidth?}

\notes{**Quality issues.** What will be the average delay for end users given our design? What is the worst-case delay? How likely is the system to drop packets?}

\subsection{Terminology}

\notes{A series of communications between two users is a *session*. The interactions consist of *messages*, each of which may be split into *packets*.}

\notes{One example of a session is a lecture: mainly one-way communication from lecturer (server) to students (clients). Messages cover different subjects; packets might be the sentences. The medium is air.}

\slides{* Session → messages → packets
* Lecture as a session: mostly one-way, air as the medium}

\subsection{Session Characteristics}

\notes{FTP, VoIP, and HTTP sessions look very different. Six characteristics of a session matter for protocol and network design.}

\slidesincremental{
* Message arrival rate (Poisson, deterministic, …)
* Session holding time
* Expected message length and its distribution
* Allowable delay (low for VoIP, higher for FTP)
* Reliability (FTP must be lossless; VoIP can lose packets)
* Message and packet ordering
}

\notes{This course concentrates on the first five.}

\subsection{Circuit Switching and Packet Switching}

\notes{We have already met two kinds of network.}

\slides{* Circuit switching: a guaranteed channel, used for telephony
* Packet switching: store and forward; dynamic routing or virtual circuits}

\notes{**Circuit switching** can waste bandwidth, because the two parties may not use the reserved channel all the time. Once connected, though, delay is known. The sum of session rates on a link cannot exceed the link capacity; new sessions are rejected when capacity is reached. That is natural for telephony, where each session has the same rate $r_s$.}

\notes{**Packet switching** uses bandwidth more efficiently: idle time on a conversation can carry someone else’s packets. Delay is then harder to guarantee.}

\figure{\includepng{\diagramsDir/npa/aliceBobCircuit}{70%}}{A simple circuit-switching network connecting Alice and Bob. The session dominates both phone lines.}{circuit-switch-alice-bob}

\notes{Alice calls Bob on the phone: the session occupies both lines. Alternatively they use an instant-messenger voice session while Bob’s friend Carol shares the land line to reach David’s web server.}

\figure{\includepng{\diagramsDir/npa/aliceBobPacket}{70%}}{A simple packet-switching network connecting Alice, Bob, Carol, and David. Congestion on the shared land line produces variable queueing delay.}{packet-switch-alice-bob}

\notes{A router in Bob’s house now shares the land line. Bob and Carol can both use it; if Carol downloads a large file, Bob sees a variable delay. That queueing delay is the object of this course.}

\subsection{The Layered Model}

\notes{The TCP/IP model is more compact than the seven-layer OSI model and is the one we will use. See Tanenbaum (4th edition, p. 41) for more detail.}

\figure{\includepng{\diagramsDir/npa/layeredModel}{70%}}{A schematic of the layered model for TCP/IP networks.}{tcp-ip-layered-model}

\slidesincremental{
* Application: HTTP, mail, voice, …
* Transport: TCP (lossless, ordered, flow control) or UDP (unreliable)
* Internet: IP, so a packet can leave one network and arrive on another
}

\subsection{Communication Media}

\notes{Circuit-switched networks share a line by multiplexing: time-division or frequency-division. Neither is perfectly efficient. Packet-switched networks give bandwidth to a session as required. In a simple FIFO system a packet is transmitted if the queue is empty; otherwise it waits. There are two delays: a variable queueing delay, and a transmission delay equal to packet length times the reciprocal of the line rate.}

\notes{Radio goes back to Marconi. The most basic wireless packet networks (ALOHA) used one channel. If two stations transmit at once, both packets are lost. Thinwire Ethernet has the same collision structure, with a coaxial cable as the medium.}

\slides{* Multiplexing vs statistical sharing
* Queueing delay (variable) + transmission delay (packet length / rate)
* ALOHA and Ethernet: one channel, collisions}

\subsection{The Road Ahead}

\slidesincremental{
* Probability review
* Simple queueing models: Little, $M/M/1$, $M/M/\infty$, $M/M/m$, $M/M/m/m$, $M/G/1$
* Simulation of queues
}

\endif
