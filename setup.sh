# Usage: source setup.sh

# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}>>> Cloning repo...${reset}"
git clone https://github.com/rg3915/django-experience.git

echo "${green}>>> Enter in django-experience directory.${reset}"
cd django-experience

echo "${green}>>> Creating virtualenv...${reset}"
python -m venv .venv
echo "${green}>>> venv is created.${reset}"

sleep 2
echo "${green}>>> activate the venv.${reset}"
source .venv/bin/activate

echo "${green}>>> Short the prompt path.${reset}"
PS1="(`basename \"$VIRTUAL_ENV\"`)\e[1;34m:/\W\e[00m$ "
sleep 2

echo "${green}>>> Installing dependencies...${reset}"
pip install -r requirements/dev.txt

echo "${green}>>> Creating .env${reset}"
python contrib/env_gen.py

echo "${green}>>> Running migrations...${reset}"
python manage.py makemigrations bookstore crm product
python manage.py migrate

echo "${green}>>> Running tests...${reset}"
python manage.py test

echo "${green}>>> Done.${reset}"

