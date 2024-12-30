from flask import Flask,render_template,redirect,url_for,request,session,flash
from second import second
import os
app=Flask(__name__)
app.register_blueprint(second,url_prefix='')
app.secret_key='hello'
directory=os.path.dirname(os.path.abspath(__file__))
@app.route('/')
def k():
    return redirect(url_for('home'))
@app.route('/choice.html' ,methods=['POST','GET'])
def home():
    if request.method=='POST':
        user=request.form['nm']
        session['user']=user
        session['directory']=directory
        return redirect(url_for('image'))
    else:
        return render_template('choice.html')
@app.route('/image.html' ,methods=['POST','GET'])
def image():
    if 'user' in session:
        user=session['user']
        if user=='1':
            flash(f'you chose Star Wars')
            flash('please provide a JPEG, JPG, PNG, BMP, GIF, TIFF, TIF, WEBP, PPM, PGM or PBM image')
            background_image='/static/backgrounds/star_wars.jpg'
            session['background']=background_image
        elif user=='2':
            flash(f'you chose Marvel')
            flash('please provide a JPEG, JPG, PNG, BMP, GIF, TIFF, TIF, WEBP, PPM, PGM or PBM image')
            background_image='/static/backgrounds/marvel.jpg'
            session['background']=background_image
        if request.method=='POST':
            file=request.files['im']
            session['file_name']=file.filename
            directory_2=directory+'/static/uploads'
            file_path=os.path.join(directory_2,file.filename)
            file.save(file_path)
            return redirect(url_for('second.result'))

    return render_template('image.html',background_image=background_image)


if __name__=='__main__':
    app.run(debug=True)