EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time remaining.

    :param number_of_layers: int - total layers in the lasagna.
    :return: int - preparation time (in minutes) derived from 'number_of_layers'.

    Function that takes the number of layers in the lasagna as an argument and 
    returns how many minutes the lasagna needs for preparation.
    """
    prep_time = number_of_layers * PREPARATION_TIME
    return prep_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the preparation time remaining.

    :param number_of_layers: int - total layers in the lasagna.
    :param elapsed_bake_time: int -  time in mins of how long the lasagna has baked in the oven.
    :return: int - elapsed time (in minutes) derived from 'number_of_layers' and 'elapsed_bake_time'.

    Function that takes 
    the number of layers in the lasagna and 
    the time the lasagna has been baking in the oven as an argument and 
    returns how many minutes the lasagna has already taken for both prep and baking.
    """
    total_prep_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_prep_time

