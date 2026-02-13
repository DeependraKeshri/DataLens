import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def generate_plot(df, x_col, y_col, chart_type, save_path):

    plt.figure(figsize=(8, 5))

    if chart_type == 'line':
        plt.plot(df[x_col], df[y_col])

    elif chart_type == 'bar':
        plt.bar(df[x_col], df[y_col])

    elif chart_type == 'scatter':
        plt.scatter(df[x_col], df[y_col])

    elif chart_type == 'hist':
        plt.hist(df[y_col], bins=20)

    elif chart_type == 'box':
        plt.boxplot(df[y_col])

    elif chart_type == 'pie':
        data = df[y_col].value_counts()
        plt.pie(data, labels=data.index, autopct='%1.1f%%')

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{chart_type.capitalize()} Chart")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
