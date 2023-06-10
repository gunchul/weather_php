#!/bin/bash

(source /home/kelly_je_kim/venv/kellyenv/bin/activate && cd /home/kelly_je_kim/weather_php && ./weather_gen.sh) >> main.log 2>&1
