import mlflow


def train_and_log(x: float):
    # Démarre un run MLflow
    with mlflow.start_run(run_name="simple_predict"):
        # Exemple de "paramètre" et de "métrique"
        mlflow.log_param("coef", 2.0)
        mlflow.log_param("bias", 1.0)

        y = 2 * x + 1
        mlflow.log_metric("input_x", x)
        mlflow.log_metric("output_y", y)

        return y
