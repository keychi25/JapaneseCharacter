from config import Config
import os
import re
import pickle
import cv2
import keras
import random
import string
from werkzeug.utils import secure_filename
from tensorflow.keras.models import Sequential
from keras.models import Sequential
from keras.utils import np_utils
from PIL import Image
import numpy as np
from flask import Flask, Blueprint, render_template, request, abort, flash
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = 'hiragana-app'
CORS(app)

tmp_dir = Config.TMP_DIR


def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')


@app.route('/run', methods=['GET', 'POST'])
def run():
    nb_classes = 72
    y_test = []
    img_rows, img_cols = 32, 32
    lowerReg = re.compile(r'^[ぁ-ゟ]+$')
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        try:
            j_character = request.form['hiragana']
            file = request.files['image']
        except Exception as err:
            return abort, 404
        if not lowerReg.match(j_character):
            flash('ひらがなを入力してください．', category='alert alert-danger')
            return render_template('index.html')

        if file:
            filename = secure_filename(file.filename)  # ファイル名
            if os.path.exists(tmp_dir):
                file.save(os.path.join(tmp_dir,
                                       filename))
        img = cv2.imread(os.path.join(tmp_dir,
                                      filename), 0)
        X_test = np.array(Image.fromarray(img).resize((img_rows, img_cols), 1))
        X_test = X_test.reshape(1, img_rows, img_cols, 1)
        y_test.append(0)
        y_test = np_utils.to_categorical(y_test, nb_classes)
        y_test = np.array(y_test)
        model = pickle.load(open("model/model_V1.sav", 'rb'))
        model.compile(loss='categorical_crossentropy',
                      optimizer='adadelta', metrics=['accuracy'])
        score = model.predict_proba(X_test)
        print(score)
        os.remove(os.path.join(tmp_dir,
                               filename))
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
