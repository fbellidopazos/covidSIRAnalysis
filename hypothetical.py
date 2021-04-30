import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate,optimize
from processingModule import getCities
import tikzplotlib
#plt.style.use("bmh")
plt.style.use("seaborn")
def SIR(y,t,beta,gamma):
    S,I,R = y
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return dS,dI,dR


N=1000
I0 = 1
S0 = N-I0
R0 = 0
vals = [(0.667,0.167),(0.5,0.167),(0.333,0.167)]
results = []


t = np.linspace(0.0,90,90)


for i in vals:
    beta,gamma = i
    results.append(integrate.odeint(SIR, (S0, I0, R0), t, args=(beta, gamma)))


'''
fig, ax = plt.subplots(3)

for i in range(0,len(vals)):
    ax[0].set_title("Susceptibles")
    ax[0].plot(t,results[i][:,0]/N)


    ax[1].set_title("Infectados")   
    ax[1].plot(t,results[i][:,1]/N)

    ax[2].set_title("Recuperados")
    ax[2].plot(t,results[i][:,2]/N)


# %%

ax[0].legend(vals)
ax[1].legend(vals)
ax[2].legend(vals)

tikzplotlib.clean_figure()
tikzplotlib.save("latex/Comparison_1to1.tex")

#plt.show()
'''
figs=[]
figs.append(plt.figure("Susceptibles"))
for i in range(0,len(vals)):
    plt.title("Susceptibles")
    plt.plot(t,results[i][:,0])
plt.legend([f"$\\beta$={i[0]}\n$\\gamma$={i[1]}" for i in vals],prop={'size': 10})
tikzplotlib.clean_figure()
tikzplotlib.save(f"latex/Comparison_1to1-Susceptibles.tex")
#plt.show()

figs.append(plt.figure("Infectados"))
for i in range(0,len(vals)):
    plt.title("Infectados")
    plt.plot(t,results[i][:,1])
plt.legend([f"$\\beta$={i[0]}\n$\\gamma$={i[1]}" for i in vals],prop={'size': 10})
tikzplotlib.clean_figure()
tikzplotlib.save(f"latex/Comparison_1to1-Infectados.tex")
#plt.show()

figs.append(plt.figure("Recuperados"))
for i in range(0,len(vals)):
    plt.title("Recuperados")
    plt.plot(t,results[i][:,2])
plt.legend([f"$\\beta$={i[0]}\n$\\gamma$={i[1]}" for i in vals],prop={'size': 10})
tikzplotlib.clean_figure()
tikzplotlib.save(f"latex/Comparison_1to1-Recuperados.tex")
#plt.show()


for i in range(0,len(vals)):
    figs.append(plt.figure(f"Comparison {i}"))
    plt.plot(t, results[i][:,0])
    plt.plot(t, results[i][:,1])
    plt.plot(t, results[i][:,2])
    plt.title(f"$\\beta$: {round(vals[i][0],3)}\t$\\gamma$: {round(vals[i][1],3)}\t $R_0$: {round(vals[i][0]/vals[i][1],3)}")
    plt.legend(["Susceptibles","Infectados","Recuperados"],prop={'size': 10})
    tikzplotlib.clean_figure()
    tikzplotlib.save(f"latex/Individual_all3[{i}].tex")
    


figs.append(plt.figure("Acumulados"))
for i in range(0,len(vals)):
    plt.plot(t,np.cumsum(results[i][:,1]))
plt.title("Infectados acumulados")
plt.legend([f"$\\beta$={i[0]}\n$\\gamma$={i[1]}" for i in vals],prop={'size': 10})
tikzplotlib.clean_figure()
tikzplotlib.save(f"latex/Comparison_Infected-Acumulative.tex")
#plt.show()

plt.show()