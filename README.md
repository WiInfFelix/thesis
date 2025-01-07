# Comparative Analysis of Large Language Models (LLM) and Natural Language Processing (NLP) Techniques to Enhance Data Processing for Improving Machine-Learning-Based Length-of-Stay Predictions

This is the code repository to the masters thesis of the same name. It contains python notebooks that were used to conduct the comparison, the analysis and all graphs in the thesis.

## Folders
The folders contain the notebooks for the following tasks:

- analysis:
- text_processing: Processes the text for the experiment using the different techniques
- training: Contains the training pipelines for the different experiments


## How to use
The notebooks are meant to be run in order. The notebooks in the `text_processing` folder should be run first, followed by the notebooks in the `training` folder, then the notebooks in the `analysis` folder, and finally the notebooks in the `graphs` folder. The notebooks in the `benchmarks` folder can be run at any time.
Not all of the contained notebooks are used in the thesis. Some are used for testing, experimenting or debugging. 

To run the notebooks, install the necessary packages with `pip install -r requirements.txt`.


[!IMPORTANT]
Not all input and output folders are created by git. The MIMIC dataset cannot be provided as access is restricted by PhysioNet. As such, empty folders are not created and may need to be created