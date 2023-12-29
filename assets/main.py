#           BIBLIOTECAS - PYWEBVIEW (APP), SCREENINFO (RESOLUÇÃO)
import webview
from screeninfo import get_monitors

#           MONITOR - RESOLUÇÃO
monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height

#           TAMANHO - RESOLUÇÃO
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.9)

#           APP DESKTOP
webview.create_window('A Chama Primordial', 
    url='C:/Users/MOABE/Desktop/app_avx/assets/frontend/index.html', 
#    html='www.google.com',
    width=window_width,
    height=window_height,
    resizable=True)

webview.start()