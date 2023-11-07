import tkinter as tk
import mysql.connector
from tkinter import font
from tkinter import messagebox
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
# Lista de usuarios válidos
usuarios_validos = ["Carlos", "Jessica", "Germaryori", "Kathy", "Pablo"]

# Función para verificar las credenciales de inicio de sesión
def verificar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    
    if usuario in usuarios_validos and contrasena == "contraseña":
        mostrar_interfaz_principal()
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

# Función para mostrar la interfaz principal
def mostrar_interfaz_principal():
    ventana_inicio.destroy()  # Cerrar la ventana de inicio de sesión

    # Aquí debes crear y mostrar la interfaz principal de tu aplicación

def conectar():
    try:
# Conectar a la base de datos MySQL
        conexion = mysql.connector.connect(user="root", password="root",
                             host="localhost",
                            database='inventario',
                            port='3306')
        cursor = conexion.cursor()
        return conexion, cursor
        print("MySQL connection was successful!")
    except mysql.connector.Error as error:
         print("Failed to connect to MySQL:", error)
         return None,None


# Crear la ventana de inicio de sesión
ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión")
ventana_inicio.geometry("400x300")

# Etiqueta y entrada para el usuario
label_usuario = tk.Label(ventana_inicio, text="Usuario:")
label_usuario.pack(pady=10)
entry_usuario = tk.Entry(ventana_inicio)
entry_usuario.pack(pady=5)

# Etiqueta y entrada para la contraseña
label_contrasena = tk.Label(ventana_inicio, text="Contraseña:")
label_contrasena.pack(pady=10)
entry_contrasena = tk.Entry(ventana_inicio, show="*")
entry_contrasena.pack(pady=5)

# Botón para iniciar sesión
boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", command=verificar_credenciales)
boton_iniciar_sesion.pack(pady=20)

# Ejecutar la aplicación
ventana_inicio.mainloop()

from PIL import Image, ImageTk
from tkinter import font

def productos():
    volver_button.config(state="normal")
    ventana2.place_forget()
    ventana3.place_forget()
    ventana4.place_forget()
    ventana5.place_forget()
    ventana6.place_forget()
    ventana1.place(x=320,y=380)
def guardarproductos():
    conexion, cursor= conectar()
    if conexion and cursor:
        print("producto guardado")
        idproducto= int(entry_idproducto1.get())
        Producto= entry_Producto.get()
        Descripcion = entry_Descripcion.get()
        Stock_inicial = int(entry_Stock_inicial.get())
        Precio = float(entry_Precio.get())
        Lugar_origen = entry_Lugar_origen.get()
        Fecha_registro = entry_Fecha_registro.get()
        cursor.execute("INSERT INTO producto (idproducto, Producto, Descripcion,Cantidad, Precio, Lugar_origen, Fecha_registro) VALUES (%s,%s, %s, %s,%s,%s,%s)", (idproducto, Producto, Descripcion,Stock_inicial, Precio, Lugar_origen, Fecha_registro))
        conexion.commit()
        limpiar()

def compras():   
    volver_button.config(state="normal")
    ventana1.place_forget()
    ventana3.place_forget()
    ventana4.place_forget()
    ventana5.place_forget()
    ventana6.place_forget()
    ventana2.place(x=320,y=380)
def guardar_en_compras():
    conexion, cursor= conectar()
    if conexion and cursor:
        print("una compra")
        idCompras = int(entry_idCompras.get())
        Fecha_compra = entry_Fecha_compra.get()
        idproducto = entry_idproductoC.get() 
        Descripcion = productC_listbox.get(tk.ACTIVE)  # Obtener la descripción seleccionada
        CantidadC = int(entry_CantidadC.get())

        cursor.execute("INSERT INTO compras (idcompras, Fecha_compra, idproducto, Descripcion, Cantidad) VALUES (%s, %s, %s, %s, %s)",
                    (idCompras, Fecha_compra, idproducto, Descripcion, CantidadC))
        '''
        # Obtener la cantidad actual del producto seleccionado
        cursor.execute("SELECT Cantidad FROM producto WHERE Producto = %s", (Descripcion,))
        cantidad_actualC = cursor.fetchone()[0]
        
        # Calcular la nueva cantidad (actual + comprada)
        nueva_cantidadC = cantidad_actualC + CantidadC
        
        # Actualizar la cantidad en la tabla de productos
        cursor.execute("UPDATE producto SET Cantidad = %s WHERE Producto = %s", (nueva_cantidadC, Descripcion))
        '''
        
        conexion.commit()
        limpiar()
def actualizar_id(event):
    selected_description = productC_listbox.get(tk.ACTIVE)  # Obtener la descripción seleccionada
    cursor.execute("SELECT idproducto FROM producto WHERE Producto = %s", (selected_description,))
    idproducto = cursor.fetchone()
    if idproducto:
        entry_idproductoC.delete(0, "end")
        entry_idproductoC.insert(0, idproducto[0])

def ventas():  
    volver_button.config(state="normal")
    ventana1.place_forget()
    ventana2.place_forget()
    ventana4.place_forget()
    ventana5.place_forget()
    ventana6.place_forget()
    ventana3.place(x=420,y=280)
def guardar_en_ventas():
    conexion, cursor= conectar()
    if conexion and cursor:
        print("prueba ventas")
        ide = int(entry_idV.get())
        selected_product = productV_listbox.get(tk.ACTIVE)  # Obtener el producto seleccionado del Listbox
        descripcion = entry_descripcionV.get()
        id_Sucursal = int(sucursal_listbox.get(tk.ACTIVE))
        Fecha_venta = entry_Fecha_venta.get()
        Cantidad = int(entry_CantidadV.get())
        cursor.execute("INSERT INTO ventas (id_venta, Producto, Descripcion, id_Sucursal, Fecha_venta, Cantidad) VALUES (%s,%s,%s,%s, %s, %s)",
                    (ide, selected_product, descripcion, id_Sucursal, Fecha_venta, Cantidad))
        # Obtener la cantidad actual del producto seleccionado
        cursor.execute("SELECT Cantidad FROM producto WHERE Producto = %s", (selected_product,))
        cantidad_actual = cursor.fetchone()[0]
        # Calcular la nueva cantidad (actual + comprada)
        nueva_cantidad = cantidad_actual - Cantidad
        # Actualizar la cantidad en la tabla de productos
        cursor.execute("UPDATE producto SET Cantidad = %s WHERE Producto = %s", (nueva_cantidad, selected_product))
        conexion.commit()
        limpiar()
        
def actualizar_descripcion(event):
    selected_description = productV_listbox.get(tk.ACTIVE)  # Obtener la descripción seleccionada
    cursor.execute("SELECT Descripcion FROM producto WHERE Producto = %s", (selected_description,))
    descripcion = cursor.fetchone()
    if descripcion:
        entry_descripcionV.delete(0, "end")
        entry_descripcionV.insert(0, descripcion[0])

def pedidos():
    volver_button.config(state="normal")
    # Ocultar la interfaz de ingreso de datos y las otras interfaces que estuvieran abiertas
    ventana1.place_forget()
    ventana2.place_forget()
    ventana3.place_forget()
    ventana5.place_forget()
    ventana6.place_forget()
    # Mostrar la interfaz de ingreso de datos
    ventana4.place(x=320,y=380)
def guardar_en_pedidos():
    conexion, cursor= conectar()
    if conexion and cursor:
        print("ingreso un pedido")
        idpedido = int(entry_idpedido.get())
        producto = entry_Productos.get()
        Descripcion = entry_descripcion_pedido.get()
        estado = entry_estado.get()
        # Insertar los datos en la base de datos
        cursor.execute("INSERT INTO pedidos (idpedidos, Producto, Descripcion, Estado) VALUES (%s, %s, %s, %s)", (idpedido, producto, Descripcion, estado))
        conexion.commit()
        limpiar()
        
def sucursal():
    volver_button.config(state="normal")
    # Ocultar la interfaz de ingreso de datos y las otras interfaces que estuvieran abiertas
    ventana1.place_forget()
    ventana2.place_forget()
    ventana3.place_forget()
    ventana4.place_forget()
    ventana6.place_forget()
    ventana5.place(x=320,y=380)
def guardar_en_sucursal():
    conexion, cursor= conectar()
    if conexion and cursor:
        print("sucursales")
        idpedido = int(entry_id.get())
        Descripcion = entry_descripcion.get()
        telefono = entry_telefono.get()

        # Insertar los datos en la base de datos
        cursor.execute("INSERT INTO sucursal (id_Sucursal, Nombre_sucursal, Telefono) VALUES (%s, %s, %s)", (idpedido, Descripcion, telefono))
        conexion.commit()
        limpiar()

def proveedores():
    volver_button.config(state="normal")
    # Ocultar la interfaz de ingreso de datos y las otras interfaces que estuvieran abiertas
    ventana1.place_forget()
    ventana2.place_forget()
    ventana3.place_forget()
    ventana4.place_forget()
    ventana5.place_forget()
    ventana6.place(x=350,y=300)

def cargar_pedidos():
    conexion, cursor= conectar()
    if conexion and cursor:
        print("cargar pedidos")
        cursor.execute("SELECT idpedidos FROM pedidos")
        pedidos = [str(row[0]) for row in cursor.fetchall()]
        listbox_idmp.delete(0, tk.END)  # Limpiar el Listbox
        listbox_idmp.insert(0, *pedidos)

def cargar_datos_pedido(event):
    conexion, cursor= conectar()
    if conexion and cursor:
        print("cargar datos pedido")
        selected_indices = listbox_idmp.curselection()
        if selected_indices:
            selected_id = listbox_idmp.get(selected_indices[0])
            cursor.execute("SELECT Producto, Descripcion, Estado FROM pedidos WHERE idpedidos = %s", (selected_id,))
            datos_pedido = cursor.fetchone()
            if datos_pedido:
                entry_prod.delete(0, "end")
                entry_desc.delete(0, "end")
                entry_est.delete(0, "end")
                entry_prod.insert(0, datos_pedido[0])
                entry_desc.insert(0, datos_pedido[1])
                entry_est.insert(0, datos_pedido[2])
        else:
            limpiar()

def modificar_pedido():
    conexion, cursor= conectar()
    if conexion and cursor:
        print("modificar pedido")
        idp = listbox_idmp.get(tk.ACTIVE)  # Obtener el ID seleccionado del Listbox
        prod = entry_prod.get()
        desc = entry_desc.get()
        est = entry_est.get()

        cursor.execute("UPDATE pedidos SET Producto = %s, Descripcion = %s, Estado = %s WHERE idpedidos = %s",
                    (prod, desc, est, idp))
        conexion.commit()
        cargar_pedidos()
        limpiar()

def eliminar_pedido():
    conexion, cursor= conectar()
    if conexion and cursor:
        print("eliminar pedido")
        idp = listbox_idmp.get(tk.ACTIVE)  # Obtener el ID seleccionado del Listbox
        cursor.execute("DELETE FROM pedidos WHERE idpedidos = %s", (idp,))
        conexion.commit()
        cargar_pedidos()
        limpiar()      

def ver_grafico_ventas_mensuales():
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        user="root",
        password="root",
        host="localhost",
        database="inventario"
    )
    curso = conexion.cursor()

    # Consulta SQL para contar las ventas por mes
    query = "SELECT MONTH(Fecha_venta), COUNT(*) FROM ventas GROUP BY MONTH(Fecha_venta)"
    curso.execute(query)

    # Obtener los resultados de la consulta
    resultados = curso.fetchall()

    # Separar los datos en listas para el gráfico
    meses = [resultado[0] for resultado in resultados]
    cantidad_ventas = [resultado[1] for resultado in resultados]

    # Cerrar la conexión a la base de datos
    # Colores para las barras del gráfico
    colores = plt.cm.viridis(np.linspace(0, 1, len(meses)))  # Colormap "Viridis"


    # Crear un gráfico de barras para mostrar las ventas por mes
    plt.bar(meses, cantidad_ventas, color=colores)
    plt.xlabel("Mes")
    plt.ylabel("Cantidad de Ventas")
    plt.title("Ventas Mensuales")
    plt.xticks(range(1, 13))  # Establecer las etiquetas del eje X a los meses del año

    # Mostrar el gráfico
    plt.show()

def volver():  
    volver_button.config(state="normal")
    ventana1.place_forget()
    ventana2.place_forget()
    ventana3.place_forget()
    ventana4.place_forget()
    ventana5.place_forget()
    ventana6.place_forget()

def limpiar():
    print("limpiar")
    entry_idproducto1.delete(0,"end")
    entry_Producto.delete(0,"end")
    entry_Descripcion.delete(0, "end")
    entry_Stock_inicial.delete(0, "end")
    entry_Precio.delete(0, "end")
    entry_Lugar_origen.delete(0, "end")
    entry_Fecha_registro.delete(0, "end")
    #compras
    entry_idCompras.delete(0, "end")
    entry_Fecha_compra.delete(0, "end")
    productC_listbox.selection_clear(0, tk.END)  # Limpiar la selección en el Listbox
    entry_idproductoC.delete(0, "end")
    entry_CantidadC.delete(0, "end")
    #ventas
    entry_idV.delete(0, "end")
    entry_Fecha_venta.delete(0, "end")
    entry_CantidadV.delete(0, "end")
    #pedidos
    entry_idpedido.delete(0, "end")
    entry_Productos.delete(0, "end")
    entry_descripcion_pedido.delete(0, "end")
    entry_estado.delete(0, "end")
    #sucursales
    entry_id.delete(0, "end")
    entry_descripcion.delete(0, "end")
    entry_telefono.delete(0, "end")
    #modificaciones
    listbox_idmp.selection_clear(0, tk.END)
    entry_prod.delete(0, "end")
    entry_desc.delete(0, "end")
    entry_est.delete(0, "end")




#__________________________________________________________________________________________________________________
#  ______________                   .___     .    __________.__.          _.      .               __        ___
# Creación de la ventana, botones, resaltados, fueentes, fondo de pantalla

ventana = tk.Tk()
ventana.title("Proyecto final")
ventana.geometry("1143x768+100+50")

fuente1 =font.Font(family="Times New Roman",size=18, weight="bold")

fuente2 =font.Font(family="Arial",size=14)

imagen_de_fondo = Image.open("C:\\Users\\ricar\\Downloads\\plantillaPROYECTO.png")
imagen_de_fondo = ImageTk.PhotoImage(imagen_de_fondo)
fondo = tk.Label(ventana, image=imagen_de_fondo)
fondo.place(x=0, y=0,relwidth=1, relheight=1)
#resaltados y botones
def resaltar1(event):
    productos_button.config(bg="blue")

def noresaltar1(event):
    productos_button.config(bg="lightblue") 
#para el resaltado 2
def resaltar2(event):
    compras_button.config(bg="green")
def noresaltar2(event):
    compras_button.config(bg="lightgreen") 
#para el resaltado 3
def resaltar3(event):
    ventas_button.config(bg="yellow")
def noresaltar3(event):
    ventas_button.config(bg="lightyellow") 
#para el resaltado 4
def resaltar4(event):
    tareas_button.config(bg="red")
def noresaltar4(event):
    tareas_button.config(bg="pink") 
#para el resaltado 5
def resaltar5(event):
    sucursal_button.config(bg="orange")
def noresaltar5(event):
    sucursal_button.config(bg="lightyellow") 

#para el resaltado 6
def resaltar6(event):
    proveedores_button.config(bg="purple")
def noresaltar6(event):
    proveedores_button.config(bg="pink")

#botones
productos_button = tk.Button(ventana, text="Registrar un producto nuevo", font=fuente1 ,command=productos)
productos_button.bind("<Enter>", resaltar1)
productos_button.bind("<Leave>",noresaltar1)
productos_button.pack()
productos_button.place(x=150,y=130)

compras_button = tk.Button(ventana, text="Archivar la compra realizada", font=fuente1 , command=compras)
compras_button.bind("<Enter>", resaltar2)
compras_button.bind("<Leave>",noresaltar2)
compras_button.pack()
compras_button.place(x=150,y=180)

ventas_button = tk.Button(ventana, text="Documentar la transacción de venta.", font=fuente1 , command=ventas)
ventas_button.bind("<Enter>", resaltar3)
ventas_button.bind("<Leave>",noresaltar3)
ventas_button.pack()
ventas_button.place(x=150,y=230)

tareas_button = tk.Button(ventana, text="Anotar un pedido", font=fuente1 , command=pedidos)
tareas_button.bind("<Enter>", resaltar4)
tareas_button.bind("<Leave>",noresaltar4)
tareas_button.pack()
tareas_button.place(x=150,y=280)

volver_button = tk.Button(ventana, text="Volver o limpiar la pantalla", command=volver)
volver_button.config(state="disabled")
volver_button.place(x=150,y=330)

sucursal_button = tk.Button(ventana, text="Ingresar datos de sucursales", font=fuente1 ,command=sucursal)
sucursal_button.bind("<Enter>", resaltar5)
sucursal_button.bind("<Leave>",noresaltar5)
sucursal_button.pack()
sucursal_button.place(x=640,y=130)

proveedores_button = tk.Button(ventana, text="Modificar o eliminar pedidos", font=fuente1 ,command=proveedores)
proveedores_button.bind("<Enter>", resaltar6)
proveedores_button.bind("<Leave>",noresaltar6)
proveedores_button.pack()
proveedores_button.place(x=640,y=180)


es_button = tk.Button(ventana, text="Estadisticas de ventas", font=fuente2 ,command=ver_grafico_ventas_mensuales)
es_button.pack()
es_button.place(x=640,y=230)
#__________________________________________________________________________________________________________________
#  ______________                   .___     .    __________.__.          _.      .               __        ___

ventana1 = tk.Frame(ventana, width=20, height=30, bg="lightblue")
label_extra=tk.Label(ventana1,text="escribe los datos necesarios ", font=fuente1)
label_extra.grid(row=0, column=0)
label_extr=tk.Label(ventana1,text="para registrar una producto nuevo", font=fuente1)
label_extr.grid(row=0, column=1)
label_idporducto = tk.Label(ventana1, text="Codigo del producto ", font=fuente2)
label_idporducto.grid(row=1, column=0)
entry_idproducto1 = tk.Entry(ventana1)
entry_idproducto1.grid(row=1, column=1)

label_Producto = tk.Label(ventana1, text="Producto", font=fuente2)
label_Producto.grid(row=2, column=0)
entry_Producto = tk.Entry(ventana1)
entry_Producto.grid(row=2, column=1)

label_Descripcion = tk.Label(ventana1, text="Descripcion:", font=fuente2)
label_Descripcion.grid(row=3, column=0)
entry_Descripcion = tk.Entry(ventana1)
entry_Descripcion.grid(row=3, column=1)

label_Stock_inicial = tk.Label(ventana1, text="Stock inicial:", font=fuente2)
label_Stock_inicial.grid(row=4, column=0)
entry_Stock_inicial = tk.Entry(ventana1)
entry_Stock_inicial.grid(row=4, column=1)

label_Precio = tk.Label(ventana1, text="Precio", font=fuente2)
label_Precio.grid(row=5, column=0)
entry_Precio = tk.Entry(ventana1)
entry_Precio.grid(row=5, column=1)

label_Lugar_origen = tk.Label(ventana1, text="Lugar de origen:", font=fuente2)
label_Lugar_origen.grid(row=6, column=0)
entry_Lugar_origen = tk.Entry(ventana1)
entry_Lugar_origen.grid(row=6, column=1)

label_Fecha_registro = tk.Label(ventana1, text="Fecha de registro", font=fuente2)
label_Fecha_registro.grid(row=7, column=0)
entry_Fecha_registro = tk.Entry(ventana1)
entry_Fecha_registro.grid(row=7, column=1)
# Botón para guardar los datos
boton_guardar = tk.Button(ventana1, text="Guardar en la base de datos", command=guardarproductos)
boton_guardar.grid(row=8, column=1)

#__________________________________________________________________________________________________________________
#  ______________                   .___     .    __________.__.          _.      .               __        ___
conexion = mysql.connector.connect(user="root", password="root",
                             host="localhost",
                            database='inventario',
                            port='3306')
cursor = conexion.cursor()

ventana2 = tk.Frame(ventana, width=20, height=30, bg="lightgreen")
label_extra=tk.Label(ventana2,text="escribe o selecciona los datos ", font=fuente1)
label_extra.grid(row=0,column=0)
label_extra=tk.Label(ventana2,text="necesarios para registrar una compra", font=fuente1)
label_extra.grid(row=0,column=1)
# Etiquetas y campos de entrada
label_idCompras = tk.Label(ventana2, text="Id de Compras")
label_idCompras.grid(row=1, column=0)
entry_idCompras = tk.Entry(ventana2)
entry_idCompras.grid(row=1, column=1)

label_Fecha_compra = tk.Label(ventana2, text="Fecha de Compra")
label_Fecha_compra.grid(row=2, column=0)
entry_Fecha_compra = tk.Entry(ventana2)
entry_Fecha_compra.grid(row=2, column=1)

label_idproductoC = tk.Label(ventana2, text="Id de Producto")
label_idproductoC.grid(row=3, column=0)
entry_idproductoC = tk.Entry(ventana2)
entry_idproductoC.grid(row=3, column=1)

label_Descripcion = tk.Label(ventana2, text="Descripción")
label_Descripcion.grid(row=4, column=0)
productC_listbox = tk.Listbox(ventana2)
productC_listbox.grid(row=4, column=1)

# Obtener los productos desde la base de datos y agregarlos al Listbox

cursor.execute("SELECT Producto FROM producto")
productos = [row[0] for row in cursor.fetchall()]
productC_listbox.insert(0, *productos)

# Vincular la función de actualización al evento de selección en el Listbox
productC_listbox.bind("<<ListboxSelect>>", actualizar_id)

label_CantidadC = tk.Label(ventana2, text="Cantidad")
label_CantidadC.grid(row=5, column=0)
entry_CantidadC = tk.Entry(ventana2)
entry_CantidadC.grid(row=5, column=1)

# Botón para guardar los datos
boton_guardar = tk.Button(ventana2, text="Guardar en compras", command=guardar_en_compras)
boton_guardar.grid(row=6, column=1)

#__________________________________________________________________________________________________________________
#  ______________                   .___     .    __________.__.          _.      .               __        ___
ventana3 = tk.Frame(ventana, width=20, height=30, bg="lightyellow")
label_extra=tk.Label(ventana3,text="escribe o selecciona", font=fuente1)
label_extra.grid(row=0 , column= 0)
#label_extra=tk.Label(ventana3,text="", font=fuente1)
#label_extra.pack()
label_idV = tk.Label(ventana3, text="Id de venta ")
label_idV.grid(row= 1, column= 0)
entry_idV = tk.Entry(ventana3)
entry_idV.grid(row= 1, column= 1)

label_ProductosV = tk.Label(ventana3, text="Productos disponibles")
label_ProductosV.grid(row= 2, column= 0)
# Lista de productos
productV_listbox = tk.Listbox(ventana3)
productV_listbox.grid(row= 2, column= 1)

# Obtener los productos desde la base de datos y agregarlos al Listbox
cursor.execute("SELECT Producto FROM producto")
productos = [row[0] for row in cursor.fetchall()]
productV_listbox.insert(0, *productos)
productV_listbox.bind("<<ListboxSelect>>", actualizar_descripcion)


label_descripcionV = tk.Label(ventana3, text="dar una descripcion ")
label_descripcionV.grid(row=3 , column=0 )
entry_descripcionV = tk.Entry(ventana3)
entry_descripcionV.grid(row=3 , column= 1)

label_id_SucursalV = tk.Label(ventana3, text="Id de Sucursal")
label_id_SucursalV.grid(row=4 , column= 0)
sucursal_listbox = tk.Listbox(ventana3)
sucursal_listbox.grid(row=4 , column= 1)
cursor.execute("SELECT id_Sucursal FROM sucursal")
sucursal = [row[0] for row in cursor.fetchall()]
sucursal_listbox.insert(0, *sucursal)

label_Fecha_venta = tk.Label(ventana3, text="Fecha de Venta")
label_Fecha_venta.grid(row= 5, column=0 )
entry_Fecha_venta = tk.Entry(ventana3)
entry_Fecha_venta.grid(row= 5, column= 1)

label_CantidadV = tk.Label(ventana3, text="Cantidad")
label_CantidadV.grid(row= 6, column= 0)
entry_CantidadV = tk.Entry(ventana3)
entry_CantidadV.grid(row= 6, column= 1)

# Botón para guardar los datos
boton_guardarV = tk.Button(ventana3, text="Guardar en ventas", command=guardar_en_ventas)
boton_guardarV.grid(row= 7, column= 1)

#__________________________________________________________________________________________________________________
#  ______________                   .___     .    __________.__.          _.      .               __        ___
ventana4 = tk.Frame(ventana)
label_extra=tk.Label(ventana4,text="ingresar los datos necesarios para registrar un pedido en el registro ", font=fuente1)
label_extra.pack()
label_idpedido = tk.Label(ventana4, text="Id Pedidos ")#, font=fuente2)
label_idpedido.pack()
entry_idpedido = tk.Entry(ventana4)
entry_idpedido.pack()

label_Productos = tk.Label(ventana4, text="Producto ")#, font=fuente2)
label_Productos.pack()
entry_Productos = tk.Entry(ventana4)
entry_Productos.pack()

label_descripcion_pedido = tk.Label(ventana4, text="Descripción ")#, font=fuente2)
label_descripcion_pedido.pack()
entry_descripcion_pedido = tk.Entry(ventana4)
entry_descripcion_pedido.pack()

label_estado = tk.Label(ventana4, text="Estado (listo o falta) ")#, font=fuente2)
label_estado.pack()
entry_estado = tk.Entry(ventana4)
entry_estado.pack()

boton_guardar = tk.Button(ventana4, text="Guardar en Pedidos ", command=guardar_en_pedidos)#, font=fuente2 )
boton_guardar.pack()

#__________________________________________________________________________________________________________________
#  ______________                   .___     .    __________.__.          _.      .               __        ___
ventana5 = tk.Frame(ventana)
label_extra=tk.Label(ventana5,text="Registrar una nueva sucursal ", font=fuente1)
label_extra.pack()
label_id = tk.Label(ventana5, text="ID Sucursal")#, font=fuente2)
label_id.pack()
entry_id = tk.Entry(ventana5)
entry_id.pack()

label_descipcion = tk.Label(ventana5, text="Nombre Sucursal")#, font=fuente2)
label_descipcion.pack()
entry_descripcion = tk.Entry(ventana5)
entry_descripcion.pack()

label_telefono = tk.Label(ventana5, text="Telefono")#, font=fuente2)
label_telefono.pack()
entry_telefono = tk.Entry(ventana5)
entry_telefono.pack()

boton_guardar = tk.Button(ventana5, text="Guardar en Sucursal ", command=guardar_en_sucursal)#, font=fuente2 
boton_guardar.pack()

#__________________________________________________________________________________________________________________
#  ______________                   .___     .    __________.__.          _.      .               __        ___
ventana6 = tk.Frame(ventana)
label_extra=tk.Label(ventana6,text="SELECCIONE PARA MODIFICAR O ELIMINAR UN PRODUCTO ", font=fuente1)
label_extra.pack()

listbox_idmp = tk.Listbox(ventana6)
listbox_idmp.pack()

boton_cargar = tk.Button(ventana6, text="Cargar Pedidos", command=cargar_pedidos)
boton_cargar.pack()

label_extra = tk.Label(ventana6, text="A continuacion, ingresa los datos de pedido o selecciona uno existente:")
label_extra.pack()

label_prod = tk.Label(ventana6, text="Producto")
label_prod.pack()
entry_prod = tk.Entry(ventana6)
entry_prod.pack()

label_desc = tk.Label(ventana6, text="Descripción")
label_desc.pack()
entry_desc = tk.Entry(ventana6)
entry_desc.pack()

label_est = tk.Label(ventana6, text="Estado (listo o falta)")
label_est.pack()
entry_est = tk.Entry(ventana6)
entry_est.pack()
# Botón para modificar un pedido seleccionado
boton_modificar = tk.Button(ventana6, text="Modificar Pedido", command=modificar_pedido)
boton_modificar.pack()

# Botón para eliminar un pedido seleccionado
boton_eliminar = tk.Button(ventana6, text="Eliminar Pedido", command=eliminar_pedido)
boton_eliminar.pack()

# Vincular funciones a eventos en el Listbox
listbox_idmp.bind("<<ListboxSelect>>", cargar_datos_pedido)
#__________________________________________________________________________________________________________________
#  ______________                   .___     .    __________.__.          _.      .               __        ___
# /   __/ ________ __  __   ____ |   | ____ \__| _/________ |  |
ventana.mainloop()