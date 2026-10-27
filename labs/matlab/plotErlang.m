function C = plotErlang(serverRange, trafficRange, CorB)

% PLOTERLANGDELAY Produce Erlang C or B curves.

% NPA 

% a is offered traffic
midTraffic = trafficRange(floor(end/2));
i = 0;
midTrafficRange = linspace(min(trafficRange), max(trafficRange), max(serverRange));
for m = serverRange
  labelled = 0;
  j = 0;
  i = i + 1;
  for a = trafficRange
    j = j + 1;
    switch CorB
     case 'C'
      C(i, j) = erlangC(a, m); 
     case 'B'
      C(i, j) = erlangB(a, m);
    end
  end  
end
handle = plot(trafficRange, C);
set(gca, 'yscale', 'log')
set(handle, 'linewidth', 2)
grid on
levelChange = 2.5/length(serverRange);
axis([min(trafficRange) max(trafficRange) 10^-3 10^0])
xspan = max(trafficRange) - min(trafficRange);
xShift = xspan/(4*length(serverRange));
level = -0.2;
plotEvery = 1;
for i = 1:plotEvery:length(serverRange)
  for j = 1:length(trafficRange);
    if C(i, j) > 10^level
      a=text(trafficRange(j)-plotEvery*xShift, C(i, j), ...
             num2str(serverRange(i)));
      set(a, 'fontsize', 8);
      set(a, 'horizontalalignment', 'right')
      level = level - plotEvery*levelChange;
      break
    end
  end
end
xlabel('offered trafic, a')
switch CorB
 case 'C'
   ylabel('probability of waiting')
 case 'B'
   ylabel('probability of blocking')
end
hold off
