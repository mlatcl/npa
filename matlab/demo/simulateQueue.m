global display
global stop
global rateUp
global rateDown
global queuePatch
global plotLine
global averageLine2
global kStore
global counter

deltaT = 0.01;
k = 0;
counter = 0;
nIters = 10000000;
kStore = zeros(nIters, 1);
everyN = 100;
numArrivals = 0;
while counter < nIters 
  counter = counter  + 1;
  p = rand(1);
  if p>rateUp*deltaT
    if p > (rateUp+rateDown)*deltaT
      % Do nothing
    else
      if k > 0
	k = k - 1;
	%fprintf('Serving one\n')
      end
    end
  else
    k = k + 1;
    numArrivals = numArrivals+1;
    %fprintf('One arrives\n')
  end
  kStore(counter) = k;
  if ~rem(counter, everyN)
    pause(0.001)
    if display
      set(queuePatch, 'YData', [0 k k 0])
      if counter>100*everyN
	set(plotLine, 'XData', ((counter/everyN-100):counter/everyN)', ...
		      'YData', kStore(counter-100*everyN:everyN:counter))
	meanVals = cumsum(kStore(1:everyN:counter))./((1:counter/everyN)');
	set(averageLine2, 'XData', ((counter/everyN-100):counter/everyN)', ...
			  'YData', meanVals(counter/everyN-100:counter/everyN))
	set(get(plotLine, 'parent'), 'XLim', [counter/everyN-100 counter/everyN], 'YLim', ...
			  [0 max([kStore; 1])+1])
      else
	set(plotLine, 'XData', (1:counter/everyN)', ...
		      'YData', kStore(1:everyN:counter))
	set(averageLine2, 'XData', (1:counter/everyN)', ...
			  'YData', cumsum(kStore(1:everyN:counter))./((1:counter/everyN)'))
	set(get(plotLine, 'parent'), 'XLim', [0 counter/everyN], 'YLim', ...
			  [0 max([kStore])+1])
      end	
      drawnow
    end
  end
  if stop
    fprintf('Stopped: Mean %f after %d seconds and %d arrivals.\n', ...
	    mean(kStore(1:counter)), counter/100, numArrivals)
    break
  end
  if ~rem(counter, 10000) & ~display
    fprintf('Mean %f after %d seconds and %d arrivals.\n', mean(kStore(1:counter)), ...
	    counter/100, numArrivals)
  end
end

  
  

