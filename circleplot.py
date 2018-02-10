import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

P1 = np.array(((1,2),(2,4)))
P2 = np.array(((-2,1),(1,-2)))
P3 = np.array(((1,2),(2,1)))
P4 = np.array(((3,1),(0,2)))


def circleplot(P, n=100):
    XY = np.empty((2,2,n))
    with sns.color_palette("hls", n):
        plt.figure(figsize=(6,6))
        circle = plt.Circle((0,0), 1, color='b', fill=False)
        plt.gca().add_artist(circle)
        phi = np.linspace(0, 2*np.pi, n)
        XY[0] = np.c_[np.cos(phi), np.sin(phi)].T
        XY[1] = P.dot(XY[0])
        for i in range(XY.shape[2]):
            plt.plot(XY[:,0,i], XY[:,1,i])
            #plt.arrow(XY[0,0,i], XY[0,1,i], XY[1,0,i]-XY[0,0,i], XY[1,1,i]-XY[0,1,i], head_width=0.05, head_length=0.1)
        plt.xlim((-4,4))
        plt.ylim((-4,4))
        plt.show()
   
print(np.linalg.eig(P4))
circleplot(P4)

circleplot(P1, n=200)

circleplot(P2)


circleplot(P3)

