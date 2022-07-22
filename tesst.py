import matplotlib.pyplot as plt
from numpy import*

x = linspace(0,100,1000)
y = sqrt((100*(1 - 0.01*x**2)**2 + 0.02*x**2)/((1 - x**2)**2 + 0.1*x**2))

plt.figure(figsize = (14, 8))
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()

plt.subplot(2, 2, 2)
plt.semilogx(x,y)
plt.title("Semilogx")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()

plt.subplot(2,2,3)
plt.semilogy(x,y)
plt.title('Semilogy')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2,2,4)
plt.loglog(x,y)
plt.title('Loglog')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.tight_layout()
plt.show()