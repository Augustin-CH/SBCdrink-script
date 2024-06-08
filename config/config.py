import yaml

with open("./config/config.yml", "r") as f:
    config = yaml.safe_load(f)

BELT_ENGINE = {
    "PIN_OUT_1": config["belt_engine"]["pin_out_1"],
    "PIN_OUT_2": config["belt_engine"]["pin_out_2"],
    "PIN_OUT_3": config["belt_engine"]["pin_out_3"],
    "PIN_OUT_4": config["belt_engine"]["pin_out_4"],
    "STEP_SLEEP": config["belt_engine"]["step_sleep"],
}

BOTTLE_ENGINE = {
    "PIN_OUT_1": config["bottle_engine"]["pin_out_1"],
    "PIN_OUT_2": config["bottle_engine"]["pin_out_2"],
    "PIN_OUT_3": config["bottle_engine"]["pin_out_3"],
    "PIN_OUT_4": config["bottle_engine"]["pin_out_4"],
    "STEP_SLEEP": config["bottle_engine"]["step_sleep"],
}

BELT_LIMIT_SENSOR = {
    "PIN_SIGNAL": config["belt_limit_sensor"]["pin_signal"],
}

BOTTLE_SLOT_POSITION = {
    "SLOT_1": config["bottle_slot_position"]["slot_1"],
    "SLOT_2": config["bottle_slot_position"]["slot_2"],
    "SLOT_3": config["bottle_slot_position"]["slot_3"],
    "SLOT_4": config["bottle_slot_position"]["slot_4"],
    "SLOT_5": config["bottle_slot_position"]["slot_5"],
    "SLOT_6": config["bottle_slot_position"]["slot_6"],
    "SLOT_7": config["bottle_slot_position"]["slot_7"],
    "SLOT_8": config["bottle_slot_position"]["slot_8"],
    "SLOT_9": config["bottle_slot_position"]["slot_9"],
    "SLOT_10": config["bottle_slot_position"]["slot_10"],
    "SLOT_11": config["bottle_slot_position"]["slot_11"],
    "SLOT_12": config["bottle_slot_position"]["slot_12"],
}

TIME_FOR_ONE_QUANTITY = config["time_for_one_quantity"]

TIME_FOR_FILL_DISPENSOR = config["time_for_fill_dispensor"]

PRESENT_POSITION = config["present_position"]