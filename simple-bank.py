import logging
import re

import click

log_levels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


@click.command()
@click.option('--input', '-i', default="recon.in",
              type=click.Path(exists=True),
              help="File to read positions and transactions from")
@click.option('--output', '-o', default="recon.out",
              type=click.Path(exists=False), help="File to output results")
@click.option('--log', '-l', default=None,
              help="Name of log file")
@click.option('--log_level', default="info",
              help="Level of logging to be output")

def process_account(input, output, log, log_level):
    """Executes file given parameters"""
    # Set up logging
    level = log_levels.get(log_level, logging.NOTSET)

    logging.basicConfig(
        level=level,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=log,
        filemode='w'
    )


    logging.info("Complete")


if __name__ == '__main__':
    process_account()
