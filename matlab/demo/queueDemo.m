close all
global display
global stop
global rateUp
global rateDown
global deathRateLabel
global birthRateLabel
global delayLabel
global queuePatch
global averageLine
global stdLine1
global stdLine2
global plotLine
global averageLine2
global kStore
global counter

display = 1;
figure

plotLine = line([0 0], [0 0]);
set(plotLine, 'EraseMode', 'xor');
averageLine2 = line([0 0], [0 0], 'color', [1 0 0], 'linestyle', '--');
xlabel('time')
ylabel('Number in queue, k')
stop = 1;

rateUp = 1;
rateDown = 1;

colordef white
figure
height = 15;
axHand = axes('position', [0.45 0.32 0.1 0.6050])
runButton = uicontrol('style', 'pushbutton', 'String', 'Start', 'units', 'normalized', 'position', ...
		      [0.7 0.05 0.2 0.1], 'Callback', 'callbackhandler(''startStop'')')
histButton = uicontrol('style', 'pushbutton', 'String', 'Histogram', 'units', 'normalized', 'position', ...
		      [0.7 0.35 0.2 0.1], 'Callback', 'callbackhandler(''histogram'')')
histSpacedButton = uicontrol('style', 'pushbutton', 'String', 'Spaced Hist', 'units', 'normalized', 'position', ...
		      [0.7 0.65 0.2 0.1], 'Callback', 'callbackhandler(''spacedHistogram'')')
displayButton = uicontrol('style', 'pushbutton', 'String', 'Display', 'units', 'normalized', 'position', ...
		      [0.7 0.2 0.2 0.1], 'Callback', 'callbackhandler(''Display'')')
deathRateLabel = uicontrol('style', 'text', 'String', 'Death Rate:', 'units', 'normalized', 'position', ...
		      [0.1 0.05 0.58 0.05])
deathSlide = uicontrol('style', 'slider', ...
		       'String', 'Rate In', ...
		       'units', 'normalized', ...
		       'position', [0.1 0.1 0.58 0.05], ...
		       'Max', 2, 'Min', 0.01, ...
		       'SliderStep', [0.01 1], ...
		       'Callback', 'callbackhandler(''deathChange'')')

birthRateLabel = uicontrol('style', 'text', ...
			   'String', 'Birth Rate:', ...
			   'units', 'normalized', ...
			   'position',[0.1 0.15 0.58 0.05])

birthSlide = uicontrol('style', 'slider', ...
		       'String', 'Rate In', ...
		       'units', 'normalized', ...
		       'position', [0.1 0.2 0.58 0.05], ...
		       'Max', 2, 'Min', 0.01, ...
		       'SliderStep', [0.01 1], ...
		       'Callback', 'callbackhandler(''birthChange'')')

delayLabel = uicontrol('style', 'text', 'String', 'Expected Delay: ', 'units', 'normalized', 'position', ...
		      [0.1 0.35 0.2 0.1])


set(birthSlide, 'value', rateUp);
set(deathSlide, 'value', rateDown);

axis([0 3 0 height])
queuePatch = patch([1 1 2 2], [0 0 0 0], 'r')
set(queuePatch, 'erasemode', 'xor')

averageLine = line([0 3], [7 7], 'color', [1 0 0], 'linestyle', '--');
stdLine1 = line([0 3], [7 7], 'color', [0 0 1]);
stdLine2 = line([0 3], [7 7], 'color', [0 0 1]);
set(averageLine, 'Visible', 'off')
set(stdLine1, 'Visible', 'off')
set(stdLine2, 'Visible', 'off')





