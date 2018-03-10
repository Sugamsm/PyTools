
# PyTools
Python Library for general discrete math calculations.

The library includes functions for calculating Probabilities and Entropies.

Functions and their Uses:

1. Entropy:
Func - calculate_entropy(x, opt)
Based on the formula H(X) = either -p(x)log(p(x)) and -sum(p(x)log(p(x))) or -sum(p(x, y)log(p(x, y))) -sum(p(x, y)log(p(x, y)))
The argument x represents either a single or joint probability of a variable or a one-dimentional array containing multiple probabilites
of a particular variable or joint probabilities.
For a single probability(single variable or joint) entropy calculation arg opt should have string value as 'single'
and for arg x to be an array opt should be 'array'

2. Conditional Entropy 
Func - conditional_entropy(x, y, opt)
The conditional Entropy H(X|Y) or H(Y|X) gives the uncertainity that remains about X when Y is known or vice versa.
The library provides two choices of formulas for the calculation.

(a) H(X|Y) = sum[p(Y)P(X|Y)log(P(X|Y)]
H(X|Y) = sum[p(X)P(Y|X)log(P(Y|X)]
using Conditional Probability
Here, the argument x represent a single probability or an array of prababilities P(X|Y) or P(Y|X). (Conditional Probability)
y represents a single probability or an array of prababilities of P(X) or P(Y)
Here, for this choice opt has 2 options:
opt = 'single_condtional' if passing single values of probabilities
opt = 'array_conditional' if passing array of probabilities

(b) H(X|Y) = sum[p(X,Y)log(p(Y)/p(X,Y)] 
H(X|Y) = sum[p(X,Y)log(p(X)/p(X,Y)]
using Joint Probability
Here, the argument x represent a single probability or an array of prababilities P(X, Y). (Joint Probability)
y represents a single probability or an array of prababilities of P(X) or P(Y)
Here, for this choice opt has 2 options:
opt = 'single_joint' if passing single values of probabilities
opt = 'array_joint' if passing array of probabilities

3. Relative Entropy
D (P || Q) = sum ( P(X=a) log (p(X=a) / P (Y = a))
Func - relative_entropy(p, q, opt)
here p and q are the two variables  P(X) and P(Y)
p and q arguments can be either single probability value or an array of probabilities of X and Y
opt can be correspondingly 'single' or 'array'
