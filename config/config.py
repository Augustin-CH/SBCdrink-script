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

BOTTLE_LIMIT_SENSOR = {
    "PIN_SIGNAL": config["bottle_limit_sensor"]["pin_signal"],
}

PRESENT_POSITION = config["present_position"]