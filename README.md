# Greetings_and_Wishes_Generator

## About of project
Greetings & Wishes Generator - educational group project as part of the course on neural networks (NLP) at ITMO. We have fine tuned the [rugpt3small_based_on_gpt2](https://huggingface.co/ai-forever/rugpt3small_based_on_gpt2) model from [sber-ai](https://github.com/ai-forever/ru-gpts) on the data that we collected from the [site](https://www.pozdravuha.ru/). 

The result we got:
```
***** train metrics *****
  epoch                    =        3.0
  total_flos               =  1312249GF
  train_loss               =     1.8419
  train_runtime            = 0:25:57.44
  train_samples            =       3595
  train_samples_per_second =      6.925
  train_steps_per_second   =      6.925
```
```
***** eval metrics *****
  epoch                   =        3.0
  eval_loss               =      1.971
  eval_runtime            = 0:00:23.57
  eval_samples            =        913
  eval_samples_per_second =     38.734
  eval_steps_per_second   =     38.734
  perplexity              =     7.1779
```
```
Mean Cosine Similarity: 0.6579082608222961
```

## Project structure 
```
.
├───data
│   ├───raw                     
│   │   └───greetings.csv                  # csv file with all greetings & wishes
│   ├───processed
│   └───├───train.txt                      # dataset for training
│       └───valid.txt                      # dataset for validation
│   
├───src                         
│   └───parse.py                           # scrapes greetings & wishes from the website
├───.gitignore
├───Greetings_and_Wishes_Generator.ipynb   # trains the model on the training dataset,
│                                            contains class with the tuned model,
│                                            example how the inference works
└───README.md
```

## How to use?
1. download finetuning [model](https://drive.google.com/drive/folders/1Uov_x-soIbuEeVZUraVQFWkVAgPt44K6?usp=sharing);
2. copy [Greetings_and_Wishes_Generator.ipynb](https://github.com/tutsilianna/Greetings_and_Wishes_Generator/blob/main/Greetings_and_Wishes_Generator.ipynb) to your Google Drive and run the last partition with your data.
