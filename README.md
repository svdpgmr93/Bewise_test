# Bewise_test
## Installation
You must have ***GIT*** and ***Docker*** installed on your PC.
  + In the folder where you want to run the project, run ```git init```
  + Then run ```git remote add your_origin https://github.com/svdpgmr93/Bewise_test.git```
  + Then run ```git pull your_origin master```
In the folder you should see downloaded files from GITHUB
  + Run ```docker compose build```
  + Then run ```docker compose up```
## Usage
To use this service you need to send a POST request to *http://localhost:8000* like *http://localhost:8000/(count_of_tests:int)*
In response you will receive ```json``` like:
```
{
  "id": 2,
  "question": "Since 1950 this Caribbean capital has played host to an international Ernest Hemingway fishing tournament",
  "answer": "Havana",
  "create_time": "2023-10-21T03:43:16.670952+00:00"
}
```
or ```{}``` if there are no records in the database yet.
## PS 
If after installation, on the first launch, the API does not work, *http://localhost:8000* not response.
Please stop and restart the container ```Ctrl+C``` then ```docker compose up```

