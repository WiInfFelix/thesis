# Comparative Analysis of Large Language Models (LLM) and Natural Language Processing (NLP) Techniques to Enhance Data Processing for Improving Machine-Learning-Based Length-of-Stay Predictions

This is the code repository to the masters thesis of the same name. It contains python notebooks that were used to conduct the comparison, the analysis and all graphs in the thesis.

## Folders
The folders contain the notebooks for the following tasks:

- raw_data: Contains a notebook with analysis of the raw data from the MIMIC dataset
- analysis: Contains notebooks that analyze the results of the experiments
- text_processing: Processes the text for the experiment using the different techniques
- training: Contains the training pipelines for the different experiments


## How to use
To be able to run the notebooks, you need to have access to the MIMIC dataset. The dataset is not included in this repository. You can request access to the dataset at https:
[Physionet MIMIC-IV](https://physionet.org/content/mimiciv/3.1/) + [Physionet MIMIC-IV-ED](https://physionet.org/content/mimic-iv-ed/2.2/).
Access is credentialed and needs the user to provide a certificate of their training in the handling of human subject data.

The notebooks are meant to be run in order. The notebooks in the `text_processing` folder should be run first, followed by the notebooks in the `training` folder, then the notebooks in the `analysis` folder.
Not all of the contained notebooks are used in the thesis. Some are used for testing, experimenting or debugging. 

To run the notebooks, install the necessary packages with `pip install -r requirements.txt`.


[!IMPORTANT]
Not all input and output folders are created by git. Output folders for images need to be manually created.