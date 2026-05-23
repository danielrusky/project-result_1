# Скрипт flask сервера для предикта
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Для проверки корректности используем следующие запросы
#
# url = http://localhost:8000/hello?param=
# response = {'param': '', 'result': 'SERVER OK'}
#
# url = http://localhost:8000/hello?param=42
# response = {'param': '42', 'result': 'SERVER OK'}
#
# url = http://localhost:8000/hello?param=python
# response = {'param': 'python', 'result': 'SERVER OK'}

# Загружаем сериализованные объект (Обученная модель)
# Признаки для тестового датасета
# Лист с порядком признаков

# ******** КОД ЗАГРУЗКИ ТРЕХ СЕРИАЛИЗОВАННЫХ ОБЪЕКТОВ

rfr = joblib.load('src/rfr.joblib')
X_test_scaled = pd.read_csv('src/X_test_scaled.zip')
feature_order = X_test_scaled.columns.tolist()

# добавляем поле "obj_id" чтобы в дальнейшем идентифицировать объект
X_test_scaled['obj_id'] = list(range(X_test_scaled.shape[0]))

# ******** КОД FLASK МЕТОДА ДЛЯ ПРОВЕРКИ РАБОТЫ СЕРВЕРА

@app.route('/hello', methods=['GET'])
def hello_chek():
    param = request.args.get('param')
    return jsonify({'param': param, 'result': 'SERVER OK'})

# Для проверки корректности используем следующие запросы

# url = http://localhost:8000/predict?obj_id=8740
# response = {'obj_id': '8740', 'prediction': 307094.233, 'response_status': 'OK'}
#
# url = http://localhost:8000/predict?obj_id=162
# response = {'obj_id': '162', 'prediction': 258471.399, 'response_status': 'OK'}
#
# url = http://localhost:8000/predict?obj_id=
# response = {'obj_id': '', 'prediction': -1.0, 'response_status': 'ERROR'}
#
# url = http://localhost:8000/predict?obj_id=python
# response = {'obj_id': 'python', 'prediction': -1.0, 'response_status': 'ERROR'}
#
# url = http://localhost:8000/predict?obj_id=-1
# response = {'obj_id': '-1', 'prediction': -1.0, 'response_status': 'ERROR'}
#
# url = http://localhost:8000/predict?obj_id=168
# response = {'obj_id': '168', 'prediction': 1699376.544, 'response_status': 'OK'}

# ******** КОД FLASK МЕТОДА ДЛЯ ПРЕДИКТА ОБУЧЕННОЙ МОДЕЛЬЮ

@app.route('/predict', methods=['GET'])
def predict():
    obj_id = request.args.get('obj_id')

    try:
        obj_id = int(obj_id)
        test_features = X_test_scaled[X_test_scaled['obj_id']==obj_id][feature_order].values
        res = np.exp(rfr.predict(test_features)[0])
        return jsonify({'prediction': round(res, 3),
                        'obj_id': str(obj_id),
                        'response_status': 'OK'})
    except:
        return jsonify({'prediction': -1, 
                        'obj_id': str(obj_id),
                        'response_status': 'ERROR'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)