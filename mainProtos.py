import sys
import os
import json
from config.config import *
from functions.getLiquid import getLiquid
from functions.rotate import initPosition, rotate, presentCoktail

# Ajouter le dossier protos au chemin du système
sys.path.append(os.path.join(os.path.dirname(__file__), 'protos'))

import grpc
from concurrent import futures
import machine_pb2, machine_pb2_grpc
from time import sleep
# import RPi.GPIO as GPIO

position = 0

def initBeltPosition():
    print("----- init position -----")
    initPosition()
    rotate("belt", 4, "right")
    position = 4
    sleep(2)
    return position

class MachineServicer(machine_pb2_grpc.MachineServicer):
    def MakeCocktail(self, request, context):
        print("---------------------------")
        print(f"Cocktail composition : {request.steps}")
        position = initBeltPosition()
        steps = json.loads(request.steps)

        for step in steps:
            print(f"distribute {step['pressed']*0.5}cl of {step['slot']} and wait {step['delayAfter']}")
            position = getLiquid(step['pressed'], step['slot'], position)
            sleep(step['delayAfter'])

        print(f"the cocktail is finished")
        position = presentCoktail(position)
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