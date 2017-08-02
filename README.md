# Install git onto your machine
git clone https://github.com/git/git

# Clone the Skyline Repo
git clone https://github.com/kpparker165/Skyline.git <name_of_destination_folder>

OR

git clone git@github.com:kpparker165/Skyline.git <name_of_destination_folder>

# move into your <name_of_destination_folder>

# while inside <name_of_destination_folder>. Source the environment that is provided
source ./bin/activate
#you should now have (env) at the begining of your prompt.

# move into the "shfc_site" folder

# To run the dev server. NOTE: this will default to 127.0.0.1:8000
python manage.py runserver

# You can define the ipaddress to run it from and the port. 
python manage.py runserver 127.0.100.100
python manage.py runserver 127.0.100.100:8080
python manage.py runserver 8080


