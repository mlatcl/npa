figure
x = gsamp([3 2], [0.5 0.45; 0.45 0.5], 200);
plot(x(:, 1), x(:, 2), 'rx')
set(gca, 'Ylim', [0.2 3.8])
set(gca, 'Xlim', [0.2 6.8])
axis off
axis ij
for i = 0.5:6.5
line([i i], [0.5 3.5])
end
for i = 0.5:3.5
line([0.5 6.5], [i i])
end
square1 = squarecreate([3 1], 1.2);
square1.selected = 0;
square1 = objectdraw(square1);
set(square1.handle, 'color', [1 0 0])
rect1 = rectCreate
