# Chronos 

# SkinDetect

SkinDetect es un programa el cual sirve para predecir un melanoma benigno o maligno según una imagen. Utiliza una estructura de red neuronal.

## Tabla de contenidos

1. Nombre del proyecto.
2. Descripción
3. Arquitectura del proyecto 
4. Proceso de desarrollo
5. Funcionalidades extra
6. Agradecimientos

* Nombre del proyecto:

    SkinDetect

* Descripción:
  
    SkinDetect es un sistema de inteligencia artificial diseñado para la categorización y predicción de melanomas malignos y benignos a partir de imágenes de la piel. Utilizando la arquitectura InceptionV3 preentrenada, SkinDetect aplica técnicas de transferencia de conocimiento para ofrecer una herramienta precisa y eficiente en el diagnóstico de cáncer de piel.
    
    El modelo se entrena y valida con un conjunto de datos de más de 10,000 imágenes, proporcionando un análisis detallado y resultados confiables. La interfaz de usuario permite cargar imágenes fácilmente y obtener predicciones rápidas, facilitando su uso tanto para profesionales médicos como para investigadores en el campo de la dermatología.
    ![image](https://github.com/user-attachments/assets/ec606ef7-1391-4dcc-973f-382058bade1f)


* Arquitectura del proyecto 

    - Modelo Preentrenado: InceptionV3 con capas congeladas.
  
    - Capas Adicionales: GlobalAveragePooling2D, Dense (1024 unidades, ReLU), Dropout (0.1), y una capa de salida sigmoide.
    
    - Entrenamiento: 9595 imágenes de entrenamiento y 1000 de validación. Compilación con Adam y pérdida binaria. Entrenado durante 15 épocas.
    
    Interfaz de Usuario
    - Desarrollada con customtkinter, permite cargar imágenes mediante arrastrar y soltar y obtener predicciones instantáneas sobre la malignidad de los melanomas. La interfaz es intuitiva y facilita la interpretación de resultados.


* Proceso de desarrollo:

    - Fuente del dataset: 

        El dataset es originario de Kaggle:
      
        https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images

    - Limpieza de datos:

        No hubo una limpieza exhaustiva de los datos, puesto que se necesitaban las imagenes tal cual venían para una mejor predicción.
        Se cargaron las imagenes en lotes y posteriormente se normalizaron.

        ![image](https://github.com/user-attachments/assets/68bd2dbd-6b21-4b13-a9ad-09eccc3b4653)

    - Manejo excepciones/control errores

        Al haber utilizado un notebook de jupyter nos ayudo bastante en los manejos de errores durante la fase de entreno.

    - ¿Qué modelo de Machine Learning están usando?

        InceptionV3: Se utiliza la arquitectura InceptionV3 preentrenada en el conjunto de datos ImageNet. Las capas del modelo preentrenado se congelan para mantener los pesos ya aprendidos y así aprovechar su capacidad de extracción de características.

      - Capas Adicionales:

        - GlobalAveragePooling2D: Se añade una capa de pooling global para reducir las dimensiones espaciales de las características extraídas.
        - Dense: Una capa densa con 1024 unidades y activación ReLU para aprender patrones específicos de la tarea de clasificación de melanomas.
        - Dropout: Una capa de dropout con una tasa del 10% para evitar el sobreajuste.
        - Dense Final: Una capa densa con una única unidad y activación sigmoide para la clasificación binaria (melanoma maligno o benigno).

      - Estadísticos

          ![image](https://github.com/user-attachments/assets/1fbf64ef-11d3-4a24-856f-125529c4c5d8)

* Funcionalidades extra:

    - Desarrollo de interfaz gráfica de usuario
      - Se utilizó como base la librería de customtkinter, la cual nos ofrece más libertar de personalización que la librería tkinter.
      - Adicional, se integró tkinterdnd2 para un widget de Drag and Drop

    - Estos fueron las tecnologías y dependecias utilizadas:
      - Entorno de Desarrollo y Requisitos
        - Entorno de desarrollo: Jupyter Notebook
        - Versión de Python: 3.12.3
        - IDE: Visual Studio Code

      - Dependencias
        - tensorflow
        - requests
        - matplotlib
        - customtkinter
        - tkinterdnd2
       
* Agradecimiento

    Quiero dejar por escrito  mi agradecimiento a todo el equipo de samsung y fundesteam, por tan maravillos curso. A mis profesores Christian y Arthuro por la dedicación y el compromiso de conectarse a cada llamada, a explicar cada tema y preocuparse genuinamente por las dudas de los estudiantes. A la señorita Meydibeth por su paciencia, e insistencia a la hora de realizar las entregas y por haberse mantenido al tanto de cada estudiante en la medida de lo posible. Sin más que decir muchas gracias a todos por tan maravilloso curso.
