import numpy as np
import cv2

def carregar_imagem(imagem, st = False):
  '''
  Uso
       caminho[string]: local da imagem a ser aberta
       st[boolean]: será usado no streamlit ou não?
  '''
  if not st:
    return cv2.imread(imagem)

def filtar_por_cor(imagem, low_color=20, up_color=80, low_sat=50, up_sat=255, st=False):
  '''
  Uso
      imagem[img]: imagem carregada;
      low_color[int]: limite inferior da cor (min=0)
      up_color[int]: limite superior da cor (max=179)
      low_sat[int]: limite inferior de saturação (min=0)
      up_sat[int]: limite superior de saturação (max=255)
      st[boolean]: será usada no streamlit ou não?
  '''
  if not st:
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    # [35, 60, 140]
    lower = np.array([low_color, low_sat, 20])
    upper = np.array([up_color, up_sat, 255])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(imagem, imagem, mask=mask)
  
    return result

def contar_celulas(imagem_original, imagem_filtrada, blur=13, low_limit=30, up_limit=120, plot=True, st=False):
  '''
  Uso:
        imagem_original[imagem]: imagem carreda inicialmente
        imagem_filtrada[imagem]: imagem filtrada por cor
        blur[int impar]: intensidade do desfoque
        low_limit[int]: limite inferior de detecção de borda (min=0)
        up_limit[int]: limite superior de detecção de borda (max=255)
        st[boolean]: será usada no streamlit ou não?
        plot[boolean]: quer mostrar o gráfico?
  '''
  if not st:
    gray = cv2.cvtColor(imagem_filtrada, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (blur, blur), 0)
    canny = cv2.Canny(blur, low_limit, up_limit, 3)
    dilated = cv2.dilate(canny, (1, 1), iterations=0)
  
    cnt, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if cnt:
      cv2.drawContours(imagem_original, cnt, -1, (0, 255, 0), 2)
      num_celulas = len(cnt)
    else:
      cnt = 0

  
    return num_celulas
