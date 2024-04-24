import os
import streamlit as st
from pathlib import Path
import subprocess

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

def authenticate(username, password):
    # Aquí puedes agregar la lógica de autenticación
    # Por ejemplo, verificar si el usuario y la contraseña coinciden con ciertos valores

    auth = False

    user_main = os.environ["USER_COMM"]
    pass_main = os.environ["PASSWORD_COMM"]

    if username == user_main and password == pass_main:
        auth = True

    return auth

def main():
    st.title("Autenticacion de Usuario")

    # Pide al usuario que ingrese el nombre de usuario y la contraseña
    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")

    # Verifica si se hizo clic en el botón de inicio de sesión
    if st.button("Iniciar Sesión"):
        if authenticate(username, password):
            st.success("Inicio de sesión exitoso")

            # Si la autenticación es exitosa, ejecuta el script main2.py
            #script_path = Path("prueba_stremalit.py")
            #subprocess.Popen(["python", str(script_path)])st.success("Inicio de sesión exitoso")

            # Si la autenticación es exitosa, ejecuta el script main.py
            autenticado = True
            script_path = os.path.join(os.path.dirname(__file__), "prueba_extraccion_streamlit.py")
            subprocess.Popen(["streamlit", "run", script_path])
            subprocess.Popen(["streamlit", "run", script_path, "--autenticado", str(autenticado)])


            # Opcionalmente, podrías redirigir la página a otra URL o hacer otras acciones
        else:
            st.error("Nombre de usuario o contraseña incorrectos")

if __name__ == "__main__":
    main()
