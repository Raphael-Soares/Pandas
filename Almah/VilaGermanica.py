import pandas as pd

moradores = pd.read_csv("Almah/Moradores.csv")
ocorrencias = pd.read_csv("Almah/Ocorrencias.csv")



moradores["Unidade"] = moradores["Unidade"].astype(str).str.replace(".0", "") + " - " + moradores["Bloco"] 

ocorrencias["Unidade"] = ocorrencias["Unidade"].astype(str) + " - " + ocorrencias["Bloco"]

ocorencias_moradores = pd.merge(moradores, ocorrencias, on="Unidade")

ocorencias_moradores = ocorencias_moradores[["Unidade", "Proprietário", "Título", "Tipo de Ocorrência", "Data", "Incluído Por"]]

ocorencias_moradores.to_csv("Almah/OcorrenciasMoradores.csv", index=False)



