import streamlit as st

def aplicar_estilos():
    st.markdown("""
        <style>
        /* 1. Fondo principal */
        .stApp {
            background-color: #f8fafc;
        }

        /* 2. Títulos y textos claros */
        h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
            color: #0f172a !important;
        }

        /* 3. Sidebar */
        [data-testid="stSidebar"] {
            background-color: #1e293b;
        }
        [data-testid="stSidebar"] * {
            color: #f8fafc !important;
        }

        /* 4. CAMBIAR COLOR DE LOS BOTONES */
        .stButton > button {
            background-color: #10b981 !important; /* <--- Color normal del botón (Ej: Verde) */
            color: #ffffff !important;             /* Color del texto del botón */
            border-radius: 8px !important;
            border: none !important;
            padding: 0.5rem 1.2rem !important;
            font-weight: 600 !important;
            transition: all 0.2s ease-in-out !important;
        }
        
        .stButton > button:hover {
            background-color: #059669 !important; /* <--- Color cuando le pasas el mouse por encima */
            transform: translateY(-1px);
        }

        /* 5. Tarjetas de métricas */
        [data-testid="stMetric"] {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            padding: 18px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        [data-testid="stMetricLabel"] {
            color: #64748b !important;
        }
        [data-testid="stMetricValue"] {
            color: #0f172a !important;
            font-weight: 700;
        }

        /* 6. Tablas */
        [data-testid="stDataFrame"] {
            border: 1px solid #e2e8f0;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)


    