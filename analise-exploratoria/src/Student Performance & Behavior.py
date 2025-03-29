"""
# Análise Exploratória dos Dados - Student Performance & Behavior
# Integrantes do grupo:
# - Caio Ribeiro - 10401002  
# - Vinícius Magno – 10401365  
#
# Descrição: Este script realiza uma análise exploratória do dataset sobre
# desempenho e comportamento dos estudantes da Geração Alfa.
"""

# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento do dataset
file_path = "student_performance_behavior.csv"  # Ajustar caminho conforme necessário
df = pd.read_csv(file_path)

# Exibição das primeiras linhas do dataset
print("Dataset - Student Performance & Behavior")
print(df.head())

# Estatísticas descritivas
def summary_statistics(df, name):
    print(f"\nEstatísticas descritivas para {name}:")
    print(df.describe())

summary_statistics(df, "Student Performance & Behavior")

# Visualizações iniciais
plt.figure(figsize=(10, 5))
sns.histplot(df['score'], bins=20, kde=True)
plt.title("Distribuição das Notas dos Alunos")
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.show()

# Correlação entre variáveis
plt.figure(figsize=(10, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlação")
plt.show()

# Salvar análise exploratória processada
df.to_csv("processed_student_performance_behavior.csv", index=False)

print("Análise exploratória concluída e arquivo salvo.")
