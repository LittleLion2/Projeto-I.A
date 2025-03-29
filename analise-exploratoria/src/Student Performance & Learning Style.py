"""
# Análise Exploratória dos Dados - Student Performance & Learning Style
# Integrantes do grupo:
# - Caio Ribeiro - 10401002  
# - Vinícius Magno – 10401365  
#
# Descrição: Este script realiza uma análise exploratória do dataset sobre
# desempenho e estilos de aprendizagem dos estudantes da Geração Alfa.
"""

# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento do dataset
file_path = "student_performance_learning_style.csv"  # Ajustar caminho conforme necessário
df = pd.read_csv(file_path)

# Exibição das primeiras linhas do dataset
print("Dataset - Student Performance & Learning Style")
print(df.head())

# Estatísticas descritivas
def summary_statistics(df, name):
    print(f"\nEstatísticas descritivas para {name}:")
    print(df.describe())

summary_statistics(df, "Student Performance & Learning Style")

# Visualizações iniciais
plt.figure(figsize=(10, 5))
sns.histplot(df['hours_of_study'], bins=20, kde=True)
plt.title("Distribuição das Horas de Estudo")
plt.xlabel("Horas de Estudo")
plt.ylabel("Frequência")
plt.show()

# Correlação entre variáveis
plt.figure(figsize=(10, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlação")
plt.show()

# Salvar análise exploratória processada
df.to_csv("processed_student_performance_learning_style.csv", index=False)

print("Análise exploratória concluída e arquivo salvo.")
