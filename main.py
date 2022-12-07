import process as ps
import streamlit as st
import cv2 
import numpy as np
from PIL import Image
 
logo = Image.open('imagem2.jpg')
st.image(logo)

st.title('ConteAlgas')
st.markdown('Este Aplicativo tem como objetivo otimizar a contagem de microalgas (células) no microscópio, para poupar a contagem manual e assim facilitar e agilizar o trabalho do pesquisador.')
imagem = st.file_uploader('Carregue a imagem ', type= ['jpg','jpeg','png'])
if imagem is not None:
    imagem_up = Image.open(imagem).convert('RGB')
    imagem_matriz = np.array(imagem_up)
    imagem_pronta = cv2.cvtColor(imagem_matriz, cv2.COLOR_RGB2BGR)

    imagem_filtrada = ps.filtar_por_cor(imagem_pronta)
    contagem = ps.contar_celulas(imagem_pronta, imagem_filtrada)
if imagem is not None:
   
   st.subheader('Resultado da Contagem :')
   st.write(str(contagem),'células') 

    
