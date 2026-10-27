function B = plotErlangLoss(serverRange, trafficRange)

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
    %k = 0:m;
    %components = (a.^k)./factorial(k);
    %invp0 = sum(components);
    invB = 0;
    for k = 0:(m-1); 
      invB = invB + prod([(a.^(k-m)) (k+1):m]);
    end
    invB = invB + 1;
%    p0 = 1/invp0;
%    B(i, j) = (a^m)/factorial(m)*p0;
    B(i, j) = 1/invB;
  end
  
end
handle = plot(trafficRange, B);
set(gca, 'yscale', 'log')
set(handle, 'linewidth', 2)
grid on
levelChange = 2.5/length(serverRange);
axis([min(trafficRange) max(trafficRange) 10^-3 10^0])
xspan = max(trafficRange) - min(trafficRange);
xShift = xspan/(2*length(serverRange));
level = -0.2;
for i = 1:length(serverRange)
  for j = 1:length(trafficRange);
    if B(i, j) > 10^level
      text(trafficRange(j)-xShift, B(i, j), num2str(serverRange(i)))
      level = level - levelChange;
      break
    end
  end
end
xlabel('offered trafic, $a$')
ylabel('blocking probability')
hold off
