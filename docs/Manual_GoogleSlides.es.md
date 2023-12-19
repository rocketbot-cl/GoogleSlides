



# Google Slides
  
Este módulo le permite crear, escribir y actualizar presentaciones de Google. Puede agregar o eliminar diapositivas y texto en ellas; descargar la presentación en varios formatos; y más.  

![banner](imgs/BannerGoogleSlides.jpg)

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

## Como usar este módulo

Antes de usar este módulo, debe registrar su aplicación en Google Cloud Portal.

1. Inicie sesión con una cuenta de Google y acceda al siguiente enlace:
https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete el formulario para crear un nuevo proyecto y luego presione "Crear".
3. Dentro del menú de navegación (izquierda), acceda a API y servicios.
4. Ve a la sección superior y presiona "+ HABILITAR API Y SERVICIOS".
5. Busque "Google Slides API", selecciónelo y luego presione "HABILITAR". Lo mismo con “Google Drive Api”.
6. Vuelva al menú de navegación, vaya a API y servicios y luego acceda a Credenciales.
7. Pulse Crear credenciales y seleccione ID de cliente de OAuth. Luego seleccione Tipo de aplicación:
Aplicación de escritorio, asígnele un nombre y presione Crear.
8. Descargue el archivo JSON de credenciales.
9. Finalmente, vuelve al Menú de Navegación, ve a la Pantalla de Consentimiento y agrega tu usuario en la sección "Usuarios de prueba" (aunque sea el mismo que está creando la aplicación).
 
Nota: Cuando se realiza la primera conexión, se creará un archivo .pickle en la carpeta raíz de Rocketbot, para conectarse al mismo servicio con otra cuenta, debe asignar un nombre a cada sesión. Si las credenciales caducan, debe eliminar el archivo .pickle y crear y descargar un archivo de credenciales nuevo (JSON).


## Descripción de los comandos

### Configurar credenciales G-Suite
  
Obtiene los permisos para manejar Google Slides con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta|Ruta al archivo JSON|C:/ruta/a/credenciales.json|
|Session|Identificador de sesión (Opcional)|session|
|Variable|Variable donde se guardará el resultado|res|

### Nueva Presentación
  
Crea una nueva presentación de Google Slides con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Titulo de la presentación||Título|
|Variable|Variable donde se guardará el resultado|res|
|Session|Identificador de sesión (Opcional)|session|

### Agregar diapositiva en blanco
  
Agrega una nueva diapositiva a tu presentación de Google Slides
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la presentación|En la URL https//docs.google.com/presentation/d/{ID}/edit|1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Variable|Variable donde se guardará el resultado|res|
|Session|Identificador de sesión (Opcional)|session|

### Agregar diapositiva prediseñada
  
Agrega una nueva diapositiva con título y cuerpo a tu presentación de Google Slides
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la presentación|En la URL https//docs.google.com/presentation/d/{ID}/edit|1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Variable|Variable donde se guardará el resultado|res|
|Session|Identificador de sesión (Opcional)|session|

### Eliminar Presentación
  
Elimina una Presentación de Google seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Presentación|En la URL https//docs.google.com/presentation/d/{ID}/edit|14olZxHX8sQUzUg33h72b-uK32jxC1u3uwsKlw0gEgM0|
|Session|Identificador de sesión (Opcional)|session|
|Variable|Variable donde se guardará el resultado|res|

### Eliminar Diapositiva
  
Elimina una diapositiva de una Presentación de Google seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Presentación|En la URL https//docs.google.com/presentation/d/{ID}/edit|14olZxHX8sQUzUg33h72b-uK32jxC1u3uwsKlw0gEgM0|
|ID de la diapositiva|En la URL https//docs.google.com/presentation/d/{ID}/edit#slide=id.{SlideID}|SLIDES_API1476047835_0|
|Session|Identificador de sesión (Opcional)|session|
|Variable|Variable donde se guardará el resultado|res|

### Agregar Texto
  
Inserta un nuevo texto en una presentación de Google Slides con Rocketbot. Este comando se utiliza para diapositivas en blanco.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Presentación|En la URL https//docs.google.com/document/d/{ID}/edit|1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|ID de la diapositiva|En la URL https//docs.google.com/presentation/d/{ID}/edit#slide=id.{SlideID}|SLIDES_API735432223_0|
|Texto|Texto a insertar|Hola!|
|Tamaño de fuente|Tamaño de fuente que tendrá el texto escrito.|12|
|Alineación|Alineación que tendrá el texto escrito.|Left|
|Color de texto|Color que tendrá el texto escrito|Black|
|Negrita|Seleccionar si el texto irá en negrita.|True|
|Cursiva|Seleccionar si el texto irá en cursiva.|True|
|Subrayar|Seleccionar si el texto irá subrayado.|False|
|Variable|Variable donde se guardará el ID|res|
|Identificador de Texto|Identificador que funcionará como Element ID|MiTexto1|
|Session|Identificador de sesión (Opcional)|session|

### Insertar Texto
  
Inserta texto en un elemento ya creado en una diapositiva específica de Google Slides.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Presentación|En la URL https//docs.google.com/document/d/{ID}/edit|1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|ID de la diapositiva|En la URL https//docs.google.com/presentation/d/{ID}/edit#slide=id.{SlideID}|SLIDES_API735432223_0|
|ID del Elemento|Ocupar el comando 'Obtener Element ID' para obtener el ID del elemento al que se quiere insertar el texto|SLIDES_API1561945157_2|
|Texto|Texto a insertar|Hola!|
|Tamaño de fuente|Tamaño de fuente que tendrá el texto escrito.|12|
|Alineación|Alineación que tendrá el texto escrito.|Left|
|Color de texto|Color que tendrá el texto escrito|Black|
|Negrita|Seleccionar si el texto irá en negrita.|True|
|Cursiva|Seleccionar si el texto irá en cursiva.|True|
|Subrayar|Seleccionar si el texto irá subrayado.|False|
|Variable|Variable donde se guardará el ID|res|
|Session|Identificador de sesión (Opcional)|s1|

### Eliminar Texto
  
Elimina el texto de un elemento en una presentación de Google Slides con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Presentación|En la URL https//docs.google.com/document/d/{ID}/edit|1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|ID de la diapositiva|En la URL https//docs.google.com/presentation/d/{ID}/edit#slide=id.{SlideID}|SLIDES_API735432223_0|
|ID del Elemento que contiene el Texto|De no tenerlo, ocupar el comando 'Obtener Element ID' para obtener el ID del elemento al que se quiere insertar el texto|MiTexto1|
|Variable|Variable donde se guardará el ID|res|
|Session|Identificador de sesión (Opcional)|session|

### Descargar Presentación
  
Decarga una presentación Google Slides en formato PP o PDF con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Presentación|En la URL https//docs.google.com/document/d/{ID}/edit|1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Formato del archivo (Slides)|Elige entre PDF o PPTX|---- Select format ----|
|Ruta|Ruta donde guardar archivo|C:\users\usuario\Downloads|
|Variable|Variable donde se guardará el resultado|Variable|
|Session||session|

### Obtener Element ID
  
Obtiene una lista con el ID de cada elemento que tiene la diapositiva indicada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Presentación|En la URL https//docs.google.com/document/d/{ID}/edit|14olZxHX8sQUzUg33h72b-uK32jxC1u3uwsKlw0gEgM0|
|Indice de la diapositiva a obtener|El índice debe ser un entero, tener en cuenta que la primer diapositiva es 0|0|
|Session|Identificador de sesión (Opcional)|session|
|Variable|Variable donde se guardará el resultado|Variable|
