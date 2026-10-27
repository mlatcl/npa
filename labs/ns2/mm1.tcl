# lambda is the arrival rate for the packets
set lamda 1

# 1/mu is the mean of the packet lengths in kilobytes
set mu 2
set m 2000

# create a new ns2 simulator object
set ns [new Simulator]

# this variable will be used for storing the maximum queue length
set maximum_queue $m

# set up some random number generators
set rng [new RNG]

# set an initial seed
$rng seed 0

# This distribution is for the arrival times
set expoT [new RandomVariable/Exponential]
$expoT set avg_ [expr 1.0/$lamda]

# This distribution gives packet lengths in bits
set expoX [new RandomVariable/Exponential]
$expoX set avg_ [expr 1024.0/$mu]

# Set up the network structure
# two nodes
set node1 [$ns node]
set node2 [$ns node]

# A link between the nodes
set link [$ns simplex-link $node1 $node2 8Kb 0ms DropTail]
set qu  [$link queue]
$qu set limit_ $m

set src [new Agent/UDP]
$src set packetSize_ 20000000
$ns attach-agent $node1 $src
set qmon [$ns monitor-queue $node1 $node2 ""]

set sink [new Agent/Null]
$ns attach-agent $node2 $sink

$ns connect $src $sink


proc finish {} {
    global ns
    $ns flush-trace
    exit 0
}

proc sendpacket {} {
    global ns src expoT expoX
    
    # get the current simulation time
    set simTime [$ns now]
    
    # draw the packet length from an exponential
    set Xbytes [expr ([$expoX value])]
    
    # send a packet of length Xbytes from node1
    $src send [expr $Xbytes]    

    # draw an interarrival from an exponential
    set T [$expoT value] 
        
    # compute the time of the next arrival
    set nextSend [expr $simTime + $T]  
    
    # at the next arrival time run this function again
    $ns at $nextSend "sendpacket"
     
}

proc outputdata {} {
    # This function outputs the values every second
    global ns qmon
    
    # run the function again after a second
    set simTime [$ns now]
    $ns at [expr $simTime + 1] "outputdata"
    
    # extract the queue length
    set NQ [$qmon set pkts_]
    puts $NQ;
}

$ns at 0.00001 "sendpacket"
$ns at 0.00001 "outputdata"
$ns at 100000.0 "finish"
$ns run
