# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # Данные, которые ты можешь заменить своими
# data = {
#     'Model': ['Simple Linear Regression', 'Multiple Linear Regression'],
#     'MAE': [1.66, 1.42],
#     'RMSE': [2.50, 2.38],
#     'R²': [0.7401, 0.7633]
# }
#
# df = pd.DataFrame(data)
#
# # Преобразуем данные для удобства построения графика
# df_melted = df.melt(id_vars='Model', var_name='Metric', value_name='Score')
#
# # Настройки стиля
# sns.set(style="whitegrid")
# plt.figure(figsize=(10, 6))
#
# # Построение графика
# sns.barplot(data=df_melted, x='Model', y='Score', hue='Metric', palette=['royalblue', 'darkorange', 'mediumseagreen'])
#
# # Добавим подписи
# plt.title('Regression Model Performance Comparison')
# plt.ylabel('Score')
# plt.xticks(rotation=15)
# plt.legend(title='')
#
# # Показать график
# plt.tight_layout()
# plt.show()

# --- Summary ---

# 1. Simple Linear Regression using G1 to predict G3:
r2_simple = 0.8233
rmse_simple = 1.88

# 2. Multiple Linear Regression using all features:
r2_multiple = 0.8487
rmse_multiple = 1.2149

# 3. Logistic Regression for pass/fail prediction:
accuracy_logistic = 0.9154

print("--- Summary ---")
print("\n1. Simple Linear Regression using G1 to predict G3:")
print(f" - R^2 Score: {r2_simple:.4f}")
print(f" - RMSE: {rmse_simple:.4f}")

print("\n2. Multiple Linear Regression using all features:")
print(f" - R^2 Score: {r2_multiple:.4f}")
print(f" - RMSE: {rmse_multiple:.4f}")

print("\n3. Logistic Regression for pass/fail prediction:")
print(f" - Accuracy: {accuracy_logistic:.4f}")
