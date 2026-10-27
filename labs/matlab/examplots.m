figure, plotErlangLoss([1:80:80 80:40:200 200:20:600], 300:1:500)
printlatex('z:\tex\projects\lectures\COM6130\erlangBexamCurves2.eepic', ...
	   8, 'top', 'n')
figure, plotErlangDelay(300:10:600, 300:1:500)
printlatex('z:\tex\projects\lectures\COM6130\erlangCexamCurves2.eepic', 8, 'top', 'n')
