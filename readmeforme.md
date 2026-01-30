1- Create Python Environment 

2- create setup.py if you write code in directories so it tell you module not found so to use your code without error of import issues we need this. and we also need __init_.py so we include that info in setup.py 

3- create a libarary or package like sensor by      creating folder and then within it __init__.py

4- librray is like a group of code like panda for processing 

5- python setup.py install now it will create packages inside lib in venv so when if you are importing code from directories it will not give error module not found.

note egg.ingo is automatically craeted that contains metadata about your packages.

-e . in requirements.txt tells that these folders are packages to the python interpreter. so when you install requirements.txt it also triggers setup.py.

6- create pipeline directory with __init__.py
7- create directorry components with __init__.py
8- create data extarctor directory with __init__.py 

9- create folder cloud storage whgich wil have code to get data from s3 upload data to s3 etc.

10. create directory configuration which will have code of connection with aws with databases etc.

11- craete folder anme as constants which will have these hard coded things.

12- create logger.py and exception.py within sensor directory not main.


steps data extraction -validation - preparation- model tarining - model evaluation - model validation - github- deployment

13- create entity directory  which will have information what will be my input what will be output for e.g traing, validation, extraction, validation etc. so it will have artifact_entity.py and config_entity in which input to anything will be specified like what will be input to model validation, like in data extaction mongodb database will be the input entity etc.

so every input to component will be specified in config_entity.py
every output from a component will be specified in artifact_entity.py

 artifact is when anything you file pipeline is generating any ouput is artifact, e.g model trained pickle file, any other thing. e.g anything your pipeline is generating like good data or data drift report is generated thats all artifact.


 14- create ml model here we will maintain custom loss custom model code etc here.