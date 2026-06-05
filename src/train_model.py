from preprocess import prepare_data
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib

df = prepare_data()

X = df[["temp_max", "temp_min", "precipitation", "wind_speed", "humidity"]]
y = df["next_day_temp"]
model = XGBRegressor()
model.fit(X, y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
preds = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, preds))
print("R2:", r2_score(y_test, preds))
print("Total samples:", len(df))

joblib.dump(model, "model.pkl")
