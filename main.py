import logging
from time import sleep

from cli import cli
from fan import Fan
from service import get_temp, is_good_time


logging.getLogger().setLevel(logging.INFO)

args = cli.parse_args()

CONTROL_PIN = args.pin
TIME_BEGIN = args.time_begin
TIME_END = args.time_end
MAX_TEMPERATURE = args.temperature
DELTA_TEMP = args.delta_temp


def main(fan: Fan):
    while True:
        curr_temp = get_temp()
        if is_good_time(TIME_BEGIN, TIME_END):
            if curr_temp > MAX_TEMPERATURE and not fan.is_enable:
                fan.enable()
            elif curr_temp < MAX_TEMPERATURE - DELTA_TEMP and fan.is_enable:
                fan.disable()
        else:
            fan.disable()

        logging.info(f'| Fan state: {fan.is_enable} | Current temp: {curr_temp} |')
        sleep(1)


if __name__ == '__main__':
    f = Fan(CONTROL_PIN)
    try:
        main(f)
    except KeyboardInterrupt:
        logging.warning('Script is turned off')
    except Exception as e:
        logging.error(f'Other exeption: {e}')
    finally:
        logging.info('Fan is turned off')
        del f
