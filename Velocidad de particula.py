from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
#from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import math

#Inicializamos la ventana
main = Tk()
main.title("Predicción de Velocidad de Partícula")
main.geometry("800x580")
main.resizable(0,0)

# CREACION DE INTERFACE
#Frame Izquierda
frame=Frame()
frame.pack(side="left",fill="y",padx=10,pady=10)
frame.config(width=550,height=750)
frame.config(bd=2)
frame.config(relief="sunken")
frame.config(bg="lightgray")
frame.config(cursor="question_arrow")

#Frame Derecha
framePlot=Frame()
framePlot.pack(side="left",fill="y",padx=10,pady=10)
framePlot.config(width=150,height=750)
framePlot.config(bd=2)
framePlot.config(bg="lightgray")
framePlot.config(relief="sunken")
framePlot.config(cursor="question_arrow")

# DECLARACION DE VARIBALES
d= DoubleVar() # Diametro [mm]
de= DoubleVar() # Densidad del Explosivo [g/cc]
taco= DoubleVar() # Taco [m]
lc= DoubleVar() # Longitud de Carga [m]
xmin= DoubleVar() # Valor minimo de X [m]
xmax= DoubleVar() # Valor maximo de X [m]
ymin= DoubleVar() # Valor minimo de Y [m]
ymax= DoubleVar() # Valor maximo [m]
paso= DoubleVar() # Paso del Dominio
k= DoubleVar()
alpha = DoubleVar()

def taladro():
	global d,de,taco,lc,k,alpha

	#Agregar componentes al frame

	#Taladro
	contenedorTaladro=LabelFrame(frame,text="Taladro", fg="red",font=("Arial",10,"bold"))
	contenedorTaladro.grid(row=0,column=0,sticky="w",padx=10,pady=5)
	contenedorTaladro.config(bd=3,relief="ridge",bg="lightgray")

	#label del Diametro
	labelDiametro=Label(contenedorTaladro,text="Diámetro [mm]:",bg="lightgray")
	labelDiametro.grid(row=0,column=0,padx=5,pady=5,sticky="e")

	#Caja de Diametro
	txtDiametro=Entry(contenedorTaladro,justify="center",fg="red",width="15",textvariable=d)
	txtDiametro.grid(row=0,column=1,padx=5,pady=5)

	#label del Densidad
	labelDensidad=Label(contenedorTaladro,text="Densidad [g/cc]:",bg="lightgray")
	labelDensidad.grid(row=1,column=0,padx=5,pady=5,sticky="e")

	#Caja de Densidad
	txtDensidad=Entry(contenedorTaladro,justify="center",fg="red",width="15",textvariable=de)
	txtDensidad.grid(row=1,column=1,padx=5,pady=5)

	#label del Taco
	labelTaco=Label(contenedorTaladro,text="Taco [m]:",bg="lightgray")
	labelTaco.grid(row=2,column=0,padx=5,pady=5,sticky="e")

	#Caja de Taco
	txtTaco=Entry(contenedorTaladro,justify="center",fg="red",width="15",textvariable=taco)
	txtTaco.grid(row=2,column=1,padx=5,pady=5)

	#label del LC
	labellc=Label(contenedorTaladro,text="Long. Carga [m]:",bg="lightgray")
	labellc.grid(row=3,column=0,padx=5,pady=5,sticky="e")

	#Caja de LC
	txtlc=Entry(contenedorTaladro,justify="center",fg="red",width="15",textvariable=lc)
	txtlc.grid(row=3,column=1,padx=5,pady=5)

	#label del K
	labelk=Label(contenedorTaladro,text="K:",bg="lightgray")
	labelk.grid(row=4,column=0,padx=5,pady=5,sticky="e")

	#Caja de K
	txtK=Entry(contenedorTaladro,justify="center",fg="red",width="15",textvariable=k)
	txtK.grid(row=4,column=1,padx=5,pady=5)

	#label del alpha
	labelalpha=Label(contenedorTaladro,text="Alpha:",bg="lightgray")
	labelalpha.grid(row=5,column=0,padx=5,pady=5,sticky="e")

	#Caja de alpha
	txtalpha=Entry(contenedorTaladro,justify="center",fg="red",width="15",textvariable=alpha)
	txtalpha.grid(row=5,column=1,padx=5,pady=5)

def configuracion():
	#Contenedor de Malla
	contenedorSetup=LabelFrame(frame,text="Malla", fg="red",font=("Arial",10,"bold"))
	contenedorSetup.grid(row=1,column=0,sticky="w",padx=10,pady=5)
	contenedorSetup.config(bd=3,relief="ridge",bg="lightgray")

	#Label de xmin
	labelxmin=Label(contenedorSetup,text="X Minimo [m]:",bg="lightgray")
	labelxmin.grid(row=0,column=0,padx=5,pady=5,sticky="e")

	#Caja de la xmin
	txtxmin=Entry(contenedorSetup,justify="center",fg="red",width="12",textvariable=xmin)
	txtxmin.grid(row=0,column=1,padx=5,pady=5)

	#Label de xmax
	labelxmax=Label(contenedorSetup,text="X Máximo [m]:",bg="lightgray")
	labelxmax.grid(row=1,column=0,padx=5,pady=5,sticky="e")

	#Caja de xmax
	txtxmax=Entry(contenedorSetup,justify="center",fg="red",width="12",textvariable=xmax)
	txtxmax.grid(row=1,column=1,padx=5,pady=5)

	#Label de ymin
	labelymin=Label(contenedorSetup,text="Y Minimo [m]:",bg="lightgray")
	labelymin.grid(row=2,column=0,padx=5,pady=5,sticky="e")

	#Caja de la xmin
	txtymin=Entry(contenedorSetup,justify="center",fg="red",width="12",textvariable=ymin)
	txtymin.grid(row=2,column=1,padx=5,pady=5)

	#Label de xmax
	labelymax=Label(contenedorSetup,text="Y Máximo [m]:",bg="lightgray")
	labelymax.grid(row=3,column=0,padx=5,pady=5,sticky="e")

	#Caja de xmax
	txtymax=Entry(contenedorSetup,justify="center",fg="red",width="12",textvariable=ymax)
	txtymax.grid(row=3,column=1,padx=5,pady=5)

	#Label de paso
	labelpaso=Label(contenedorSetup,text="Paso [m]:",bg="lightgray")
	labelpaso.grid(row=4,column=0,padx=5,pady=5,sticky="e")

	#Caja de paso
	txtpaso=Entry(contenedorSetup,justify="center",fg="red",width="12",textvariable=paso)
	txtpaso.grid(row=4,column=1,padx=5,pady=5)

#Inicializar Ejemplo 1
def ejemplo1():
	d.set(200)
	de.set(1.1)
	taco.set(6)
	lc.set(9)
	xmin.set(-10)
	xmax.set(10)
	ymin.set(0)
	ymax.set(20)
	paso.set(0.1)
	k.set(700)
	alpha.set(0.7)

def limpiar():
	global ax,canvas
	valor = messagebox.askyesno(message="¿Desea Limpiar Gráfica?", title="Limpiar")
	if valor==True:
		ax.clear()
		## PROPIEDADES DE LA GRAFICA
		ax.set_xlabel('Distancia X[m]',color="r")
		ax.set_ylabel('Distancia Y [m]',color="r")
		#ax.grid(True,color="lightgray")
		plt.title("Campo de Velocidades de Partícula")
		canvas.draw()

def getDatos():
	_d= d.get(); _de=de.get();_taco= taco.get();_lc= lc.get();_k= k.get();_alpha=alpha.get()
	_xmin= xmin.get();_xmax=xmax.get();_ymin= ymin.get();_ymax= ymax.get();_paso= paso.get()
	calcular(_d,_de,_taco,_lc,_k,_alpha,_xmin,_xmax,_ymin,_ymax,_paso)

u=[] # ticks
contador=0
listavpp=[]
def calcular(d,de,t,lc,k,alpha,xmin,xmax,ymin,ymax,paso):
	global ax,fig,plt,canvas,contador,u
	ax.clear()
	try:
		fig.delaxes(fig.axes[1])
	except:
		print("No encontro Axes")

	ax.set_xlabel('Distancia X[m]',color="r")
	ax.set_ylabel('Distancia Y [m]',color="r")
	plt.gca().invert_yaxis()
	#ax.grid(True,color="lightgray") 
	plt.title("Campo de Velocidades de Partícula")

	#Dominios
	x=np.arange(xmin,xmax+paso,paso)
	y=np.arange(ymin,ymax+paso,paso)

	X,Y = np.meshgrid(x,y)

	#Parametros Iniciales
	xc=10
	H=lc
	z1= t # Z1
	z2= z1+H
	yp= (z1+z2)/2
	print(yp)
	l=de*((d/1000)**2)*1000/4 # Carga Lineal
	v = (k*((l/np.abs(X))**alpha)*(np.arctan((z2-Y)/np.abs(X))+np.arctan((Y-z1)/np.abs(X)))**alpha)/1000

	# vpp en paredes del taladro
	d= d/1000
	_v=(k*((l/np.abs(0.5*d))**alpha)*(np.arctan((z2-yp)/np.abs(0.5*d))+np.arctan((yp-z1)/np.abs(0.5*d)))**alpha)/1000
	
	if contador==0:
		u=[0.01*_v,0.05*_v,0.2*_v,0.5*_v,0.7*_v,0.9*_v,_v]
		cf = ax.contourf(X,Y,v,u,cmap="jet",alpha=0.5,extend='both')
		ax_bar = fig.add_axes([0.87,0.15,0.02,0.70], anchor='SW')
		cb= fig.colorbar(cf,cax=ax_bar,ticks=u)
	else:
		cf = ax.contourf(X,Y,v,u,cmap="jet",alpha=0.5,extend='both')
		ax_bar = fig.add_axes([0.87,0.15,0.02,0.70], anchor='SW')
		cb= fig.colorbar(cf,cax=ax_bar,ticks=u)
	
	contador=contador+1
	canvas.draw()

######....................

botonCalcular = Button(main,text="-- CALCULAR --", command=getDatos).place(x=25,y=535)

botonLimpiar = Button(main,text="-- LIMPIAR --", command=limpiar).place(x=150,y=535)

## LLAMAR FUNCIONES
taladro()
configuracion()

# CREAR FIGURA DEL MATPLOTLIB
fig,ax= plt.subplots()
###################
ax.set_xlabel('Distancia X[m]',color="r")
ax.set_ylabel('Distancia Y [m]',color="r")
#ax.grid(True,color="lightgray")
plt.title("Campo de Velocidades de Partícula")
plt.gca().invert_yaxis()

fig.subplots_adjust(bottom=0.12)
fig.subplots_adjust(top=0.90)
fig.subplots_adjust(left=0.13)
fig.subplots_adjust(right=0.85)

canvas = FigureCanvasTkAgg(fig,framePlot)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, framePlot)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side="top",fill="both",expand=True)

# LLAMAR AL EJEMPLO 1
ejemplo1()

main.mainloop()