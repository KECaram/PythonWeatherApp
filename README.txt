***These are all the packages that need to be installed in order to run my app. 
You may have to replace 'python' with 'python3' or 'pip' with 'pip3' depending on your aliases,
so if you're having trouble with any of the commands try that alteration first.***

python -m pip install --user --upgrade pip
python -m pip install --user virtualenv

***After installing pip and virtualenv travel to the 'WeatherApp' directory and execute the script 
"source env/bin/activate" to activate the virtual environment and install packages below.***

pip install requests
pip install flask
pip install configparser

***After installing all packages executing the command "python weatherWebApp.py" should launch 
the app and you should be able to access the home page by typing "localhost:5000" into your preferred web browser.***

