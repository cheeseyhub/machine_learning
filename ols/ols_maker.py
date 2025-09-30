import pandas
import statsmodels.formula.api as smf
import joblib

data = pandas.read_csv("doggy-boot-harness.csv")
model = smf.ols(formula = "boot_size ~ harness_size", data = data).fit()

model_filename = './avalanche_dog_boot_model.pkl'
joblib.dump(model,model_filename);


model_loaded = joblib.load(model_filename)
print("Model loaded with these params")
print(model_loaded.params)
