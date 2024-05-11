# push-the-front
Push the Front is a card game in which two players compete on a board with 6 tiles, aiming to push the front to the base of the enemy

# How to run
1. If you don't have a functional venv, create a python venv and install all requirements in requirements.txt
1. Activate python venv
1. Ensure you are in the root directory of the project (i.e. the same directory as this README)
1. Ensure your json file is in the folder ```json_in```
1. Use command ```python src\main.py <name-of-your-json>``` to create cards from json file, <br>
   Or use command ```python src\main.py <name-of-your-json> d``` to deck images that can be imported into tss
1. Navigate to directory ```img_out\<name-of-your-json>\``` to look for your generated images

# Notice
1. The input json files should be in format UTF-8, else there would be error
1. All json files in ```json_in\``` with name that starts with ```test``` will be gitignored

# Naming Conventions
1. Card ids should be the English names of the cards