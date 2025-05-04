import shap
import joblib
import matplotlib.pyplot as plt

def generate_shap_summary(X, model_path="models/artifacts/latest_model.joblib"):
    model = joblib.load(model_path)
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    shap.summary_plot(shap_values, X, show=False)
    plt.savefig("reports/figures/shap_summary.png")
