from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictionPipeline

app = Flask(__name__)
@app.route('/')  # creates a direct homepage, when app is run this will be opened directly.
def index():
    return render_template('index.html')

@app.route('/predictprice', methods=['GET', 'POST'])
def predict_price():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Company= request.form.get('Company'),
            TypeName= request.form.get("typename"),
            Ram = request.form.get("ram"),
            Gpu = request.form.get('gpu'),
            Weight = request.form.get('weight'),
            Touchscreen = request.form.get("touchscreen"),
            Ips = request.form.get("ips"),
            x_res = request.form.get('xres'),
            y_res = request.form.get('yres'),
            inches = request.form.get('inches'),
            CpuName = request.form.get('cpu'),
            HDD = request.form.get('hdd'),
            SSD = request.form.get('ssd'),
            OS = request.form.get("os")
            



        )  # For actual model and predicting class
        predict_df = data.get_data_as_dataframe()
        print(predict_df)
        predict_pipeline = PredictionPipeline()
        results = predict_pipeline.predict(predict_df)
        return render_template('home.html', result=results[0])

if __name__ == '__main__':
    app.run(debug=True)
