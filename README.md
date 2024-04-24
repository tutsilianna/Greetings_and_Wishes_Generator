# Greetings_and_Wishes_Generator
Greetings & Wishes Generator - educational group project as part of the course on neural networks (NLP) at ITMO 

# Project structure 
```
.
├───data
│   ├───raw                     
│   │   └───greetings.csv                  # csv file with all greetings & wishes
│   ├───processed
│   │   ├───train.txt                      # dataset for training
│   │   └───valid.txt                      # dataset for validation
│   └───model                              # weights and parameters for the GPT model
├───src                         
│   └───parse.py                           # scrapes greetings & wishes from the website
├───.gitignore
├───greetings_text.txt                     # output text
├───greetings_promt.txt                    # input text
├───Greetings_and_Wishes_Generator.ipynb   # trains the model on the training dataset,
│                                            contains class with the tuned model,
│                                            example how the inference works
└───README.md
```
