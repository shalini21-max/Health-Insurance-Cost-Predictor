import joblib

model_young = joblib.load("artifacts/model_young.joblib")
model_rest = joblib.load("artifacts/model_rest.joblib")

print("Young Model Features:")
print(model_young.feature_names_in_)

print("\nRest Model Features:")
print(model_rest.feature_names_in_)