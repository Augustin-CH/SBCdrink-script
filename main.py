import sys
import os
import json
from config.config import *
from functions.getLiquid import getLiquid
from functions.presentCocktail import presentCocktail
from functions.initPosition import initPosition
from functions.setAllGpioToLow import setAllGpioToLow

# Ajouter le dossier protos au chemin du système
sys.path.append(os.path.join(os.path.dirname(__file__), 'protos'))

import grpc
from concurrent import futures
import machine_pb2, machine_pb2_grpc
from time import sleep
# import RPi.GPIO as GPIO

currentPosition = 0

class MachineServicer(machine_pb2_grpc.MachineServicer):
    def MakeCocktail(self, request, context):
        print("---------------------------")
        print(f"Cocktail composition : {request.steps}")
        currentPosition = initPosition("belt", 4)

        # steps format :
        # Array<{
        #     stepId: string
        #     pressed: number
        #     delayAfter: number
        #     position: number
        # }>
        steps = json.loads(request.steps)
        dispenserEmptyingTime = request.dispenser_emptying_time 
        dispenserFillingTime = request.dispenser_filling_time

        print(f"dispenser emptying time : {dispenserEmptyingTime}")
        print(f"dispenser filling time : {dispenserFillingTime}")

        for step in steps:
            print(f"step {step['stepId']} distribute at position {step['position']}, pressed {step['pressed']} seconde and delayAfter {step['delayAfter']} seconds")
            currentPosition = getLiquid(step, currentPosition, dispenserEmptyingTime, dispenserFillingTime)
            sleep(step['delayAfter'])

        print(f"the cocktail is finished")
        # currentPosition = presentCocktail(currentPosition)
        setAllGpioToLow()
        return machine_pb2.MakeCocktailResponse(success=True, message="Cocktail done with success")

def serve():
    print("Server started")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    machine_pb2_grpc.add_MachineServicer_to_server(
        MachineServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
    # GPIO.cleanup()