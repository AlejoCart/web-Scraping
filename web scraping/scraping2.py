from bs4 import BeautifulSoup
import requests

url="https://www.ibeltran.com.ar/"

resp= requests.get(url)

html=resp.text

soup = BeautifulSoup(html, "html.parser")


#Encuentra todo el texto dentro del div con la clase latest-area section-padding bg-white
noticias= soup.find('div',class_='latest-area section-padding bg-white').get_text()#strip=True formato

print("TODO EL TEXTO EN LAS NOTICIAS"+ noticias)

#Selecciona un lista de todos los elementos que esten dentro del elemento de ultimas noticias y que sean de la clase single-latest-item y e imprime el texto
noticias2=soup.select('latest-area section-padding bg-white single-latest-item')
for noticia2 in noticias2:
    print("Solo las noticias: "+ noticia2.get_text())

#encuentra todos los enlaces
print('Enlaces generales\n')
enlaces= [link.get('href') for link in soup.find_all('a')]
print(enlaces)

# encuentra las redes sociales e imprime todos los enlaces de las redes sociales

enlaces_sociales= soup.find('div', class_='social-icons')
print("\nEnlaces redes sociales \n")
for enlace_social in enlaces_sociales.find_all('a'):
    print(enlace_social.get('href')+'\n')

