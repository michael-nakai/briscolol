from simulation import main_pipeline
import AI

a = AI.big_spender()
b = AI.big_spender()
c = AI.little_coward()
d = AI.little_coward()
e = AI.randy_random()
f = AI.randy_random()
g = AI.little_opportunist()
h = AI.little_opportunist()
y = [a, c, e, g] # Add your new AI here
z = [b, d, f, h]
main_pipeline(y, z, 1000)