from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    data_html = None
    insights = None
    chart_path = None
    columns = []
    selected_column = None
    chart_type = None

    if request.method == 'POST':
        file = request.files.get('file')
        selected_column = request.form.get('column')
        chart_type = request.form.get('chart')

        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            df = pd.read_csv(filepath)
            columns = df.columns.tolist()
            print("DEBUG - Columns:", columns)

            data_html = df.head(10).to_html(classes='table table-bordered', index=False)

            if selected_column and chart_type:
                if pd.api.types.is_numeric_dtype(df[selected_column]):
                    summary = df[selected_column].describe()
                    insights = f"Min: {summary['min']}, Max: {summary['max']}, Mean: {summary['mean']:.2f}, Std: {summary['std']:.2f}"

                    plt.figure(figsize=(6, 4))
                    if chart_type == 'bar':
                        df[selected_column].value_counts().plot(kind='bar')
                    elif chart_type == 'pie':
                        df[selected_column].value_counts().plot(kind='pie', autopct='%1.1f%%')

                    plt.title(f"{chart_type.capitalize()} Chart of {selected_column}")
                    chart_path = os.path.join('static', 'chart.png')
                    plt.tight_layout()
                    plt.savefig(chart_path)
                    plt.close()
                else:
                    insights = f"{selected_column} is not numeric. Only value counts will be shown."
                    
                    plt.figure(figsize=(6, 4))
                    if chart_type == 'bar':
                        df[selected_column].value_counts().plot(kind='bar')
                    elif chart_type == 'pie':
                        df[selected_column].value_counts().plot(kind='pie', autopct='%1.1f%%')

                    plt.title(f"{chart_type.capitalize()} Chart of {selected_column}")
                    chart_path = os.path.join('static', 'chart.png')
                    plt.tight_layout()
                    plt.savefig(chart_path)
                    plt.close()

    return render_template('index.html', data=data_html, columns=columns, selected_column=selected_column,
                           chart_type=chart_type, insights=insights, chart_path=chart_path)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)
