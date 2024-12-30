from flask import Blueprint,render_template,session,url_for,flash,request,redirect
import tensorflow as tf
from tensorflow import keras
from keras import backend as K
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
second=Blueprint("second",__name__)
@second.route('/result.html', methods=['POST','GET'])
def result():
    if request.method=='POST':
        filename=session['file_name']
        image_path = session['directory']+'/static/uploads/'+filename
        os.remove(image_path)
        K.clear_session()
        session.clear()
        return redirect(url_for('home'))
    else:
        filename=session['file_name']
        imag_url=url_for('static',filename=f'uploads/{filename}')
        choice=session['user']
        if choice=='1':
            model_path = os.path.join(session['directory'], 'starwars_resnet.h5')
            model = keras.models.load_model(model_path)
            names=['YODA','LUKE SKYWALKER','R2-D2','MACE WINDU','GENERAL GRIEVOUS']
        else:
            model_path = os.path.join(session['directory'], 'marvel_resnet.h5')
            model = keras.models.load_model(model_path)
            names=['SPIDERMAN','VENOM','BLACKWIDOW','CAPTAIN-AMERICA','IRON-MAN']
        preprocess_input=tf.keras.applications.vgg16.preprocess_input
        image_path = session['directory']+'/static/uploads/'+filename
        img = load_img(image_path, target_size=(224, 224))  # Resize the image
        img_array = img_to_array(img)  # Convert to a NumPy array
        img_array = preprocess_input(img_array)  # Apply preprocessing
        img_array = tf.expand_dims(img_array, axis=0)  # Add batch dimension
        predictions = model.predict(img_array)  # Make predictions
        predicted_class = np.argmax(predictions, axis=1)
        flash(f'The image is of : {names[predicted_class[0]]}')
        return render_template('result.html',img_url=imag_url,background_image=session['background'])
