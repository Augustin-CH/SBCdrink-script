import yaml

with open("./config/config.yml", "r") as f:
    config = yaml.safe_load(f)

BELT_PIN_OUT_1 = config["belt"]["pin_out_1"]
BELT_PIN_OUT_2 = config["belt"]["pin_out_2"]
BELT_PIN_OUT_3 = config["belt"]["pin_out_3"]
BELT_PIN_OUT_4 = config["belt"]["pin_out_4"]
BELT_STEP_SLEEP = config["belt"]["step_sleep"]

BOTTLE_PIN_OUT_1 = config["bottle"]["pin_out_1"]
BOTTLE_PIN_OUT_2 = config["bottle"]["pin_out_2"]
BOTTLE_PIN_OUT_3 = config["bottle"]["pin_out_3"]
BOTTLE_PIN_OUT_4 = config["bottle"]["pin_out_4"]
BOTTLE_STEP_SLEEP = config["bottle"]["step_sleep"]
