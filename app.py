
import streamlit as st
import Funciones as fun
import pandas as pd
import numpy as np

st.title ("Especialización en Python for Analytics")  #Titulo de la aplicacion

st.markdown ('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

st.sidebar.image("python-logo.png", width=200)
st.sidebar.title("Menu") #Panel lateral

st.sidebar.selectbox( "",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]) #Texto en el panel lateral

elementos = st.sidebar.slider("Ingrese la cantidad de elementos", 0, 100) #Slider para ingresar un numero
st.write("Cantidad de elementos:", elementos)
arreglo = np.arange(elementos) #Crear un arreglo con la cantidad de elementos ingresada
st.write(arreglo)

st.sidebar.write("Elaborado por: ")
st.sidebar.write("Erick Castro")

capital = st.number_input("Ingrese el capital inicial: ", 100, 10000, 1000)
tiempo = st.number_input("Ingrese el tiempo en años: ", value = 12)
tasa_interes = st.number_input("Ingrese la tasa de interes: ", value =0.05)    
interes = fun.interes_simple(capital_inicial = capital, tiempo_meses = tiempo, tasa_interes = tasa_interes) #Calcular el interes simple utilizando la funcion creada en Funciones.py
st.write("El interes simple es: ", int(interes))

valor = st.number_input("Ingrese un numero entero: ")
lista = list (range(int(valor)))

st.write(lista)

