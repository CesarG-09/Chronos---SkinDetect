from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from tkinterdnd2 import TkinterDnD, DND_FILES
from tensorflow.keras.preprocessing import image
import customtkinter as ctk
import tkinter as tk

# Configurar la pantalla principal
c_ligthskyblue = '#2B4C6B'
c_buttom = '#28649D'
c_hover_buttom = '#6090BD'

ctk.set_appearance_mode("Dark")
# Cargar el modelo entrenado desde la ruta especificada
model_path = r'Chronos---SkinDetect\models\melanoma_classifier_v2.keras'
model = tf.keras.models.load_model(model_path)

def predict_image(img_path):
    # Cargar y preprocesar la imagen
    img = image.load_img(img_path, target_size=(300, 300))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Reescalar como en el generador de datos
    
    # Realizar la predicción
    prediction = model.predict(img_array)
    
    # Convertir la predicción a una clase binaria
    if prediction[0] > 0.5:
        return "Maligno"
    else:
        return "Benigno"

class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    '''Creates a new instance of a ctk.CTk() window; all methods of the
    DnDWrapper class apply to this window and all its descendants.'''
    def __init__(self, *args, **kw):
        ctk.CTk.__init__(self, *args, **kw)
        self.TkdndVersion = TkinterDnD._require(self)

def show_prediction_interface():
    app.withdraw()
    text_font = ctk.CTkFont(family="Segoe UI", weight="bold", size=20)
    # Crear la ventana de predicción
    pred_window = ctk.CTkToplevel(app)
    pred_window.title("SkinDetect - Predicción de Melanoma")
    pred_window.geometry("800x600")
    pred_window.resizable(False, False)
    pred_window.iconbitmap(r"Chronos---SkinDetect\assets\icon.ico")

    # Crear etiquetas para mostrar la imagen y el resultado
    main_frame_all = ctk.CTkFrame(
        pred_window,
        width= 600,
        height= 500,
        fg_color= "transparent",
    )
    main_frame_all.place(rely=0.5, relx=0.5, anchor="center")
    
    main_frame_dnd = ctk.CTkFrame(
        main_frame_all,
        fg_color= "#CDCFD1",
        border_width= 3,
        border_color= "white",
        width=500,
        height=400
    )
    main_frame_dnd.pack(pady=10, side="top")
    
    image_label = ctk.CTkLabel(
        main_frame_dnd, 
        text="Arrastra y suelta una imagen aquí", 
        width=40, 
        height=20,
        font=text_font,
        text_color="black",
        fg_color="transparent"
    )
    image_label.place(rely=0.5, relx=0.5, anchor="center")

    result_label = ctk.CTkLabel(
        main_frame_all, 
        text="", 
        font=text_font
    )
    result_label.pack(pady=20, side="bottom")
    
    def on_drop(event):
        # Obtener la ruta del archivo
        img_path = event.data.strip('{}')
        
        # Mostrar la imagen en la interfaz
        img = Image.open(img_path)
        img.thumbnail((300, 300))
        ctk_img = ctk.CTkImage(
            img, 
            size=(300, 300)
        )
        image_label.configure(
            image=ctk_img,
            text=""
        )
        image_label.image = ctk_img
        
        # Realizar la predicción
        result = predict_image(img_path)
        result_label.configure(text=f"El siguiente Melanoma se predice es: \n{result}")

    # Habilitar arrastrar y soltar
    pred_window.drop_target_register(DND_FILES)
    pred_window.dnd_bind('<<Drop>>', on_drop)
    
    # Botón para regresar a la pantalla principal
    ctk.CTkButton(
        main_frame_all, 
        text="Regresar",
        font= text_font,
        command=lambda: [pred_window.destroy(), app.deiconify()]
    ).pack(fill="x", pady=20, side="bottom")

def show_how_it_works_interface():
    app.withdraw()
    text_font = ctk.CTkFont(family="Segoe UI", weight="bold", size=20)
    # Crear la ventana de explicación
    how_window = ctk.CTkToplevel(app)
    how_window.title("SkinDetect - ¿Cómo funciona?")
    how_window.geometry("800x400")
    how_window.resizable(False, False)
    how_window.iconbitmap(r"Chronos---SkinDetect\assets\icon.ico")

    # Explicación del funcionamiento del modelo
    ctk.CTkLabel(
        how_window, 
        text="El modelo analiza una imagen de Melanomas y, en base a predicciones matemáticas, dirá si el Melanoma es maligno o benigno.\n\n Advertencia: Esta aplicación no sustituye una consulta médica. Si presenta algún síntoma, por favor consulte a su médico de confianza.", 
        wraplength=500, 
        font=text_font
        ).pack(pady=20)

    # Botón para regresar a la pantalla principal
    ctk.CTkButton(
        how_window, 
        text="Regresar", 
        font= text_font,
        command=lambda: [how_window.destroy(), app.deiconify()]
    ).pack(pady=20)

def main():
    global app
    app = Tk()
    app.title("SkinDetect")
    app.geometry("800x400")
    app.resizable(False, False)

    app.iconbitmap(r"Chronos---SkinDetect\assets\icon.ico")
    
    title_font = ctk.CTkFont(family="Cascadia Code", weight="bold", size=30)
    text_font = ctk.CTkFont(family="Segoe UI", weight="bold", size=20)

    main_frame = ctk.CTkFrame(
        app, 
        fg_color="transparent"
    )
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Título de la aplicación
    title_label = ctk.CTkLabel(
        main_frame, 
        text="SkinDetect:\nAplicación para la Detección de\nCáncer de Piel",
        text_color="Black", 
        font=title_font,
        justify = "center",
        fg_color= "white",
        corner_radius= 10,
        pady=5,
        padx=5
    )
    title_label.pack(side="top")

    # Frame para los botones
    button_frame = ctk.CTkFrame(
        main_frame, 
        fg_color="transparent"
    )
    button_frame.pack(pady = 50, side="bottom")

    # Botón Empezar
    start_button = ctk.CTkButton(
        master= button_frame, 
        text="Empezar", 
        corner_radius=32, 
        fg_color= c_buttom,
        hover_color= c_hover_buttom,
        font=text_font, 
        border_color="white",
        border_width=2,
        border_spacing= 8,
        anchor= "center",
        command=show_prediction_interface
    )
    start_button.pack(pady = 8, padx = 4, fill= "x", side= "top")

    # Botón ¿Cómo Funciona?
    how_button = ctk.CTkButton(
        master= button_frame, 
        text="¿Cómo Funciona?", 
        corner_radius=32, 
        fg_color= c_buttom,
        hover_color= c_hover_buttom,
        font=text_font, 
        border_color="white",
        border_width=2,
        border_spacing= 8,
        anchor= "center",
        command=show_how_it_works_interface
    )
    how_button.pack(pady = 8, padx = 4, fill= "x", side= "bottom")

    # Iniciar la aplicación
    app.mainloop()

# Ejecutar la función principal para iniciar la aplicación
main()