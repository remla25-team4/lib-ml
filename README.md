# lib-ml

[![GitHub Actions Workflow Status](https://github.com/remla25-team4/lib-ml/actions/workflows/release.yml/badge.svg)](https://github.com/remla25-team4/lib-ml/actions/workflows/release.yml)

## Overview

`lib-ml` is a Python library created as part of the REMLA `Restaurant Sentiment Analysis` application.

Its purpose is to encapsulate the common machine learning preprocessing logic required for the restaurant sentiment analysis task. This ensures consistency between the model training pipeline (`model-training`) and the prediction service (`model-service`), both of which depend on this library.

Currently, it provides functions for preprocessing review (text) data.

## How it Works

This library contains functions to perform standard text preprocessing steps, such as:

* Removing non-alphabetic characters.
* Converting text to lowercase.
* Splitting text into tokens.
* Applying Porter stemming.
* Removing standard English stopwords (excluding 'not').

The library's version is automatically determined from Git tags using `setuptools_scm` during the build process managed by the GitHub Actions workflow.

**Important Note:** This library provides the *code* for preprocessing. The *fitted* artifacts resulting from preprocessing during training (like CountVectorizer) are managed separately by the `model-training` component and utilized by `model-service`.

## Installation

This library is intended to be installed directly from its Git tag using `pip`. It is **not** published to any public package registries like PyPI.

To install a specific version (e.g., `v0.1.0`) as a dependency in another component (like `model-training` or `model-service`):

```bash
pip install git+https://github.com/remla25-team4/lib-ml.git@v<tag-name>

# Example:
# pip install git+https://github.com/remla25-team4/lib-ml.git@v0.1.0
# Replace <tag_name> with the desired release tag (e.g., v0.1.0). 

# Or
# lib-ml @ git+https://github.com/remla25-team4/lib-ml.git@v0.1.0 
# You can add this line to the requirements.txt file of your project.

```

## Usage
Once installed, import and use the preprocessing functions as needed.

Example usage within model-training or model-service

```python
from lib_ml.preprocessing import preprocess

reviews = dataset['Review']
processed_corpus = preprocess(reviews)
# now use processed_corpus with CountVectorizer...
```
