from argparse import ArgumentParser


cli = ArgumentParser(description='CLI interface for control smart cooling')

cli.add_argument(
    '-t',
    '--temperature',
    default=60,
    type=float,
    help='Max temperature CPU without fan cooling, default temp=60 C'
)

cli.add_argument(
    '-te',
    '--time_end',
    default=24,
    type=int,
    help='The hours after which the board will be turned off, default time_end=24'
)

cli.add_argument(
    '-tb',
    '--time_begin',
    default=8,
    type=int,
    help='The hours after which the board will be turned on, default time_begin=8'
)

cli.add_argument(
    '-p',
    '--pin',
    default=14,
    type=int,
    help='Value for control pin in your board, default pin=14'
)

cli.add_argument(
    '-dt',
    '--delta_temp',
    default=15,
    type=int,
    help='The value of how many degrees should be cooled, default dt=15'
)
