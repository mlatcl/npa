\ifndef{packetSwitchingAndInternet}
\define{packetSwitchingAndInternet}

\section{Computer Networks}

\notes{Circuit-switched networks were designed for a telephone conversation between two people. They were the first worldwide communication networks. By the early 1960s a different kind of network was needed. In circuit switching a permanently open line connects the correspondents and a fixed bandwidth is reserved for them. If they do not use it, nobody else can.}

\notes{In *packet switching* (store-and-forward) the bandwidth is shared. What a user sends — voice over IP, or a file by FTP — is split into packets that are routed across the network. If a required line is busy the packet waits in a queue. The ideas were developed independently by **Paul Baran** (1926–2011) at RAND and **Donald Davies** (1924–2000) at the National Physical Laboratory. **Leonard Kleinrock**’s 1962 thesis, later a book [@Kleinrock:communication64], gave the mathematical theory that underpins these networks.}

\slides{* Circuit switching reserves a channel; unused bandwidth is wasted
* Packet switching: store and forward, queues at busy links
* Baran, Davies, Kleinrock (1962)}

\subsection{ARPANET}

\notes{ARPA funded a network that implemented these ideas. In 1969 it connected four nodes: UCLA, the Stanford Research Institute, UC Santa Barbara, and the University of Utah. By 1975 the network covered most major US universities (61 nodes) and a node at University College London.}

\figure{\includepng{\diagramsDir/npa/1975_net_map}{80%}}{The ARPANET in 1975, image courtesy of the Computer History Museum. PDP machines are DEC minicomputers; 360 and 370 are IBM mainframes. Note the transatlantic link to London and the Pacific link to Hawaii. There are 61 nodes.}{arpa-net-1975}

\notes{ARPANET was restricted to non-commercial use and funded by ARPA and NSF until 1990. Telnet and FTP appeared in 1971. The transmission control protocol (TCP), developed in the mid-1970s by **Vinton Cerf** (1943–) and **Robert Kahn** (1938–) [@Cerf:packet74], allowed interconnection between networks and thereby the internet.}

\slides{* ARPANET, 1969: four nodes; 1975: 61 nodes including UCL
* TCP (Cerf and Kahn, mid-1970s): internetworking}

\subsection{The Internet}

\notes{By 1977 Cerf and Kahn could send messages across the Packet Radio net, SATNET, and ARPANET. At a similar time **Robert Metcalfe** (1946–) was developing Ethernet at Xerox PARC. Ethernet was inspired by the ALOHA networks at the University of Hawaii: machines shared a radio channel, collisions had to be detected, and packets retransmitted. Ethernet used a cable rather than a radio frequency. Cheap Ethernet and cheap computers produced an explosion in the number of networks on the internet.}

\notes{When ARPANET was shut down in 1990 it had grown to 300,000 hosts. It evolved into NSFNet, the backbone of the internet. In 1991 the internet opened to commercial traffic. Combined with HTML and URLs, invented by **Tim Berners-Lee** (1955–), that is the foundation of the modern internet.}

\slides{* Ethernet (Metcalfe), inspired by ALOHA
* 1990: ARPANET closed at ~300,000 hosts
* 1991: commercial traffic; Berners-Lee, HTML and URLs}

\endif
