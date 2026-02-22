import streamlit as st
import Funciones as fun

def interes_simple(capital_inicial=0, tiempo_meses=1, tasa_interes = 0.05):
  """
  Función para calcular el interés simple
  Parámetros:
  capital_inicial: Capital inicial en soles S/
  tiempo_meses: Tiempo en meses en valor entero
  tasa_interes: Tasa de interés en decimales
  return: Retorna el interés simple en soles S/
  """
  interes = capital_inicial * tasa_interes * (tiempo_meses/12)
  return interes