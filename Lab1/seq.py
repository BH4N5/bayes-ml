"""
INITIAL APPROACH

Let X be a random variable describing a coin toss i.e. X has values in {0,1} and assume X ~
Bern(p) where 0 < p < 1. Let us consider the following process involving an unfair coin described by
X:
    -> toss the coin and memorize the result in var x 
    -> repeat: 
        -> toss the coin and get some result y in {0,1}
            -> if y == 1 flip x so that x = ~x
            -> else do nothing

Let P(n) be the probability of getting x = 1 after n such repetitions. Then we simply have

    P(n) = | p, n=0
           | p * (1 - P(n-1)) + (1-p) * P(n-1) = p + (1-2p) * P(n-1) , n > 0

This is a linear recurrence relation with constant coeffs which may readily be put into a closed form

    P(n) = 0.5 * (1 - (1-2p)^(n+1))

It is trivial to see that the condition 0 < p < 1 implies |1-2p| < 1 so that we have lim P(n) = 0.5.

Described construction enables us to "simulate" a fair coin (i.e. coin described by X ~ Bern(0.5))
having an unfair coin (and a lot of time for tossing).  
"""

import numpy as np


def unfair_coin():
    return np.random.choice([0, 1], p=[0.1, 0.9])


def make_coin_fair():
    trials = 10**2

    x = unfair_coin()
    for _ in range(trials):
        if unfair_coin() == 1:
            x = 1 - x

    return x
