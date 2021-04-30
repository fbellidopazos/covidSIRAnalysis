import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate,optimize
from processingModule import getCities
import tikzplotlib

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

'''
Obtenemos todas las funciones de cada par <beta,gamma>
'''
for i in vals:
    beta,gamma = i
    results.append(integrate.odeint(SIR, (S0, I0, R0), t, args=(beta, gamma)))


'''
Empezamos a sacar gráficas
1. Comparamos all versus all
    1.1 Susceptibles
    1.2 Infectados
    1.3 Recuperados
2. Graficas SIR individuales
3. Acumuladas
'''
# 
figs=[]
figs.append(plt.figure("Susceptibles"))
for i in range(0,len(vals)):
    plt.title("Susceptibles")
    plt.plot(t,results[i][:,0])
plt.legend([f"$\\beta$={i[0]}\n$\\gamma$={i[1]}" for i in vals],prop={'size': 10})
tikzplotlib.clean_figure()
tikzplotlib.save(f"latex/Comparison_1to1-Susceptibles.tex")


figs.append(plt.figure("Infectados"))
for i in range(0,len(vals)):
    plt.title("Infectados")
    plt.plot(t,results[i][:,1])
plt.legend([f"$\\beta$={i[0]}\n$\\gamma$={i[1]}" for i in vals],prop={'size': 10})
tikzplotlib.clean_figure()
tikzplotlib.save(f"latex/Comparison_1to1-Infectados.tex")


figs.append(plt.figure("Recuperados"))
for i in range(0,len(vals)):
    plt.title("Recuperados")
    plt.plot(t,results[i][:,2])
plt.legend([f"$\\beta$={i[0]}\n$\\gamma$={i[1]}" for i in vals],prop={'size': 10})
tikzplotlib.clean_figure()
tikzplotlib.save(f"latex/Comparison_1to1-Recuperados.tex")



for i in range(0,len(vals)):
    figs.append(plt.figure(f"Comparison {i}"))
    plt.plot(t, results[i][:,0])
    plt.plot(t, results[i][:,1])
    plt.plot(t, results[i][:,2])
    plt.title(f"$\\beta$: {round(vals[i][0],3)}\t$\\gamma$: {round(vals[i][1],3)}\t $R_0$: {round(vals[i][0]/vals[i][1],3)}")
    plt.legend(["Susceptibles","Infectados","Recuperados"],prop={'size': 10})
    tikzplotlib.clean_figure()
    tikzplotlib.save(f"latex/Individual_all3[{i}].tex")
    
def acumula(arr):
    res = []
    i = 0
    for j in arr:
        if i == 0:
            res.append(i)
        else:
            res.append(res[i-1]+j)
        i-=-1 
    return res

figs.append(plt.figure("Acumulados"))
for i in range(0,len(vals)):
    plt.plot(t,acumula(results[i][:,1]))
plt.title("Infectados acumulados")
plt.legend([f"$\\beta$={i[0]}\n$\\gamma$={i[1]}" for i in vals],prop={'size': 10})
tikzplotlib.clean_figure()
tikzplotlib.save(f"latex/Comparison_Infected-Acumulative.tex")




plt.show()



'''
Firmado por : Angel Escudero,Beatriz Sara Alonso ,Alejandro TIburon y Fernando Bellido
                                                             ..
                                  ,,,                         MM .M
                              ,!MMMMMMM!,                     MM MM  ,.
      ., .M                .MMMMMMMMMMMMMMMM.,          *MM.  MM MM .M*
    . M: M;  M          .MMMMMMMMMMMMMMMMMMMMMM,          *MM,:M M*!M*
   ;M MM M: .M        .MMMMMMMMMMMMMMMMMMMMMMMMMM,         *MM*...*M
    M;MM;M :MM      .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.       .MMMMMMMM
    *M;M*M MM      MMMMMM  MMMMMMMMMMMMMMMMM  MMMMMM.    ,,M.M.*MMM*
     MM*MMMM      MMMMMM @@ MMMMMMMMMMMMMMM @@ MMMMMMM.*M**MMMM;MM*
    MM., ,MM     MMMMMMMM  MMMMMMMMMMMMMMMMM  MMMMMMMMM      *.MMM
    *MM;MMMMMMMM.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.      *MMM
     **.*MMM*  .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM       MMMM
      MMC      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.      *MMMM
     .MM      :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM**MMM       MMMMM
     MMM      :M  *MMMMMMMMMMMMM.MMMMM.MMMMMMMMMM*.MM  MM:M.    *MMMMM
    .MMM   ...:M: :M.*MMMMMMMMMMMMMMMMMMMMMMMMM*.M**   MM:MMMMMMMMMMMM*
   AMMM..MMMMM:M.    :M.*MMMMMMMMMMMMMMMMMMMM*.MM*     MM************
   MMMMMMMMMMM:MM     *M*.M*MMMMMMMMMMMMMM*.MC*M*     .MM
    **********:MM.       *MM!M.*M-M-M-M*M.*MM*        MMM
               MMM.            *MMMM!MMMM*            .MM
                MMM.             ***   **            .MM*
                 MMM.                               MMM*
                  MMMM            ,.J.JJJJ.       .MMM*
                   MMMM.       *JJJJJJJ*JJJM   CMMMMM
                     MMMMM.    *JJJJJJJJ*JJJ .MMMMM*
                       MMMMMMMM.*  *JJJJJ*JJMMMMM*
                         *MMMMMMMMM*JJJJJ JJJJJ*
                            **MMMMMMJJJJJJJJJJ*
                                    *JJJJJJJJ*		


'''