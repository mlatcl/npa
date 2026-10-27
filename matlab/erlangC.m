function C = erlangC(a, m)

% ERLANGC Erlang C formula in terms of offered load and number of servers.

% NPA

for i = 1:length(a)
  for j = 1:length(m)
    if a<m
      kVec = [0:m(j)-1];
      partOne = m(j).*log(a(i)) - gammaln(m(j)+1) - log(1-a(i)./m(j));
      logTerms = [kVec.*(log(a(i)))-gammaln(kVec+1)-partOne, 0];
      C(i, j) = 1/sum(exp(logTerms));
    elseif a==m
      C(i, j) = 1;
    else
      C(i, j) = NaN;
    end
  end
end
