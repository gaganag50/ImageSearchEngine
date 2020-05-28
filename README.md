# ImageSearchEngine


## Requirements
1. requests
2. opencv-python
3. numpy
4. imutils
5. pickle


### Simple Image Search to search most similar screenshots of 'The Hobbit and Lord of the Rings' based on 25 initial screenshots

## How to use
Just run the following two files and then the external query file to search
1. python index.py --dataset images --index index.cpickle

2. python search.py --dataset images --index index.cpickle

3. python search_external.py --dataset images --index index.cpickle --query queries/rivendell-query.png
(replace queries/rivendell-query.png by path of your query image)
