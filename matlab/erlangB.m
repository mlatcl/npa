function B = erlangB(a, m)

% ERLANGB Erlang B formula in terms of offered load and number of servers.

% NPA

for i = 1:length(a)
  for j = 1:length(m)
    kVec = [0:m(j)-1];
    partOne = m(j).*log(a(i)) - gammaln(m(j)+1);
    logTerms = [kVec.*(log(a(i)))-gammaln(kVec+1)-partOne, 0];
    B(i, j) = 1/sum(exp(logTerms));
  end
end
