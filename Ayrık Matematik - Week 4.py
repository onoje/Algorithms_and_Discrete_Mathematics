darkness = int(input("dark(1) - light(0):"))
presence_at_home = int(input("home(1) - out(0):"))
temperature = int(input("cold(1) - hot(0):"))
window_state = int(input("window_open(1) - window_close(0):"))
alarm_status = int(input("alarm_open(1) - alarm_close(0):"))
nighttime = int(input("night(1) - day(0):"))


def control_lights():
    if darkness == 1 and presence_at_home == 1:
        return (True)
    else:
        return (False)


def control_heating():
    if temperature == 1 and presence_at_home == 0:
        return (True)
    else:
        return (False)


def control_alarm():
    if window_state == 1 and alarm_status == 1 and nighttime == 1:
        return (True)
    else:
        return (False)


print("lights:", control_lights())
print("heat:", control_heating())
print("alarm:", control_alarm())