import sys
sys.path.append("pip")

from lorenz.py import * 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d as axes
from matplotlib.backends.backend_pdf import PdfPages

L1 = Lorenz([-1,1,0])
u1 = L1.solve(50,0.01)
L2 = Lorenz([-1.001,1.001,.001])
u2 = L2.solve(50,0.01)

with PdfPages("vlinder.pdf") as pdf:
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(u1[:,0],u1[:,1],u1[:,2]) 
    ax.plot(u2[:,0],u2[:,1],u2[:,2])
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    
    pdf.savefig()