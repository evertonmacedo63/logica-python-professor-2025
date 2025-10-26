# 📘 Estrutura de Branches e Organização — Projeto Lógica com Python

Este repositório é utilizado no curso **Lógica com Python — Professor 2025**. 
Abaixo está a estrutura de versionamento e organização dos arquivos para facilitar o desenvolvimento, entrega de atividades e controle de versões.

---

## 🧠 Branches Utilizados

| Branch        | Função                                                                 |
|---------------|------------------------------------------------------------------------|
| `main`        | Versão estável e oficial. Apenas o professor atualiza com conteúdo revisado e aprovado. |
| `alunos-dev`  | Ambiente de desenvolvimento dos alunos. Aqui são disponibilizados os exercícios e onde os alunos entregam suas atividades. |
| `PROD`        | Espelho do progresso dos alunos. O professor sobe aqui os arquivos que os alunos produziram ou modificaram no `alunos-dev`. |

---

## 📁 Estrutura de Pastas no `alunos-dev`

```plaintext
├── S25/
│   ├── joao_silva/
│   │   └── aula1.py
│   ├── maria_oliveira/
│   │   └── aula1.py
│   └── modelo_exercicio.ipynb
├── S26/
│   └── ...
├── S27/
│   └── ...
├── S32/
│   └── ...
```

- Cada pasta `SXX` representa uma semana de aula.
- Dentro de cada semana, os alunos devem criar uma pasta com seu nome (sem espaços).
- Os arquivos `.py` ou `.ipynb` devem conter as soluções dos exercícios daquela semana.

---

## 🔄 Fluxo de Trabalho

1. **Criação de conteúdo**
   - O professor desenvolve os materiais no branch `main`.

2. **Distribuição para os alunos**
   - Os arquivos são disponibilizados no branch `alunos-dev`.

3. **Entrega dos alunos**
   - Cada aluno cria sua pasta dentro da semana correspondente e adiciona seus arquivos.

4. **Revisão e coleta**
   - O professor revisa os trabalhos e seleciona os que serão promovidos.

5. **Publicação em produção**
   - Os arquivos aprovados são commitados no branch `PROD`.

6. **Atualização da versão oficial**
   - O conteúdo do `PROD` é revisado e promovido para o `main`.

---

## 📌 Recomendações para os Alunos

- Sempre trabalhe no branch `alunos-dev`.
- Crie sua pasta com seu nome completo (sem espaços) dentro da semana correspondente.
- Suba apenas os arquivos relacionados à aula.
- Não altere os arquivos do professor ou de outros alunos.

---

## 👨‍🏫 Observações do Professor

Este modelo de organização permite:

- Clareza entre versões de desenvolvimento e produção  
- Controle sobre o que é publicado oficialmente  
- Acompanhamento do progresso dos alunos de forma estruturada

---
