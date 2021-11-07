import time

import numpy as np
from datetime import timedelta
from datetime import datetime


"""to facilitate calculations, all times are timedeltas, not actual time objects"""


class TargetCalculator:

    def __init__(self, break_periods, cycle_time, max_target, reset_time=timedelta(hours=6)):
        self.break_periods = break_periods
        self.cycle_time = cycle_time
        self.max_target = max_target
        self.reset_time = reset_time

        print(type(max_target))
        assert type(max_target) == int
        assert type(cycle_time) == type(reset_time) == timedelta

    def calculate_target(self, target_time):

        """takes target_time as timedelta from midnight as input.
        Returns target quantity based on cycle time and breaks"""

        assert type(target_time) == timedelta

        print(target_time)

        normalized_target_time = self.normalize_to_midnight(target_time)
        print(normalized_target_time)

        for period in break_periods:  # period[0] = break_begin, period[1] = break_end
            break_begin = self.normalize_to_midnight(period[0])
            break_end = self.normalize_to_midnight(period[1])

            if break_end > reset_time > break_begin:  # special case break lasting over reset
                print("WARNING: Break over reset!")
                normalized_target_time = self.account_for_pause(normalized_target_time, timedelta(hours=0), break_end)
                normalized_target_time = self.account_for_pause(normalized_target_time, break_begin, timedelta(hours=0))
            else:
                normalized_target_time = self.account_for_pause(normalized_target_time, break_begin, break_end)

        print(normalized_target_time)

        target = np.floor(normalized_target_time / cycle_time)  # use floor because target should only increase for each full cycle

        print(target)
        target = max_target if target > max_target else target
        print(target)

        return target

    def normalize_to_midnight(self, input_time):
        """
        normalizes input time based on input reset time, so that output matches time elapsed since reset, e.g.:
        input 14:00 / reset 06:00 --> normalized 08:00
        input 04:00 / reset 06:00 --> normalized 22:00
        """
        if input_time > self.reset_time:
            return input_time - self.reset_time
        else:
            return (timedelta(hours=24) - self.reset_time) + input_time

    @staticmethod
    def account_for_pause(input_time, break_begin, break_end):  # requires times to be normalized to midnight!

        if input_time > break_end:  # break fully passed
            input_time = input_time - (break_end - break_begin)
        elif input_time > break_begin:  # during break
            input_time = input_time - (input_time - break_begin)
        return input_time


class AndonBackend:

    def __int__(self, elements, ):
        pass

    def read_ini(self):
        pass

    def run(self):
        while 1:
            print("running")
            time.sleep(5)

if __name__ == "__main__":
    # =========================================CONFIGURABLE=============================================================
    # todo put in config / class / function input

    break_periods = [(timedelta(hours=9, minutes=0), timedelta(hours=9, minutes=15)),
                     (timedelta(hours=12, minutes=20), timedelta(hours=12, minutes=50)),
                     (timedelta(hours=17, minutes=0), timedelta(hours=17, minutes=30)),
                     (timedelta(hours=1, minutes=0), timedelta(hours=1, minutes=30))]

    reset_time = timedelta(hours=6)
    cycle_time = timedelta(minutes=20)
    max_target = 40
    # ==================================================================================================================

    calculator = TargetCalculator(break_periods, cycle_time, max_target, reset_time)

    calculator.calculate_target(timedelta(hours=datetime.now().hour, minutes=datetime.now().minute))
    calculator.calculate_target(timedelta(hours=5, minutes=0))
