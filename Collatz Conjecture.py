from matplotlib import pyplot as plt
ver=int(input('Enter number:\t'))
j=[ver]
i=[0]
st=0
while ver>1:
    if ver%2==0:
        ver=ver/2
        st+=1
        j.append(ver)
    else:
        ver=3*ver+1
        st+=1
        j.append(ver)
print('Stopping number is',st)
for x in range(0,st):
    i.append(x)
plt.plot(i,j)
plt.xlabel('Iteration Number')
plt.ylabel('Output')
plt.grid(True)
plt.show()