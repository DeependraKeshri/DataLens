def get_summary(df, column):
    if column not in df.columns:
        return None

    if not df[column].dtype.kind in 'biufc':
        return None

    return df[column].describe().to_dict()


def missing_percentage(df, column):
    total = len(df)
    missing = df[column].isnull().sum()
    return round((missing / total) * 100, 2)


def get_correlation(df):
    numeric_df = df.select_dtypes(include=['number'])
    return numeric_df.corr().to_html(classes="data-table")


def get_value_counts(df, column):
    return df[column].value_counts().to_frame().to_html(classes="data-table")
