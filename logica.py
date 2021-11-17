import beconnect

def gestionarProv():
    Opcion = input ("1- Dar de alta  2- Dar de baja  3- Mostrar proveedor 4- Salir: \t")
    if Opcion == 1:
        altaProv()
    elif Opcion == 2:
        bajaProv()
    elif Opcion == 3:
        ElegirProv = input ("Elegir nombre del proveedor a mostrar: \t")
        beconnect.Mostrar("SELECT nombreprov FROM proveedor WHERE nombreprov = "+ ElegirProv)
    else:
        pass

def controlarProd():
    Opcion = input ("1- Dar de alta  2- Dar de baja  3- Mostrar producto 4- Salir")
    if Opcion == 1:
        altaProd()
    elif Opcion == 2:
        bajaProd()
    elif Opcion == 3:
        ElegirProd = input ("Elegir nombre del producto a mostrar: \t")
        beconnect.Mostrar("SELECT nombreprod FROM producto WHERE nombreprod = "+ ElegirProd)
    else:
        pass

def comprarProd():
    Producto = input ("Introducir ID del objeto a comprar: \t")
    Cantidad = input ("Introducir la cantidad comprada del producto: \t")
    sql = "UPDATE stock SET cantidadstock + (%s) WHERE idproducto = (%s)" 
    val= [(Cantidad,Producto)]
    beconnect.EjecutarSQL_VAL(sql, val)
    pass

def controlarStockProd():
    Opcion = input ("1- Dar de alta  2- Dar de baja  3- Mostrar stock 4- Salir: \t")
    if Opcion == 1:
        altaProd()
    elif Opcion == 2:
        bajaProd()
    elif Opcion == 3:
        ElegirProd = input ("Elegir nombre del producto a mostrar: \t")
        beconnect.Mostrar("SELECT nombreprod FROM producto WHERE nombreprod = "+ ElegirProd)
    else:
        pass

def venderCliente():
    Producto = input ("Introducir ID del objeto comprado: \t")
    Cantidad = input ("Introducir la cantidad comprada del producto: \t")
    sql = "UPDATE stock SET cantidadstock - (%s) WHERE idproducto = (%s)" 
    val= [(Cantidad,Producto)]
    beconnect.EjecutarSQL_VAL(sql, val)
    pass

def reservarProd():
    altaReser()
    pass


#GESTIONAR PROVEEDORES
def altaProv():
    Nombre = input ("Inserte nombre del proveedor: \t" )
    Descripcion = input ("Inserte descripción del proveedor: \t")
    sql = "INSERT INTO proveedor (nombreprov,descripcion) VALUES (%s,%s)" 
    val= [(Nombre,Descripcion)]
    beconnect.EjecutarSQL_VAL(sql, val)

def bajaProv():
    IDprov = input ("Inserte ID del proveedor: \t" )
    sql = "DELETE FROM proveedor WHERE proveedorid = (%s)" 
    val= [(IDprov)]
    beconnect.EjecutarSQL_VAL(sql, val)

#GESTIONAR PRODUCTOS
def altaProd():
    Nombre = input ("Inserte nombre del producto: \t" )
    Descripcion = input ("Inserte descripción del producto: \t")
    sql = "INSERT INTO producto (nombreprod,descripprod) VALUES (%s,%s)" 
    val= [(Nombre,Descripcion)]
    beconnect.EjecutarSQL_VAL(sql, val)

def bajaProd():
    IDprod = input ("Inserte ID del producto: \t" )
    sql = "DELETE FROM producto WHERE productoid = (%s)" 
    val= [(IDprod)]
    beconnect.EjecutarSQL_VAL(sql, val)

#GESTIONAR CLIENTES
def altaClien():
    Nombre = input ("Inserte nombre del cliente: \t")
    Apellido = input ("Inserte apellido del cliente: \t")
    sql = "INSERT INTO cliente (nombre,apellido) VALUES (%s,%s)" 
    val = [(Nombre,Apellido)]
    beconnect.EjecutarSQL_VAL(sql, val)

def bajaClien():
    DNIcliente = input ("Inserte DNI del cliente: \t")
    sql = "DELETE FROM cliente WHERE dnicliente = (%s)"
    val = [(DNIcliente)]
    beconnect.EjecutarSQL_VAL(sql, val)

#GESTIONAR RESERVA
def altaReser():
    Cliente = input ("Inserte ID del cliente: \t")
    Producto = input ("Inserte el producto reservado: \t")
    sql = "INSERT INTO reserva (clienteid,productoreser) VALUES (%s,%s)" 
    val = [(Cliente,Producto)]
    beconnect.EjecutarSQL_VAL(sql, val)

def bajaReser():
    IDreserva = input ("Inserte ID de la reserva: \t")
    sql = "DELETE FROM reserva WHERE idreserva = (%s)"
    val = [(IDreserva)]
    beconnect.EjecutarSQL_VAL(sql, val)
