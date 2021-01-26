@echo off
set mypath=%cd%
cd %mypath%  
python manage.py runserver
pause