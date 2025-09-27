import pandas
import matplotlib.pyplot as plt
dataset = pandas.read_csv('./doggy-boot-harness.csv')
del dataset["sex"]
del dataset["age_years"]
print(f"We have {len(dataset)} rows in our dataset.")

is_small = dataset.harness_size < 55;
data_from_small_dogs = dataset[is_small];
data_smaller_paws = dataset[dataset.boot_size < 40].copy()

# plt.scatter(data_smaller_paws["harness_size"],data_smaller_paws["boot_size"])

# plt.xlabel("harness_size")
# plt.ylabel("boot_size")
# plt.show();


data_smaller_paws['harness_size_imperial'] = data_smaller_paws.harness_size  / 2.54

plt.scatter(data_smaller_paws["harness_size_imperial"],data_smaller_paws["boot_size"]);
plt.xlabel("harness_size_imperial")
plt.ylabel("boot_size")
plt.show();


# Practice for getting data from file
# Inspecting top and bottom of dataframe
# Adding removing columns
# Graphing the data
