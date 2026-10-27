randn('seed', 1e4)
numData = 100;
xmin = 1;
xmax = 6;
ymin = 1;
ymax = 4;
fontName = 'helvetica';
fontSize = 20;
X = gsamp([3.5 2.5], [1 -.5; -.5 1]*.7, 100);
plot(X(:, 1), X(:, 2), 'rx', 'markersize', 10, 'linewidth', 2)
set(gca, 'xtick', [1 2 3 4 5 6]);
set(gca, 'ytick', [1 2 3 4 5 6]);
set(gca, 'xlim', [xmin-.6 xmax+.6])
set(gca, 'ylim', [ymin-.6 ymax+.6])
txtX = xlabel('X');
txtY= ylabel('Y');
set([txtX txtY], 'fontName', fontName, 'fontsize', fontSize);
set(gca, 'fontName', fontName, 'fontsize', fontSize);
for val = ymin-.5:1:ymax+.5
  line([xmin-0.5 xmax+0.5], [val val]);
end
for val = xmin-.5:1:xmax+.5
  line([val val], [ymin-.5 ymax+.5]);
end
linewidth = 3;
yval = 2;
xval = 5;
line([xmin-0.55 xmax+0.55; xmax+.55 xmax+0.55; xmax+0.55 xmin-.55; xmin-.55 xmin-.55], [yval+.55 yval+.55; yval+.55 yval-.55; yval-.55 yval-.55; yval-.55 yval+.55], 'linewidth', linewidth, 'linestyle', ':', 'color', [1 0 0])
line([xval-0.55 xval+0.55; xval+.55 xval+0.55; xval+0.55 xval-.55; xval-.55 xval-.55], [ymax+.55 ymax+.55; ymax+.55 ymin-.55; ymin-.55 ymin-.55; ymin-.55 ymax+.55], 'linewidth', linewidth, 'linestyle', '--', 'color', [0 0 1])
yval = 4;
xval = 3;
line([xval-0.55 xval+0.55; xval+.55 xval+0.55; xval+0.55 xval-.55; xval-.55 xval-.55], [yval+.55 yval+.55; yval+.55 yval-.55; yval-.55 yval-.55; yval-.55 yval+.55], 'linewidth', linewidth, 'linestyle', '-', 'color', [0 1 0])
box off