\ifndef{npaGenNotesIntroductionAndNetworks}
\define{npaGenNotesIntroductionAndNetworks}

\notes{\section{Introduction}}

\notes{Welcome to Network Performance Analysis, 16 lectures and 2 lab sessions on queueing theory and network simulation.
Queueing theory dates back to the beginning of the 20th Century and the pioneering work of **Agner Krarup Erlang** (1878-1929) a Danish Telecoms Engineer who published the first paper on queueing theory [@Erlang:theory09].
In these first two chapters we will introduce the background for the material which follows: the development of worldwide communication networks. For further reading please check [http://en.wikipedia.org](http://en.wikipedia.org) and [http://www.computerhistory.org](http://www.computerhistory.org).}

\notes{\section{Early Milestones}}

\notes{Perhaps the first major development in telecommunications was *the telegraph*. **Samuel F. B. Morse** developed ideas for the electrical telegraph which exploited the relationship between magnetism and electricity. His first working system sent a short message from Baltimore to Washington D.C. (two cities that are conveniently close together!). It was sent on May 24th, 1844: `What hath God wrought?'. Ten years later 23,000 miles of wire across the United States.
At the time, a key limitation of the telegraph was that it only provided one channel per wire for communication. Work in using a single wire for multiple channels (multiplexing) indirectly led to the invention of *the telephone*which was patented by **Alexander Graham Bell** (1847-1922) in March 7th, 1876.

$$
\begin{aligned}
The development of a *wireless telegraphy* system by the Italian born engineer **Guglielmo Marconi** (1874-1937), patented in July 1897, led to the foundation of the Wireless Telegraph & Signal Company. By December 1901 short wave transmission across the Atlantic between England and Canada (over 2,100 miles).
\end{aligned}
$$

}

\notes{\section{Automated Telephone Networks}}

\notes{Initially, telephone call routing was achieved manually. Operators at the exchange used patch boards to make physical connections between the callers. The invention, by **Almon Strowger** (1839-1902), of the *automatic telephone exchange* (through the Strowger switch) in 1891 brought about the need for a theoretical study of the operation of telephone exchanges.
The network of interconnected phone lines is now known as a *circuit switching network*. It is a network of lines which can be switched between two subscribers to form a connection.
Erlang's contribution was to provide theoretical studies of these networks which allowed telephone exchanges to be designed to meet demand.}

\notes{\section{Information Theory}}

\notes{As 'phone networks developed the need for underlying theory grew. Networks transmit `information' but to discuss concepts such as channel capacity with out a formal definition for information is meaningless. **Claude E. Shannon** (1916-2001) wrote a seminal paper *A Mathematical Theory of Communication* [@Shannon:info48] which founded the field of information theory and revolutionised the way we look at telecommunication. This work enabled us to discuss concepts such as the capacity of a channel with a well founded underlying mathematical theory. We will not cover the ideas from this course here, but some students will learn more about this in the module COM6862: *Applications of Coding, Information and Learning Theories*.}

\notes{\section{Computer Networks}}

\notes{Circuit switched networks were designed for telephone communication between two correspondents. These were the first worldwide communication networks. However, by the early 1960s the need for a new type of communication network was arising. In circuit switching networks, a permanently open line connects the correspondents. A fixed bandwidth is available to them for communication. If they do not use this bandwidth it cannot be made available to other network users. In *packet switching networks* or store and forward switching networks the bandwidth is not reserved in this way: it is distributed across the network user base. The information a user sends (whether it be voice like in a phone conversation and VoIP or a file using FTP) is split into packets which are routed across the network to the desired destination. If a required communication line is in use the packet is stored in a queue until the line becomes available (thus the name store and forward switching). The ideas behind packet switching networks were developed independently by **Paul Baran** (1926-) at the RAND corporation in the U.S. and **Donald Davies** (1924-2000) of the National Physical Laboratory in the U.K.. **Leonard Kleinrock's** (1934-) 1962 thesis (later published as a book [@Kleinrock:communication64]) provided a mathematical theory that underpinned these networks.
\footnote{Voice over IP, the protocol for having phone conversations over the internet.}
\footnote{FTP is the file transfer protocol, a much older protocol which dates back to the formation of the ARPANET.}}

\speakernotes{Student exercise: summarise differences between packet switched and circuit switched networks.}

\notes{\subsection{ARPANET}}

\notes{The Advanced Research Projects Agency (ARPA) funded a network that actually implemented these ideas. In 1969 the ARPA network connected four nodes at the University of California, Los Angeles (UCSB); the Stanford Research Institute; the University of California, Santa Barbara (UCSB) and the University of Utah. By 1975 (see Figure\  \ref{cap:arpaNet1975}) the network had expanded to cover most of the major universities (61 nodes) in the U.S. as well as a node at University College London in the U.K..
ARPANET was the first network for computer communications, it was restricted to non-commercial use and funded by ARPA and NSF until 1990. With the increase in communication, protocols became far more important. Just as spellings of European languages became standardised after the introduction of the the printing press communication protocols also became more prevalent. Telnet and file transfer protocols (FTP) were developed in 1971, but perhaps the most important protocol developed at that time was the transmission control protocol (TCP) developed in the mid-seventies by **Vinton G. Cerf** (1943-) and **Robert E. Kahn** (1938-) [@Cerf:packet74]. These protocols allow interconnection between networks thereby enabling the formation of the internet.}

\figure{\includepng{\diagramsDir/npa/1975_net_map}{100%}}{The ARPANET in 1975, image courtesy of the Computer History Museum, [http://www.computerhistory.org](http://www.computerhistory.org). Some abbreviations: UCB - University of California at Berkeley; UCSD - University of California at San Diego; UCLA - University of California at Los Angeles; PDP-XX - the PDP machines were early mini-computers made by DEC with a price tag of around $20,000. The machines starting with 360 and 370 are IBM mainframe machines. Note the transatlantic link to London and the link over the Pacific to Hawaii. There are 61 nodes in total on this network.}{cap:arpaNet1975}

\notes{\subsection{The Internet}}

\notes{By 1977 Cerf and Kahn were able to send messages across networks including the `Packet Radio net', SATNET and the ARPANET. At a similar time **Robert Metcalfe** (1946-) was developing Ethernet at Xerox PARC. Ethernet was inspired by the ALOHA networks at the University of Hawaii. Each machine in the ALOHA network communicated across the same frequency radio channel. This meant that if several communications where sent at the same time `collisions' could occur resulting in garbled messages. A procedure for detecting and retransmitting the message was required. For Ethernet networks a cable is the medium of transmission, rather than a radio frequency. Ethernet was supported by an alliance of companies: DEC, Intel and Xerox. This led to Ethernet networks superseding other competing approaches such as token ring, FDDI and ARCNET. The cheap availability of Ethernet and computers in general contributed to an explosion in the number of networks associated with the internet.
By 1990 when ARPANET was formally shutdown it had grown to 300,000 hosts and connected countries across the globe, it evolved into the NSFNet which became the backbone of the internet. In 1991 the internet was opened to commercial traffic, the commercialisation of the internet in combination with the invention of the hyper-text markup language (HTML) and universal resource locaters (URL) by **Tim Berners-Lee** (1955-) formed the foundations of the modern internet.}

\speakernotes{\begin{itemize}
    \item Design and analysis of networks.
    \item Queues arise in a variety of IT scenarios.
    \begin{itemize}
      \item cashpoints, supermarkets, call centres *etc*..
    \end{itemize}
    \item The principles we teach cover all these scenarios.
  \end{itemize}}

\notes{\section{Practical Considerations}}

\notes{For the moment, let's focus on, for example, network design. Broadly speaking we need to focus on two interrelated areas in our analysis:}

\notes{1. **Design Issues**: when building or buying a router how much memory should we allow for? How much bandwidth do we need between routers? How much processing power should the router have so that it may exploit that bandwidth effectively?
2. **Quality Issues**: what will be the average delay for end users given our network design? What is the worst case delay? How likely is the system to drop packets?}

\notes{These are important because resources are finite, there are limitations on the available bandwidth, processor speeds and memory.}

\speakernotes{\begin{itemize}
    \item In our analysis we should consider:
    \begin{enumerate}
      \item **Design Issues**:
      \begin{itemize}
        \item how much memory? should we allow for?
        \item How much bandwidth?
        \item How much processing power?
      \end{itemize}
      \item **Quality Issues**:
      \begin{itemize}
        \item Average delay for end users.
        \item The worst case delay.
        \item Will the system to drop packets?
      \end{itemize}
    \end{enumerate}
  \end{itemize}}

\notes{\section{Terminology}}

\notes{Before we cover these issues in more detail, let's introduce some standard terminology. Typically a series of communications between two users/computers is known as a *session*. The interactions themselves consist of *messages* each of which may be split into *packets*.
One example of a session would be a lecture. The session consists of a mainly one-way communication between the lecturer (the server) and the students (multiple clients). In this case most of the information transfer is one-way with the lecturer sending a series of messages, each involving a different subject: the lecturer' s identity, the course's subject matter *etc*. and you acknowledging by your lively reactions. Each message consists of a series of packets, in this case perhaps the sentences that the lecturer speaks. The communication medium is the air.}

\notes{\section{Session Characteristics}}

\notes{Depending on the nature of the information communicated between the client and the server the characteristics of the session can vary dramatically. An FTP session may involve a few packets from the client to request a file followed by many packets from the server to send the file. A VoIP session will involve large numbers of packets between two users and no obvious client/server relationship. An hypertext transfer protocol (HTTP) session may involve long periods of inactivity as the client reads the pages they have downloaded.
Each of the following six criteria/characteristics of a session may need to be considered in the design of the protocol and the network.}

\notes{1. **Message arrival rate**. We can seek to model the arrivals as: *Poisson arrivals*, *deterministic arrivals*, *uniform arrivals* or as coming from a more general class of distributions.
2. **Session holding time**: The length of a session.
3. **Expected message length** and **length distribution**, message lengths can be modelled as *exponential distributions*,*uniform length*.
4. **Allowable delay** - acceptable expected delays vary. The acceptable delay is low for VoIP and quite high for FTP.
5. **Reliability** - FTP *must* be error free but VoIP can have some bit errors or packet loss without major consequences.
6. **Message and packet ordering** - Some sessions will require that the packets arrive in the order they are sent: for example database requests.}

\notes{In this course we will be particularly interested in the first five of these characteristics.}

\notes{\section{Network Types}}

\notes{In our review of the history of communication networks, we have already met two distinct kinds of network.}

\notes{* **{Circuit~Switching:}** used for telephone routing. Guarantees an open `channel' between two peers.
* **{Packet~Switching}** or Store and Forward Switching: used for data. May operate via
* **{Dynamic~Routing}** Each packet of the message moves through the network independently.
* **{Virtual~Circuit~}** Routing A fixed path through the network is provided for the entire message.}

\notes{The character of the two approaches are quite different.}

\notes{\subsection{Circuit\  Switching}}

\notes{Circuit switching can be wasteful in terms of bandwidth. The communicating nodes may not be using all the available bandwidth reserved for them all of the time. However, once connection is established, a guaranteed channel is provided with a known communication delay associated with it.
In a circuit switching network, the sum of rates for all sessions using a link cannot exceed the total capacity of the link. New sessions must be rejected when the link capacity is reached. The approach is used for telephone networks where the session rate, $r_{s}$, is the same for each session. Switching would be more complex for data networks and the nature of transmission would also mean that the links are inefficiently used.}

\notes{\subsection{Packet Switching}}

\notes{Packet switching makes efficient use of bandwidth because, whilst communication between two nodes may be idle for a period of time, packets from another communication may be sent along the same line. However because it is unknown *a priori* how much bandwidth will be available it is difficult to guarantee a maximum delay.}

\notes{\subsection{Illustrative Example}}

\notes{Alice and Bob both have telephone lines. Alice decides to call Bob using the phone line. Here the make use of a circuit switching network provided by their telephone supplier (Figure\  \ref{cap:circuitSwitch}). The session dominates both phone lines preventing use by other `clients'.}

\figure{\includepng{\diagramsDir/npa/aliceBobCircuit}{70%}}{A simple circuit switching network connecting Alice and Bob.}{cap:circuitSwitch}

\notes{Alternatively Alice and Bob use MSN messenger to communicate (either via voice or typing), and Bob's friend Carol shares his fixed land line connection to access David's web server (Figure\  \ref{cap:packetSwitch}).}

\figure{\includepng{\diagramsDir/npa/aliceBobPacket}{70%}}{A simple packet switching network connecting Alice, Bob, Carol and David.}{cap:packetSwitch}

\notes{Now the fixed land line is managed by some form of router in the local area network in Bob's house. The advantage is that Bob and Carol may both use the land line for communication the disadvantage is that if the land line becomes congested *e.g.* as a result of Carol downloading a large file from David's web server, Bob will notice a variable delay (delays also occur with circuit switching but they are known as transmission delays and should be of fixed length) in his communication with Alice due to queueing occurring at his Internet Service Provider and in his LAN's router. This can be particularly irritating for voice conversation, as anyone who has used MSN messenger for voice communication over a low bandwidth channel will attest.}

\notes{\section{The Layered Model}}

\notes{We now review the layered model for TCP/IP networks, you are referred to Tanenbaum (4th Edition pg. 41) for more details.}

\figure{\includepng{\diagramsDir/npa/layeredModel}{70%}}{A schematic of the Layered model for TCP/IP networks.}{layeredModel}

\notes{The traditional OSI Reference model contains seven layers which reflect in a network how communication occurs at different layers using different protocols. By way of reviewing the TCP model we introduce a layered representation of the TCP/IP model which underlies the internet. As we mentioned above TCP/IP was introduced in 1974 as a standard which interconnects between networks. This is achieved through the Internet Protocol. The TCP/IP reference model is much more compact and will serve as a useful reminder.}

\notes{* **{Application~Layer}** This layer represents the interface to the user and consists of applications which are commonly used by users. As well as the examples in the diagram packetised voice communications, electronic news, HTTP and its secure variants etc.
* **{The~Transport~}** Layer The layer above the internet layer is known as the transport layer and contains two protocols. The Transmission Control Protocol (TCP) allows applications to communicate in a lossless manner, *i.e.*any packets which are dropped are retransmitted. It also implements flow control in an effort to prevent network congestion and reorders arrivals at the destination. The User Datagram Protocol (UDP) is an unreliable protocol for applications which wish to provide their own sequencing and flow control (e.g. voice transmission or video).
* **{The~Internet~}** Layer The key to the success of TCP/IP is the Internet Protocol. Its objective is to allow the interfacing of different networks by allowing hosts to place packets on any network and enabling them to travel to any other network.}

\notes{\section{Communication Media}}

\notes{Circuit switching networks may share a communication line but this is done through multiplexing where a fixed proportion of the communication channel is dedicated to the session. The multiplexing may be time division multiplexing or frequency division multiplexing. The former splits the communication channel into time slots and allocates each to a different session, the latter uses different portions of the frequency bandwidth for each channel. Both are not 100% efficient (time multiplexing requires a small amount of time for switching to occur, and frequency division multiplexing requires a small `buffer' band of frequencies between each session. Packet switching networks dedicate communication bandwidth to each channel as required. In a simple `first in, first out' (FIFO) system, packets arrive and, if the queue is empty, they are transmitted. Otherwise they are stored and await their turn for transmission. Thus there are two delays: a queueing delay and a transmission delay. The queueing delay is variable, whilst the transmission delay will be fixed and given by the packet length multiplied by the transmission rate of the channel.
\footnote{Also known as `first come, first served' (FCFS).}
Radio transmission is a communication medium which dates back to Marconi. Transmission may occur across several bandwidths. Traditionally radio broadcast occurs through frequency division multiplexing. Radio communication involves taking turns to communicate over the channel (half-duplex). The most basic wireless packet networks (*e.g.*ALOHA) used one channel to broadcast their packets over. Delays may occur due to collisions. A collision is when two systems both attempt to communicate on the same channel at the same time. Both packets are then lost and such losses need to be detected.
Similar principles occur for *e.g.* thinwire Ethernet, in this case the communication medium is a coaxial cable.}

\notes{\section{The Road Ahead}}

\notes{* **{Probability~Review}** Review of probability theory.
* **{Simple~Queueing~}** models Simple models of queues based on probability theory. Little's formula, $M/M/1$ queue, $M/M/\infty$, $M/M/m$, $M/M/m/m$ and $M/G/1$.
* **{Simulation}** Simulation of queueing systems.}

\notes{## Examples}

\notes{1. As a simple example let's consider a database (perhaps MySQL). We are constructing it from existing parts. We have two CPU/motherboard systems and two separate disk systems, their expected characteristics are shown in Table\  \ref{cap:SQLserver}. Which should we match with which? Are we better off building one faster system and one slower system? Or should we build two systems that have a similar performance?
  
  % empty table}

\speakernotes{\begin{itemize}
      \item You are starting an e-commerce company.
      \item You have a tight budget.
      \item You have:
      \begin{itemize}
      \end{itemize}
      \item Which should you combine to make your two servers?
    \end{itemize}

$$
\begin{aligned}
        \item two disk systems (1 & 2).
        \item two CPU systems (A & B).
\end{aligned}
$$

}

\notes{\answer{
* You should match A with 2 and B with 1.
* This avoids bottlenecks:
* Disk 1 would wait for CPU A to process about 50% of the time.
* CPU B would wait for disk 2 to access about 50% of the time.
}{0}}

\endif
