function callbackhandler(call)

global stop
global rateUp
global rateDown
global deathRateLabel
global birthRateLabel
global display
global kStore
global counter

switch call
 case 'spacedHistogram'
  figure(4)
  maxK = max(kStore(1:5000:counter));
  bin = hist(kStore(1:5000:counter), maxK+1);
  rho = rateUp/rateDown;
  for i = 0:maxK
    pK(i+1) = rho^i*(1-rho);
  end
%  patch1 = bar(0:maxK, pK); 
%  set(patch1, 'CData', [NaN])
%  hold on
  bar((0:maxK)', [bin/sum(bin); pK]');
%  hold off
  
 case 'histogram'
  figure(3)
  maxK = max(kStore(1:counter));
  bin = hist(kStore(1:counter), maxK+1);
  rho = rateUp/rateDown;
  for i = 0:maxK
    pK(i+1) = rho^i*(1-rho);
  end
%  patch1 = bar(0:maxK, pK); 
%  set(patch1, 'CData', [NaN])
%  hold on
  bar((0:maxK)', [bin/sum(bin); pK]');
%  hold off
 case 'startStop'
  stop = ~stop;
  if stop
    set(gcbo, 'String', 'Start')
  else
    set(gcbo, 'String', 'Stop')     
    simulateQueue;
  end
 
 case 'Display'
  display = ~display;
  if display
    set(gcbo, 'String', 'Display On');
  else
    set(gcbo, 'String', 'Display Off');
  end
 case 'deathChange'
  rateDown = get(gcbo, 'Value')
  set(deathRateLabel, 'String', ['Death Rate: ' num2str(rateDown)])
  rateChange
  
 case 'birthChange'
  rateUp = get(gcbo, 'value')
  set(birthRateLabel, 'String', ['Birth Rate: ' num2str(rateUp)])
  rateChange
end


function rateChange

global rateUp
global rateDown
global averageLine
global stdLine1
global stdLine2
global delayLabel

if rateDown > rateUp
  rho = rateUp/rateDown;
  
  meanVal = rho/(1-rho);
  set(averageLine, 'YData', [meanVal meanVal], 'Visible', 'on')
  averageWait = 1/(rateDown - rateUp);
  set(delayLabel, 'String', ['Expected Delay: ' num2str(averageWait)])
  stdVal = sqrt(rho)/(1-rho);
  %set(stdLine1, 'YData', [meanVal+stdVal meanVal+stdVal], 'Visible', 'on');
  %set(stdLine2, 'YData', [meanVal-stdVal meanVal-stdVal], 'Visible', 'on');
  
  set(gca, 'YLim', [0 meanVal+stdVal])
else
  set(delayLabel, 'String', ['Expected Delay: '])
  set(averageLine, 'Visible', 'off')
  set(stdLine1, 'Visible', 'off')
  set(stdLine2, 'Visible', 'off')
end