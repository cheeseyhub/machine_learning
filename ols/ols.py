import pandas
import statsmodels.formula.api as smf
data = {
    "boot_size": [ 39, 38, 37, 39, 38, 35, 37, 36, 35, 40, 40, 36, 38, 39, 42, 42, 36, 36, 35, 41, 42, 38, 37, 35, 40, 36, 3 , 39, 41, 37, 35, 41, 39, 41, 42, 42, 36, 37, 37, 39, 42, 35, 36, 41, 41, 41, 39, 39, 35, 39, ],
    "harness_size": [ 58, 58, 52, 58, 57, 52, 55, 53, 49, 54, 59, 56, 53, 58, 57, 58, 56, 51, 50, 59, 59, 59, 55, 50, 55, 52, 53, 54, 61, 56, 55, 60, 57, 56, 61, 58, 53, 57, 57, 55, 60, 51, 52, 56, 55, 57, 58, 57, 51, 59, ],
}
dataset = pandas.DataFrame(data)
formula = "boot_size ~ harness_size"
model = smf.ols(formula = formula, data = dataset)
fitted_model = model.fit()
print(f"The following model parameters have been found: Line Slope: {fitted_model.params.iloc[1]} , Line Intercept: {fitted_model.params.iloc[0]}")


harness_size = {'harness_size' : [52.5]};
approximate_size = fitted_model.predict(harness_size);
print("Estimated Boot Size:", approximate_size[0])