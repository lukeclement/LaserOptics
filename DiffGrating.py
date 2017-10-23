import numpy as n

NdSigma=0.001
ZSigma=0.001

Nd=n.array([0.050,0.101,0.151,0.204,0.259,0.042,0.088,0.142,0.219,0.062,0.153])
Z=n.array([0.9100,0.910,0.910,0.910,0.910,0.253,0.253,0.253,0.253,0.174,0.174])
#              ^^Added just so numbers would align
#Finding sinTheta
sinTheta=Nd/n.sqrt(Z**2+Nd**2)
print("Sine Theta:")
print(sinTheta)
#Finding uncertainty
sigma=sinTheta*n.sqrt((NdSigma/Nd)**2+(ZSigma/Z)**2)
print("Sigma Sine Theta:")
print(sigma)
