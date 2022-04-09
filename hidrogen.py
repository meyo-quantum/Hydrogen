#HIDROGEN

import time 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cmath


t0=time.time()


N = 40
ither = 200
k1 = 1
r = 1

A = np.zeros((N,N,N),dtype='complex_')
T = np.zeros((N,N,N))
I = np.zeros((N,N,N))
AB = np.zeros((N,N,N))
AN = np.zeros((N,N,N))

#početni uslovi
A[0,:,:] = 0.00
A[N-1,:,:] = 0
A[:,0,:] = 0.00
A[:,N-1,:] = 0.00
A[:,:,0] = 1
A[:,:,N-1] = 1

Niter = range(ither)

for ither in Niter:
    for i in range(1,N-1):
        for j in range(1,N-1):
            for k in range(1,N-1):
                #A[i,j,l] = (A[i,j,l+1]+(A[i+1,j,l]+A[i-1,j,l]+A[i,j+1,l]+A[i,j-1,l]))/(1+4-k1/np.sqrt(float(i*i+j*j)))
                #A[i,j,l] = (N*A[i,j,l+1]+N*N*(A[i+1,j,l]+A[i-1,j,l]+A[i,j+1,l]+A[i,j-1,l]))/(N+4*N*N-k1)    
                A[i,j,k] = ((A[i+1,j,k]+A[i-1,j,k]+A[i,j+1,k]+A[i,j-1,k])*N*N+1/r+complex(0,N)*A[i,j,k-1])/(complex(0,N)+4*N*N)



#pravim realnu matricu
'''for i in range(N-1):
    for j in range(N-1):
        for k in range(N-1):
            b = A[i,j,k]
            T[i,j,k] = float(b.real)'''
            
            
#pravim imaginarnu matricu
'''for i in range(N-1):
    for j in range(N-1):
        for k in range(N-1):
            u = A[i,j,k]
            I[i,j,k] = float(u.imag)'''
  
#za realnu komponentu valne funkcije
#def some_data(i):   # function returns a 2D data array
#    return AB[:,:,i]

def some_data_Im(i):   # function returns a 2D data array
    return I[:,:,i]

x = range(N)
y = range(N)
#t = range(N)

X,Y = np.meshgrid(x,y)
v = T[:,:,:]
#print(v)

#fig = plt.figure(figsize=(8,8),dpi=200)
#plt.contour(X,Y,v)
t1=time.time()
print(t1-t0)


#matrica apsolutnih vrijednosti
for i in range(N-1):
    for j in range(N-1):
        for k in range(N-1):
            b = A[i,j,k]
            AB[i,j,k] = abs(b)
            
 
#normalizacija matrice
AN = AB/np.max(AB)
           
           
#za realnu komponentu valne funkcije
def some_data(i):   # function returns a 2D data array
    return AN[:,:,i]

print(AN)

mxt = np.amax(AN)
print('Maximum je: ', mxt)
#animacija apsolutne vrijednosti
fig = plt.figure()
ax = plt.axes(xlim=(0, 40), ylim=(0, 40), xlabel='x', ylabel='y')

cvals = np.linspace(0,1,30)      # set contour values 
cont = plt.contourf(x, y, some_data(0), cvals)    # first image on screen
plt.colorbar()

# animation function
def animate(i):
    global cont
    z = some_data(i)
    #for c in cont.collections:
    #    c.remove()  # removes only the contours, leaves the rest intact
    cont = plt.contourf(x, y, z, cvals)
    plt.title('t = %i:  %.2f' % (i,z[7,7]))
    return cont

anim1 = animation.FuncAnimation(fig, animate, frames=N-1, repeat=True)






'''
#---------------------------------------------------------------------
#prvi
#---------------------------------------------------------------------
fig = plt.figure()
ax = plt.axes(xlim=(0, N), ylim=(0, N), xlabel='x', ylabel='y')

cvals = np.linspace(0,1.4,N+1)      # set contour values 
cont = plt.contourf(x, y, some_data(0), cvals)    # first image on screen
plt.colorbar()

# animation function
def animate(i):
    global cont
    z = some_data(i)
    for c in cont.collections:
        c.remove()  # removes only the contours, leaves the rest intact
    cont = plt.contourf(x, y, z, cvals)
    plt.title('t = %i:  %.2f' % (i,z[5,5]))
    return cont

anim1 = animation.FuncAnimation(fig, animate, frames=N-1, repeat=True)
#-----------------------------------------------------------------
#drugi -----------------------------------------------------------
#-----------------------------------------------------------------
fig_Im = plt.figure()
ax = plt.axes(xlim=(0, N), ylim=(0, N), xlabel='x', ylabel='y')

cvals = np.linspace(0,1.4,N+1)      # set contour values 
cont = plt.contourf(x, y, some_data_Im(0), cvals)    # first image on screen
plt.colorbar()

# animation function
def animate_im(i):
    global cont
    z = some_data_Im(i)
    for c in cont.collections:
        c.remove()  # removes only the contours, leaves the rest intact
    cont = plt.contourf(x, y, z, cvals)
    plt.title('t = %i:  %.2f' % (i,z[5,5]))
    return cont

anim2 = animation.FuncAnimation(fig_Im, animate_im, frames=N-1, repeat=False)
anim1 = animation.FuncAnimation(fig, animate, frames=N-1, repeat=True)
plt.show(anim2,anim1)'''







'''def norm(l):
    return sum(sum(T[:,:,l])/(N*N))

def update(H):
    for i in range(N):
        H[:,:,i]=H[:,:,i]/norm(i)
    return H'''
        


            









