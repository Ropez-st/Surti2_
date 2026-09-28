import streamlit as st
import pandas as pd
from Estilo import aplicar_estilos

st.set_page_config(
    page_title="Surtid2",
    page_icon="🛒",
    layout="wide"
)

aplicar_estilos()

# DATOS INICIALES CON IMÁGENES
if "Productos" not in st.session_state:
    st.session_state["Productos"] = [
        {
            "ID": 1, 
            "Imagen": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=300",
            "Producto": "Coca Cola", 
            "Categoria": "Bebidas", 
            "Precio": 1.25, 
            "Cantidad": 10
        },
        {
            "ID": 2, 
            "Imagen": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=300",
            "Producto": "Jabon para manos", 
            "Categoria": "Limpieza", 
            "Precio": 2.50, 
            "Cantidad": 7
        },
        {
            "ID": 3, 
            "Imagen": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=300",
            "Producto": "Producto adulto", 
            "Categoria": "Otros", 
            "Precio": 15.00, 
            "Cantidad": 4
        },
        {
            "ID": 4, 
            "Imagen": "https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=300",
            "Producto": "Comida para Gatos", 
            "Categoria": "Comida", 
            "Precio": 5.00, 
            "Cantidad": 5
        },
        {
            "ID": 5, 
            "Imagen": "https://images.unsplash.com/photo-1584556812952-905ffd0c611a?w=300",
            "Producto": "Papel Higienico", 
            "Categoria": "Limpieza", 
            "Precio": 3.50, 
            "Cantidad": 9
        }
    ]

# MENÚ
st.sidebar.title("🛒 Surtid2 :)")

opcion = st.sidebar.selectbox(
    "Seleccione la opción que más le parezca:",
    [
        "🏠 Inicio",
        "📦 Productos",
        "➕ Agregar Producto",
        "✏️ Editar Producto",
        "🗑️ Eliminar Producto",
        "🔍 Buscar Producto",
        "💰 Ventas",
        "📊 Inventario"
    ]
)

# INICIO
if opcion == "🏠 Inicio":
    st.title("🏠 Bienvenido a Surtid2")
    st.write("Sistema fácil para almacenar productos, inventario y ventas.")

    col1, col2, col3 = st.columns(3)

    total_Productos = len(st.session_state["Productos"])
    total_Cantidad = sum(p["Cantidad"] for p in st.session_state["Productos"])
    valor_Inventario = sum(p["Precio"] * p["Cantidad"] for p in st.session_state["Productos"])

    with col1:
        st.metric("Productos", total_Productos)
    with col2:
        st.metric("Cantidad total", total_Cantidad)
    with col3:
        st.metric("Coste del Inventario", f"${valor_Inventario:.2f}")

    st.subheader("Productos Disponibles")
    df = pd.DataFrame(st.session_state["Productos"])
    
    # RENDERIZAR TABLA CON IMÁGENES
    st.dataframe(
        df, 
        column_config={
            "Imagen": st.column_config.ImageColumn("Foto", help="Vista previa del producto")
        },
        use_container_width=True, 
        hide_index=True
    )

# PRODUCTOS (VISTA TIPO CATÁLOGO DE TARJETAS)
elif opcion == "📦 Productos":
    st.title("📦 Catálogo de Productos")
    
    # Crear una cuadrícula de tarjetas con fotos
    cols = st.columns(3)
    for index, p in enumerate(st.session_state["Productos"]):
        with cols[index % 3]:
            with st.container(border=True):
                st.image(p["Imagen"], use_column_width=True)
                st.subheader(p["Producto"])
                st.caption(f"Categoría: {p['Categoria']}")
                st.write(f"**Precio:** ${p['Precio']:.2f}")
                st.write(f"**Stock:** {p['Cantidad']} unidades")

# AGREGAR PRODUCTO
elif opcion == "➕ Agregar Producto":
    st.title("➕ Agregar Producto")

    nombre = st.text_input("Nombre del Producto")
    categoria = st.selectbox(
        "Categoria",
        ["Bebidas", "Comida", "Lacteos", "Limpieza", "Panaderia", "Otros"]
    )
    precio = st.number_input("Precio", min_value=0.01, step=0.10)
    cantidad = st.number_input("Cantidad en stock", min_value=0, step=1)
    
    # NUEVO CAMPO DE URL DE IMAGEN
    url_imagen = st.text_input(
        "URL de la Imagen (Link)", 
        value="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=300"
    )

    if st.button("➕ Guardar Producto"):
        if nombre.strip() == "":
            st.error("Debes escribir el nombre del Producto")
        else:
            nuevo_id = 1
            if len(st.session_state["Productos"]) > 0:
                nuevo_id = max(p["ID"] for p in st.session_state["Productos"]) + 1

            nuevo_producto = {
                "ID": nuevo_id,
                "Imagen": url_imagen,
                "Producto": nombre,
                "Categoria": categoria,
                "Precio": precio,
                "Cantidad": cantidad
            }
            st.session_state["Productos"].append(nuevo_producto)
            st.success("Producto agregado correctamente")

# EDITAR PRODUCTO
elif opcion == "✏️ Editar Producto":
    st.title("✏️ Editar Producto")
    Productos = st.session_state["Productos"]

    if len(Productos) == 0:
        st.warning("No hay productos hasta el momento")
    else:
        Nombres = [p["Producto"] for p in Productos]
        Producto_seleccionado = st.selectbox("Seleccione el producto", Nombres)

        Producto = next(p for p in Productos if p["Producto"] == Producto_seleccionado)

        nuevo_nombre = st.text_input("Nombre", value=Producto["Producto"])
        
        categorias_lista = ["Bebidas", "Comida", "Lacteos", "Limpieza", "Panaderia", "Otros"]
        idx_cat = categorias_lista.index(Producto["Categoria"]) if Producto["Categoria"] in categorias_lista else 5
        nueva_categoria = st.selectbox("Categoria", categorias_lista, index=idx_cat)

        nuevo_precio = st.number_input("Precio", min_value=0.01, value=float(Producto["Precio"]), step=0.10)
        nuevo_stock = st.number_input("Stock", min_value=0, value=int(Producto["Cantidad"]), step=1)
        nueva_imagen = st.text_input("URL de Imagen", value=Producto["Imagen"])

        if st.button("💾 Guardar Cambios"):
            Producto["Producto"] = nuevo_nombre
            Producto["Categoria"] = nueva_categoria
            Producto["Precio"] = nuevo_precio
            Producto["Cantidad"] = nuevo_stock
            Producto["Imagen"] = nueva_imagen
            st.success("Producto actualizado correctamente")

# ELIMINAR PRODUCTO
elif opcion == "🗑️ Eliminar Producto":
    st.title("🗑️ Eliminar Producto")
    Productos = st.session_state["Productos"]

    if len(Productos) == 0:
        st.warning("No hay productos agregados actualmente")
    else:
        nombres = [p["Producto"] for p in Productos]
        Producto_eliminar = st.selectbox("Seleccionar Producto", nombres)

        if st.button("🗑️ Eliminar Producto"):
            st.session_state["Productos"] = [
                p for p in Productos if p["Producto"] != Producto_eliminar
            ]
            st.success("Se ha eliminado el Producto correctamente")

# BUSCAR PRODUCTO
elif opcion == "🔍 Buscar Producto":
    st.title("🔍 Buscar Producto")
    busqueda = st.text_input("Escriba el nombre del producto")

    if busqueda:
        resultados = [
            p for p in st.session_state["Productos"] 
            if busqueda.lower() in p["Producto"].lower()
        ]
        if len(resultados) > 0:
            df = pd.DataFrame(resultados)
            st.dataframe(
                df, 
                column_config={"Imagen": st.column_config.ImageColumn("Foto")},
                use_container_width=True, 
                hide_index=True
            )
        else:
            st.info("No se encontraron productos.")

# VENTAS
elif opcion == "💰 Ventas":
    st.title("💰 Registrar Venta")
    Productos = st.session_state["Productos"]

    if len(Productos) == 0:
        st.warning("No hay productos disponibles")
    else:
        nombres = [p["Producto"] for p in Productos]
        Producto_venta = st.selectbox("Seleccione el producto a vender", nombres)

        Producto = next(p for p in Productos if p["Producto"] == Producto_venta)

        col_img, col_info = st.columns([1, 2])
        with col_img:
            st.image(Producto["Imagen"], width=150)
        with col_info:
            cantidad = st.number_input("Cantidad", min_value=1, step=1)
            total = Producto["Precio"] * cantidad
            st.write(f"**Precio Unitario:** ${Producto['Precio']:.2f}")
            st.write(f"**Total a pagar:** ${total:.2f}")

        if st.button("💳 Registrar Venta"):
            if cantidad > Producto["Cantidad"]:
                st.error("No hay suficiente stock.")
            else:
                Producto["Cantidad"] -= cantidad
                st.success(f"Venta registrada por ${total:.2f}")

# INVENTARIO
elif opcion == "📊 Inventario":
    st.title("📊 Inventario")
    df = pd.DataFrame(st.session_state["Productos"])
    st.dataframe(
        df, 
        column_config={"Imagen": st.column_config.ImageColumn("Foto")},
        use_container_width=True, 
        hide_index=True
    )

    st.subheader("Productos con poco stock (5 o menos)")
    Productos_bajos = [p for p in st.session_state["Productos"] if p["Cantidad"] <= 5]

    if len(Productos_bajos) > 0:
        df_bajos = pd.DataFrame(Productos_bajos)
        st.dataframe(
            df_bajos, 
            column_config={"Imagen": st.column_config.ImageColumn("Foto")},
            use_container_width=True, 
            hide_index=True
        )
    else:
        st.success("No hay productos con stock bajo")





