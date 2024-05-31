# Copyright (c) 2024, https://github.com/arloncunha

import time
import logging

START   = None
STOP    = None
LAPS    = []

START_NS   = None
STOP_NS    = None
LAPS_NS    = []

def start_timer():
    global START
    global STOP
    global LAPS
    START    = time.time()
    LAPS.append(START)

    global START_NS
    global STOP_NS
    global LAPS_NS
    START_NS = time.time_ns()
    LAPS_NS.append(START_NS)
    # print(f"DEBUG start_timer() {START=}")
    # print(f"DEBUG start_timer() {STOP=}")

def stop_timer():

    global START
    global STOP
    global LAPS
    # print(f"DEBUG stop_timer() {START=}")
    # print(f"DEBUG stop_timer() {STOP=}")
    assert START != None, "start timer was not setted, use start_timer() before calling stop_timer()"
    STOP = time.time()
    LAPS.append(STOP)

    global START_NS
    global STOP_NS
    global LAPS_NS
    STOP_NS = time.time_ns()
    LAPS_NS.append(STOP_NS)

def lap_timer():
    global START
    global STOP
    global LAPS
    LAPS.append(time.time())

    global START_NS
    global STOP_NS
    global LAPS_NS
    LAPS_NS.append(time.time_ns())

def elapsed_time_sec():
    global START
    global STOP
    global LAPS
    # print(f"DEBUG {START=}")
    # print(f"DEBUG {STOP=}")
    # print(f"DEBUG {LAPS=}")
    return STOP - START 

def elapsed_time_ns():
    global START_NS
    global STOP_NS
    global LAPS_NS
    # print(f"DEBUG {START=}")
    # print(f"DEBUG {STOP=}")
    # print(f"DEBUG {LAPS=}")
    return STOP_NS - START_NS 

def elapsed_time():
    if elapsed_time_sec() >= 1:
       return str(elapsed_time_sec()) + 's'
    else:
       return str(elapsed_time_ns()) + 'ns'


def elapsed_time_btw_laps_sec(start_lap, end_lap):
    global START
    global STOP
    global LAPS
    # print(f"DEBUG {START=}")
    # print(f"DEBUG {STOP=}")
    # print(f"DEBUG {LAPS=}")
    return LAPS[end_lap] - LAPS[start_lap]

def elapsed_time_btw_laps_ns(start_lap, end_lap):
    global START_NS
    global STOP_NS
    global LAPS_NS
    # print(f"DEBUG {START=}")
    # print(f"DEBUG {STOP=}")
    # print(f"DEBUG {LAPS=}")
    return LAPS_NS[end_lap] - LAPS_NS[start_lap]

def elapsed_time_btw_laps(start_lap, end_lap):
    if elapsed_time_btw_laps_sec(start_lap, end_lap) >= 1:
       return str(elapsed_time_btw_laps_sec(start_lap, end_lap)) + 's'
    else:
       return str(elapsed_time_btw_laps_ns(start_lap, end_lap)) + 'ns'

