import mlflow
import streamlit as st

st.set_page_config(page_title="MLflow Runs Dashboard", layout="wide")

st.title("MLflow Runs Dashboard")

# Indique où MLflow stocke les runs
mlflow_dir = "./mlruns"
mlflow.set_tracking_uri(f"file:{mlflow_dir}")

# Liste des expériences
experiments = mlflow.search_experiments()
exp_names = [exp.name for exp in experiments]
selected_exp = st.selectbox("Choisir une expérience", exp_names)

if selected_exp:
    exp = next(exp for exp in experiments if exp.name == selected_exp)
    runs_df = mlflow.search_runs([exp.experiment_id])

    if runs_df.empty:
        st.warning("Aucun run enregistré pour cette expérience.")
    else:
        st.subheader(f"Résultats - {selected_exp}")
        st.dataframe(
            runs_df[
                [
                    "run_id",
                    "params.coef",
                    "params.bias",
                    "metrics.input_x",
                    "metrics.output_y",
                    "start_time",
                ]
            ]
        )

        # Visualisation simple
        st.line_chart(
            runs_df[["metrics.input_x", "metrics.output_y"]].rename(
                columns={"metrics.input_x": "x", "metrics.output_y": "y"}
            )
        )
