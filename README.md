# interactive-data-analysis
An AI-powered interactive data analysis tool leveraging Langgraph and OpenAI. Provides an automated workflow for exploratory data analysis and detailed data exploration with Pandas DataFrame agent, including chart generation.

## Overview
This project is an AI-powered data analysis tool utilizing **langgraph**, **langchain agent**, and **pandas DataFrame** to facilitate interactive data analysis.

## Motivation
With the advancements in Large Language Models (LLM) and Large Multimodal Models (LMM), AI-driven data analysis has become feasible. Examples include:
- ChatGPT for analyzing Excel or CSV files
- Vanna.ai using NL2SQL for RDB-based data analysis

However, there are limitations with these tools:
- **ChatGPT** cannot use other data sources. (only uploaded files)
- **Vanna.ai** relies on SQL, making it harder to use NoSQL or other data sources. Moreover, data from `.xlsx` or `.csv` files must be transferred into an RDB for analysis, which is cumbersome.

To address these issues, this project aims to build an AI data analysis program based on **pandas DataFrame**, supporting a wide range of data sources.

## Usage

1. Prepare the data to be analyzed:
   - Files (e.g., `.csv`, `.xlsx`)
   - Databases
   - HBase file URL

2. In the prompt, specify the location of the data for analysis.
3. Execute the program.
4. View the AI’s analysis results through the execution log.

## Project Structure
The project is built around **langgraph** where each step is defined as a node, with edges connecting nodes based on the analysis sequence. The primary nodes include:

- **load_data**: Loads data from various sources, supporting multiple data formats.
- **eda**: Performs exploratory data analysis, including `info`, `describe`, `head`, and other functions.
- **agent**: Carries out data analysis. Using the agent, the AI can generate charts, perform correlation analysis, and more, delivering insights based on the data.

## Benefits
In traditional data analysis, loading data from various sources and conducting comprehensive exploratory data analysis is time-consuming. This tool helps analysts quickly extract insights and make decisions on analysis directions, using:

- **pandas DataFrame**: A robust interface for handling diverse data sources.
- **langchain agent**: For flexible and scalable AI-driven analysis.

This allows small-scale data analysis teams or individuals to perform fast, diverse analyses across different datasets.

## License
This project is licensed under the terms of the MIT License.
