from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
import math

#Inicializamos la ventana
main = Tk()

def infoAdicional():
	messagebox.showinfo("Programa para Modelo de Kuz Ram", "Bajo derechos de autor")

def infoLicencia():
	messagebox.showwarning("Licencia","Licencia activada hasta el 2020.")

def salirApp(): 
	valor = messagebox.askokcancel("Salir","¿Estas seguro que quieres salir?")
	if valor==True:
		main.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar","No es posible cerrar el documento")
	if valor==False:
		main.destroy()

def abreArchivo():
	archivo=filedialog.askopenfilename(title="Abrir",initialdir="/")#,filetypes=("Todos los ficheros"))
	print(archivo)


# CREACION DE INTERFACE

barraMenu=Menu(main)
main.config(menu=barraMenu)

archivoMenu=Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir",command=abreArchivo)
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirApp)

edicionMenu=Menu(barraMenu,tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")

herramientaMenu=Menu(barraMenu,tearoff=0)
herramientaMenu.add_command(label="Reemplazar")

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia",command=infoLicencia)
ayudaMenu.add_command(label="Acerca de...",command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramienta", menu=herramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


main.title("Predicción del tamaño de roca fragmentada")
main.geometry("1100x580")
main.resizable(0,0)

#Frame Izquierda
frame=Frame()
frame.pack(side="left",fill="y",padx=10,pady=10)
frame.config(width=550,height=750)
frame.config(bd=2)
frame.config(relief="sunken")
frame.config(bg="lightgray")
frame.config(cursor="question_arrow")

#Frame Derecha
frameLista=Frame()
frameLista.pack(side="left",fill="y",padx=10,pady=10)
frameLista.config(width=150,height=750)
frameLista.config(bd=2)
frameLista.config(bg="lightgray")
frameLista.config(relief="sunken")
frameLista.config(cursor="question_arrow")

#Frame Derecha
framePlot=Frame()
framePlot.pack(side="left",fill="y",padx=10,pady=10)
framePlot.config(width=550)
framePlot.config(bd=2)
framePlot.config(bg="lightgray")
framePlot.config(relief="sunken")
framePlot.config(cursor="question_arrow")


def roca():

	#Agregar componentes al frame

	#Roca
	contenedorRoca=LabelFrame(frame,text="Roca", fg="red",font=("Arial",10,"bold"))
	contenedorRoca.grid(row=0,column=0,sticky="w",padx=10,pady=5)
	contenedorRoca.config(bd=3,relief="ridge",bg="lightgray")
	#label de la roca
	labelRoca=Label(contenedorRoca,text="Factor de Roca:",bg="lightgray")
	labelRoca.grid(row=0,column=0,padx=5,pady=5,sticky="e")

	#Caja de la roca
	txtFactorRoca=Entry(contenedorRoca,justify="center",fg="red",width="15",textvariable=fr)
	txtFactorRoca.grid(row=0,column=1,padx=5,pady=5)

def malla():
	#Contenedor de Malla
	contenedorMalla=LabelFrame(frame,text="Malla", fg="red",font=("Arial",10,"bold"))
	contenedorMalla.grid(row=1,column=0,sticky="w",padx=10,pady=5)
	contenedorMalla.config(bd=3,relief="ridge",bg="lightgray")

	#Label de Burden
	labelBurden=Label(contenedorMalla,text="Burden [m]:",bg="lightgray")
	labelBurden.grid(row=0,column=0,padx=5,pady=5,sticky="e")

	#Caja de la Burden
	txtBurden=Entry(contenedorMalla,justify="center",fg="red",width="12",textvariable=b)
	txtBurden.grid(row=0,column=1,padx=5,pady=5)

	#Label de Espaciamiento
	labelEspaciamiento=Label(contenedorMalla,text="Espaciamiento [m]:",bg="lightgray")
	labelEspaciamiento.grid(row=1,column=0,padx=5,pady=5,sticky="e")

	#Caja de la Espaciamiento
	txtEspaciamiento=Entry(contenedorMalla,justify="center",fg="red",width="12",textvariable=s)
	txtEspaciamiento.grid(row=1,column=1,padx=5,pady=5)

	#Label de Altura
	labelAltura=Label(contenedorMalla,text="Altura [m]:",bg="lightgray")
	labelAltura.grid(row=2,column=0,padx=5,pady=5,sticky="e")

	#Caja de la Altura
	txtAltura=Entry(contenedorMalla,justify="center",fg="red",width="12",textvariable=h)
	txtAltura.grid(row=2,column=1,padx=5,pady=5)

	#Label de Tipo
	labelTipo=Label(contenedorMalla,text="Tipo:",bg="lightgray")
	labelTipo.grid(row=3,column=0,padx=5,pady=5,sticky="e")

	#Caja de Tipo
	Tipo=ttk.Combobox(contenedorMalla,width="9",textvariable=pater)
	Tipo.grid(row=3,column=1)
	Tipo['values']=("Triangular","Cuadrada")

	#Label de Desviacion
	labelDesviacion=Label(contenedorMalla,text="Desviación [m]:",bg="lightgray")
	labelDesviacion.grid(row=4,column=0,padx=5,pady=5,sticky="e")

	#Caja de la Desviacion
	txtDesviacion=Entry(contenedorMalla,justify="center",fg="red",width="12",textvariable=desv)
	txtDesviacion.grid(row=4,column=1,padx=5,pady=5)

def taladro():
	#Contenedor de Taladro
	contenedorTaladro=LabelFrame(frame,text="Taladro", fg="red",font=("Arial",10,"bold"))
	contenedorTaladro.grid(row=2,column=0,sticky="w",padx=10,pady=5)
	contenedorTaladro.config(bd=3,relief="ridge",bg="lightgray")

	#Label de Taco
	labelTaco=Label(contenedorTaladro,text="Taco [m]:",bg="lightgray")
	labelTaco.grid(row=0,column=0,padx=5,pady=5,sticky="e")

	#Caja de la Taco
	txtTaco=Entry(contenedorTaladro,justify="center",fg="red",width="8",textvariable=taco)
	txtTaco.grid(row=0,column=1,padx=5,pady=5)

	#Label de Diámetro
	labelDiametro=Label(contenedorTaladro,text="Diámetro [mm]:",bg="lightgray")
	labelDiametro.grid(row=1,column=0,padx=5,pady=5,sticky="e")

	#Caja de la Diámetro
	txtDiametro=Entry(contenedorTaladro,justify="center",fg="red",width="8",textvariable=d)
	txtDiametro.grid(row=1,column=1,padx=5,pady=5)

	#Label de Sobreperforación
	labelSobreperforacion=Label(contenedorTaladro,text="Sobreperforación [mm]:",bg="lightgray")
	labelSobreperforacion.grid(row=2,column=0,padx=5,pady=5,sticky="e")

	#Caja de Sobreperforación
	txtSobreperforacion=Entry(contenedorTaladro,justify="center",fg="red",width="8",textvariable=sp)
	txtSobreperforacion.grid(row=2,column=1,padx=5,pady=5)

def Explosivo():
	#Contenedor de Explosivo
	contenedorExplosivo=LabelFrame(frame,text="Explosivo", fg="red",font=("Arial",10,"bold"))
	contenedorExplosivo.grid(row=3,column=0,sticky="w",padx=10,pady=5)
	contenedorExplosivo.config(bd=3,relief="ridge",bg="lightgray")

	#Label de Densidad
	labelDensidad=Label(contenedorExplosivo,text="Densidad [g/CC]:",bg="lightgray")
	labelDensidad.grid(row=0,column=0,padx=5,pady=5,sticky="e")

	#Caja de la Densidad
	txtDensidad=Entry(contenedorExplosivo,justify="center",fg="red",width="14",textvariable=de)
	txtDensidad.grid(row=0,column=1,padx=5,pady=5)

	#Label de Energía
	labelEnergia=Label(contenedorExplosivo,text="Energía [Kj/kg]:",bg="lightgray")
	labelEnergia.grid(row=1,column=0,padx=5,pady=5,sticky="e")

	#Caja de la Energía
	txtEnergia=Entry(contenedorExplosivo,justify="center",fg="red",width="14",textvariable=e)
	txtEnergia.grid(row=1,column=1,padx=5,pady=5)

	#Label de RWS
	labelRWS=Label(contenedorExplosivo,text="RWS [%]:",bg="lightgray")
	labelRWS.grid(row=2,column=0,padx=5,pady=5,sticky="e")

	#Caja de RWS
	txtRWS=Entry(contenedorExplosivo,justify="center",fg="red",width="14",textvariable=rws)
	txtRWS.grid(row=2,column=1,padx=5,pady=5)

# DECLARACION DE VARIBALES
fr= DoubleVar() # Factor de Roca
b= DoubleVar() # Burden [m]
s= DoubleVar() # Espaciamiento [m]
h= DoubleVar() # Altura [m]
pater= StringVar() # Patron de Perforación
desv= DoubleVar() # Desviación de Perforación [m]
taco= DoubleVar() # Taco [m]
d = DoubleVar() # Diametro [mm]
sp = DoubleVar() # Sobreperforacion [m]
de= DoubleVar() # Densidad de explosivo [g/cc]
e= DoubleVar() # energia del explosivo [kcal/kg]
rws = DoubleVar() # potencia relativa del explosivo [%]

# Variables de Entrada
paso=5
p=np.arange(5,95+paso,paso)/100 # Lista , (Valor inicial , final , paso)
listaX=[];listaY=[]

# Variables de Resultados
Xprom=0;n=0;x80=0;result=[];listaCurva=[];

fig,ax= plt.subplots()
#grafica= fig.add_subplot(221)

ax.set_xlabel('Tamaño de Fragmento [cm]',color="r")
ax.set_ylabel('Porcentaje Pasante [%]',color="r")
ax.grid(True,color="lightgray")
plt.title("Curva Granulométrica")

canvas = FigureCanvasTkAgg(fig,framePlot)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, framePlot)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side="top",fill="both",expand=True)

def calcular():
	global listaCurva,listaX,listaY,p,result,ax,Xprom,n,canvas

	valor = messagebox.askyesno(message="¿Desea Agregar Gráfica?", title="Agregar")

	if valor==True:

		# OBTENER VALORES --------------------------------------------------------------
		_fr = fr.get()
		_b = b.get()
		_s = s.get()
		_h = h.get()
		_pater= pater.get()

		# Asignar valor al pater si es que es triangular o cuadrada (1 / 1.1)
		if _pater == "Triangular":
			_pater= 1.1
		else:
			_pater=1

		_t = taco.get()
		_d = d.get()/1000
		_sp = sp.get()
		_de = de.get()*1000
		_e = e.get()
		_rws = rws.get()
		Desv = desv.get()

		#------------------------------------------------------------------------------------------------
		
		# Longitud de carga
		lc = _h+_sp-_t
		print("Longitud de carga: ", lc)
		# Kg de explosivo
		w = _de * lc * math.pi*_d**2/4
		print("cantidad de êxplosivo [kg]: ", w)

		# CALCULAR TAMAÑO PROMEDIO ----------------------------------------------------------------------

		tamañomedio(_b,_s,_h,_fr,w,_rws)

		# CALCULAR INDICE DE UNIFORMIDAD ----------------------------------------------------------------
		indice(_b,_d*1000,_s,Desv,lc,_h,_pater)

		# CALCULAR CURVA --------------------------------------------------------------------------------
		curva(Xprom,p,n,result,listaCurva)
		
		xmin= round(min(listaCurva))
		xmax= round(max(listaCurva))
		pasox=5
		pasoy=10
		listaX= np.arange(xmin,xmax+pasox,pasox)
		listaY= np.arange(0,100+pasoy,pasoy)

		ax.set_xticks(listaX)
		ax.set_yticks(listaY)

		#Actualizar Gráfica
		canvas.draw()

def tamañomedio(b,s,h,a,w,rws):
	global Xprom
	V= b*s*h
	print("V",V)
	try:
		Xprom = a*((V/w)**0.8)*(w**(1/6))*(115/rws)**(19/30) # cm
		print("xprom: ", Xprom)
		print("RWS", rws)
	except Exception as e:
		print(e)
	
def indice(b,d,s,Desv,lc,h,pater):
	global n
	try:
		n = (2.2-14*(b/d))*(((1+s/b)/2)**0.5)*(1-Desv/b)*(lc/h)*pater
		print("n",n)
	except Exception as m:
		print(m)

def curva(Xprom,p,n,result,listaCurva):
	global ax
	valores = Xprom*(-(np.log(1-p)/0.693))**(1/n) # --> X80
	# agrego nuevos valores
	result.append({"res":valores,"n":n})
	agregarCurva()
	#x80= Xprom*(-(np.log(1-0.8)/0.693))**(1/n)

def agregarCurva():
	global result,listavalores,ax,canvas
	# LIMPIO grafica
	ax.clear()
	print(len(result))
	listavalores.delete(0,len(result))

	## PROPIEDADES DE LA GRAFICA
	ax.set_xlabel('Tamaño de Fragmento [cm]',color="r")
	ax.set_ylabel('Porcentaje Pasante [%]',color="r")
	ax.grid(True,color="lightgray")
	plt.title("Curva Granulométrica")

	i=0

	for res in result:
		#x80 = Xprom*(-(np.log(1-0.8)/0.693))**(1/n)
		titulo = "n :"+str(round(res['n'],3))#+" X80:"+str(round(x80,2))
		ax.plot(res['res'],p*100,label=titulo)
		listavalores.insert(i,titulo)	
		for x in res['res']:
			listaCurva.append(x)
		i=i+1

	ax.legend(loc="lower right",shadow=True,fontsize=9)
	canvas.draw()

def limpiar():
	global ax,canvas
	valor = messagebox.askyesno(message="¿Desea Limpiar Gráfica?", title="Limpiar")
	if valor==True:
		ax.clear()
		## PROPIEDADES DE LA GRAFICA
		ax.set_xlabel('Tamaño de Fragmento [cm]',color="r")
		ax.set_ylabel('Porcentaje Pasante [%]',color="r")
		ax.grid(True,color="lightgray")
		plt.title("Curva Granulométrica")
		canvas.draw()

def eliminar():
	global listavalores
	if len(listavalores.curselection())!=0:
		val = listavalores.curselection()[0]
		result.pop(val)
		agregarCurva()

def ejemplo1():
	fr.set(8.421)
	b.set(10)
	s.set(10)
	h.set(15)
	pater.set("cuadrada")
	desv.set(0.58)
	taco.set(7)
	d.set(250.8)
	sp.set(1.5)
	de.set(1.20)
	rws.set(125)


botonEliminar = Button(frameLista,text="-- Eliminar --",command=eliminar)
botonEliminar.grid(row=0,column=0,sticky="w",padx=10,pady=5)
listavalores = Listbox(frameLista,height=25)
listavalores.grid(row=1,column=0,sticky="w",padx=10,pady=5)
######....................

botonCalcular = Button(main,text="-- CALCULAR --", command=calcular).place(x=25,y=535)

botonLimpiar = Button(main,text="-- LIMPIAR --", command=limpiar).place(x=150,y=535)

## LLAMAR FUNCIONES
Explosivo()
taladro()
malla()
roca()
ejemplo1()

# CREAR FIGURA DEL MATPLOTLIB

#fig= Figure(figsize=(5.5, 5), dpi=100)



main.mainloop()