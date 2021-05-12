------Instalacion de proyecto------
Descargar este repositorio a un servidor que tenga instalado python en su version 3.9.5
puedes comprobar la version de python con el comando:


python --version


en el cmd de windows, de no tener instalado python, debes ir a la pagina principal de python y descargar python en su version 3.9.5,
en el momento de ejecutar el paquete de instalacion que has descargado, no olvide marca la casilla de PATH. para poder ejecutar 
python desde el cmd.
_____________________________________________________________________________________________________________

Descarge los archivos del repositorio en formato .zip y descomprima los archivos en una ruta deseada, donde pueda 
trabajar.
_____________________________________________________________________________________________________________

-----Para windows- puesta en marcha------

1. Abrir cmd o simbolo de sistema--- Utiliza comandos win + R 
2. escribe "cmd"
3. click boton ejecutar

4. ingresa el siguiente comando 	
 - cd "lugar donde se encuentra el repositorio descargado"
ejemplo : 

 cd C:\Users\natal\OneDrive\Documentos\Laboral\PruebaTecnica\Apiproductos>

5. verificar que se encuentren los archivos README.txt y requerimientos.txt, con el comando 

dir

6. Si se encuentra en la ruta indicada ejecute el siguiente archivo para instalar todos los complementos y 
frameworks requeridos para ejecutar este proyecto con el siguiente comando en cmd.

python install -r requerimientos.txt

7. al instalar los frameworks, ejecute el proyecto con el siguiente comando:

python manage.py runserver

Al ingresar este comando se desplegara algo similar a los siguiente: 
"Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 11, 2021 - 17:48:09
Django version 3.2.2, using settings 'Apiproductos.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK."


8. Ingresar al navegador de confianza y digitar el la url el numero de servidor localhost:

http://127.0.0.1:8000


9. se ejcutara el proyecto en donde visualizara algo similar a esta pagina, siga las intrucciones de la 
siguiente imagen que se encuentra en la raiz del repositorio llamada:

tutorialpng
 





