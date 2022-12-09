# Copyright (c) 2024, https://github.com/arloncunha

import time
import logging

START   = None
STOP    = None
LAPS    = []

def start_timer():
    global START
    global STOP
    global LAPS
    START = time.time()
    # print(f"DEBUG start_timer() {START=}")
    # print(f"DEBUG start_timer() {STOP=}")
    LAPS.append(START)

def stop_timer():
    global START
    global STOP
    global LAPS
    # print(f"DEBUG stop_timer() {START=}")
    # print(f"DEBUG stop_timer() {STOP=}")
    # assert START != None, "start timer was not setted, use start_timer() before calling stop_timer()"
    STOP = time.time()
    LAPS.append(STOP)

def lap_timer():
    global START
    global STOP
    global LAPS
    LAPS.append(time.time())

def elapsed_time():
    global START
    global STOP
    global LAPS
    # print(f"DEBUG {START=}")
    # print(f"DEBUG {STOP=}")
    # print(f"DEBUG {LAPS=}")
    return STOP - START 

def elapsed_time_btw_laps(start_lap, end_lap):
    global START
    global STOP
    global LAPS
    return LAPS[end_lap] - LAPS[start_lap]