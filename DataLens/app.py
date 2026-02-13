import os
import uuid
import pandas as pd
import plotly.express as px
import plotly.io as pio

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from utils.file_handler import read_file
from utils.analysis import (
    get_summary,
    missing_percentage,
    get_correlation,
    get_value_counts
)

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

df_global = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    global df_global

    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)
    unique_name = str(uuid.uuid4()) + "_" + filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)

    file.save(filepath)

    try:
        df_global = read_file(filepath)
    except Exception as e:
        print("Error reading file:", e)
        return redirect(url_for('index'))

    return redirect(url_for('dashboard'))


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    global df_global

    if df_global is None:
        return redirect(url_for('index'))

    plot_div = None
    summary = None
    missing = None
    correlation = None
    value_counts = None

    if request.method == 'POST':
        x_col = request.form.get('x_column')
        y_col = request.form.get('y_column')
        chart_type = request.form.get('chart_type')
        analysis_type = request.form.get('analysis_type')

        # 📊 Plotly Visualization
        if chart_type:
            if chart_type == "line":
                fig = px.line(df_global, x=x_col, y=y_col)
            elif chart_type == "bar":
                fig = px.bar(df_global, x=x_col, y=y_col)
            elif chart_type == "scatter":
                fig = px.scatter(df_global, x=x_col, y=y_col)
            elif chart_type == "histogram":
                fig = px.histogram(df_global, x=x_col)
            elif chart_type == "box":
                fig = px.box(df_global, x=x_col, y=y_col)
            elif chart_type == "violin":
                fig = px.violin(df_global, x=x_col, y=y_col)
            elif chart_type == "area":
                fig = px.area(df_global, x=x_col, y=y_col)
            elif chart_type == "pie":
                fig = px.pie(df_global, names=x_col)

            plot_div = pio.to_html(fig, full_html=False)

        # 📈 Data Analysis Options
        if analysis_type:
            if analysis_type == "summary":
                summary = get_summary(df_global, y_col)
                missing = missing_percentage(df_global, y_col)

            elif analysis_type == "correlation":
                correlation = get_correlation(df_global)

            elif analysis_type == "value_counts":
                value_counts = get_value_counts(df_global, x_col)

    return render_template(
        "dashboard.html",
        columns=df_global.columns.tolist(),
        shape=df_global.shape,
        plot_div=plot_div,
        summary=summary,
        missing=missing,
        correlation=correlation,
        value_counts=value_counts
    )


@app.route('/features')
def features():
    return render_template('features.html')


if __name__ == '__main__':
    app.run(debug=True)
