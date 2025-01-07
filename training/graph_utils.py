import plotly.express as px


def plot_feature_importances(model, model_setup: str):
    """Plot feature importances from a trained catboost regressor model."""
    feature_importances = model.get_feature_importance(prettified=True)
    feature_importances = feature_importances.set_index("Feature Id")
    feature_importances = feature_importances.sort_values(
        by="Importances", ascending=True
    )
    fig = px.bar(
        feature_importances,
        x="Importances",
        y=feature_importances.index,
        orientation="h",
    )
    fig.update_layout(title=f"Feature importances for {model_setup}")
    fig.show()


def plot_regression_results(y_true, y_pred, title: str):
    """Plot regression results."""
    fig = px.scatter(
        x=y_true,
        y=y_pred,
        labels={"x": "True", "y": "Predicted"},
        trendline="ols",
        trendline_color_override="red",
    )
    fig.update_layout(title=title)
    fig.update_xaxes(title_text="True")
    fig.update_yaxes(title_text="Predicted")

    fig.update_traces(marker=dict(size=5))

    fig.show()


def plot_residuals(y_true, y_pred, title: str):
    """Plot residuals."""
    residuals = y_true - y_pred
    fig = px.scatter(
        x=y_pred,
        y=residuals,
        labels={"x": "Predicted", "y": "Residuals"},
        trendline="ols",
        trendline_color_override="red",
    )
    fig.update_layout(title=title)
    fig.update_xaxes(title_text="Predicted")
    fig.update_yaxes(title_text="Residuals")

    fig.update_traces(marker=dict(size=5))

    fig.show()
