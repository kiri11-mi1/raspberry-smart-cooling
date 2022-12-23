import sys
from subprocess import check_output
from re import findall
from datetime import datetime


def get_temp() -> float:
	'''Получение текущей температуры в градусах'''
	out_of_program = check_output(["vcgencmd","measure_temp"]).decode()
	temp_value = findall('\d+\.\d+', out_of_program)[0]
	return float(temp_value)


def is_good_time(begin: int, end: int) -> bool:
	'''Можно лю включить вентилятор в данный момент'''
	current = datetime.now().hour
	if begin < end:
		return end > current > begin
	elif begin > end:
		interval = list(range(begin, 24)) + list(range(end))
		return current in interval
	return False
