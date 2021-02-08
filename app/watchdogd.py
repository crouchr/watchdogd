import time
import beepy
import traceback
from pprint import pprint

import call_rest_api
import get_env

def check_aercus_serial_connected():
    try:
        alert = False

        endpoint = 'http://192.168.1.180:8998/api/data/currentdata'
        status_code, response_dict = call_rest_api.call_rest_api(endpoint)
        # pprint(response_dict)

        if response_dict['DataStopped'] == True:
            print('Error : Alert : Aercus base station USB serial connection is not connected to CumulusMX')
            alert = True

        if response_dict['AlarmBattery'] == True:
            print('Error : Alert : Aercus base station battery alarm')
            alert = True

        if response_dict['AlarmBattery'] == True:
            print('Error : Alert : Aercus base station battery alarm')
            alert = True

        if response_dict['AlarmUpgrade'] == True:
            print('Error : Alert : CumulusMX software upgrade is available')
            alert = True

        if alert:
            return False
        else:
            # print('Aercus base station / sensor OK')
            return True

    except Exception as e:
        print('Error : Alert : Unable to communicate with CumulusMX API')
        return False


def main():
    version = get_env.get_version()
    poll_secs = get_env.get_poll_secs()

    beepy.beep(sound=2)         # run a sound when this daemon starts up
    time.sleep(2)
    print('watchdogd started, version=' + version)

    while True:
        aercus_connected = check_aercus_serial_connected()
        if not aercus_connected:

            # make some noise
            beepy.beep(sound=1)
            time.sleep(0.5)
            beepy.beep(sound=1)
            time.sleep(0.5)
            beepy.beep(sound=1)

        time.sleep(poll_secs)           # typically 60 seconds


if __name__ == '__main__':
    main()
