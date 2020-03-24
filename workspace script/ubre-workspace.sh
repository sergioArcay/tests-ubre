#!/bin/bash

######################################################################################
######################################################################################

PROJECT_PATH="~/Documents/Lpro-Ubre"
BACKEND_PATH="${PROJECT_PATH}/Back-end"
FRONTEND_PATH="${PROJECT_PATH}/Front-end"

#(django-s osrm-s vroom-s ionic-s django-c osrm-c vroom-c ionic-c)
ACTS=(0 0 0 0 0 0 0 0)

######################################################################################
######################################################################################

#Check xterm installed
xterm -title "__test__" -e "exit"

if [ $? -ne 0 ]; then
    if [ "$(id -u)" != "0" ]; then
        echo "This script need to use Xterm. Run as a root to install it. (only the FIRST TIME)" 1>&2
        exit 1
    else
        apt install xterm
    fi
fi

#Run all when no param
if [ $# -eq 0 ]; then ACTS=(1 1 1 1 1 1 1 1); else

for arg in "$@"; do
    case $arg in
        "all-s")     ACTS[0]=1; ACTS[1]=1; ACTS[2]=1; ACTS[3]=1 ;;
        "back-s")    ACTS[0]=1; ACTS[1]=1; ACTS[2]=1 ;;
        "front-s")   ACTS[3]=1 ;;
        "django-s")  ACTS[0]=1 ;;
        "osrm-s")    ACTS[1]=1 ;;
        "vroom-s")   ACTS[2]=1 ;;
        "ionic-s")   ACTS[3]=1 ;;

        "all-c")                                                        ACTS[4]=1; ACTS[5]=1; ACTS[6]=1; ACTS[7]=1 ;;
        "back-c")                                                       ACTS[4]=1; ACTS[5]=1; ACTS[6]=1 ;; 
        "front-c")                                                      ACTS[7]=1 ;;
        "django-c")                                                     ACTS[4]=1 ;;
        "osrm-c")                                                       ACTS[5]=1 ;;
        "vroom-c")                                                      ACTS[6]=1 ;;
        "ionic-c")                                                      ACTS[7]=1 ;;

        "all")        ACTS[0]=1; ACTS[1]=1; ACTS[2]=1; ACTS[3]=1        ACTS[4]=1; ACTS[5]=1; ACTS[6]=1; ACTS[7]=1 ;;
        "back")       ACTS[0]=1; ACTS[1]=1; ACTS[2]=1;                  ACTS[4]=1; ACTS[5]=1; ACTS[6]=1 ;; 
        "front")      ACTS[3]=1;                                        ACTS[7]=1 ;;
        "django")     ACTS[0]=1;                                        ACTS[4]=1 ;;
        "osrm")       ACTS[1]=1;                                        ACTS[5]=1 ;;
        "vroom")      ACTS[2]=1;                                        ACTS[6]=1 ;;
        "ionic")      ACTS[3]=1;                                        ACTS[7]=1 ;;

        *) echo "ERROR: $arg is not a valid argument." ;;
    esac
done

fi

if [ ${ACTS[0]} -eq 1 ]; then xterm -title "Django backend" -e "python3 ${BACKEND_PATH}/ubre-backend/manage.py runserver" </dev/null &>/dev/null & fi
if [ ${ACTS[1]} -eq 1 ]; then xterm -title "OSRM server" -e "cd ${BACKEND_PATH}/osrm-backend; osrm-routed --algorithm=MLD galicia.osrm" </dev/null &>/dev/null & fi
if [ ${ACTS[2]} -eq 1 ]; then xterm -title "VROOM server" -e "cd ${BACKEND_PATH}/vroom-backend/vroom-express; npm start" </dev/null &>/dev/null & fi
if [ ${ACTS[3]} -eq 1 ]; then xterm -title "Ionic frontend" -e "cd ${FRONTEND_PATH}/ubre-front; ionic serve" </dev/null &>/dev/null & fi
if [ ${ACTS[4]} -eq 1 ]; then xterm -e "code --folder-uri ${BACKEND_PATH}/ubre-backend" fi
if [ ${ACTS[5]} -eq 1 ]; then xterm -e "code --folder-uri ${BACKEND_PATH}/osrm-backend" fi
if [ ${ACTS[6]} -eq 1 ]; then xterm -e "code --folder-uri ${BACKEND_PATH}/vroom" fi
if [ ${ACTS[7]} -eq 1 ]; then xterm -e "code --folder-uri ${FRONTEND_PATH}/ubre-front" fi

if [ ${ACTS[0]} -eq 1 ]; then sleep 5; firefox "localhost:8000" </dev/null &>/dev/null & fi
