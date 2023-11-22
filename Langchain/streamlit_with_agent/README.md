# Data Visualization Agent with Streamlit and Langchain

## Overview
This repository showcases the development of a data visualization agent that leverages OpenAI's powerful language model and Langchain, a library for creating applications with language models. The agent is designed to interpret user inputs, perform data analysis, and generate interactive visualizations.

## Framework
We utilize Streamlit, an open-source app framework, which is ideal for creating and sharing beautiful, custom web apps for machine learning and data science. In this project, Streamlit demonstrates its capability to rapidly develop prototypes and its potential as a deployment solution for small-scale projects.

## Features
- **Interactive Data Visualization**: The agent can plot various types of graphs (like box plots, violin plots, and scatter matrices) and display tables based on the user's request, offering a dynamic way to explore and understand data.
- **Ease of Use**: Streamlit's simplicity allows us to create web apps with minimal effort, making it an excellent tool for proof of concepts (PoCs) and quick iterations.
- **Integration with OpenAI and Langchain**: Combining these technologies, we can create an intelligent agent capable of understanding complex queries and generating appropriate visualizations.

## Project Structure
While the project demonstrates the functionalities mentioned above, it's important to note the following considerations for real-world applications:
- **Session Management**: In a production environment, managing user sessions and states is crucial. This would involve implementing `session_ids` and other state management techniques to provide a consistent and secure user experience.
- **Data Handling**: For the purposes of illustration, we load CSV files directly from a local path. In a real project, data management would involve secure and efficient data storage and retrieval mechanisms, such as databases, cloud storage solutions, and robust data pipelines.

## Getting Started
To run this project locally:
1. Clone the repository.
2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
