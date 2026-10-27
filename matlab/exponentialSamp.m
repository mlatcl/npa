function [x] = exponentialSamp(lambda, size)

% EXPONENTIALSAMP Sample from the exponential distribution.

x = rand(size);
x = -log(x)./lambda;
