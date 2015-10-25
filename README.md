# chat-data
Python script to download and process movie script data for nlp purposes.

This script was created to download open movie scripts from imsdb.com with the idea to use the data to train deep learning nlp based applications for educational purposes.

This is not finished yet, so far it only downloads all the raw scripts, parsing for conversation hasn't been implemented yet. It is coming soon.

##Dependencies:

- Requires Python 2.7

- Requires package BeautifulSoup

```bash sudo pip install BeautifulSoup```

##Usage:

To run:

```python main.py```

It takes care of the rest.

If you want to delete all the downloaded data and temporary files, run:

```python main.py clean```
