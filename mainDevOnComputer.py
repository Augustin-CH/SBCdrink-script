import sys
import os
import json
from config.config import *

# Ajouter le dossier protos au chemin du système
sys.path.append(os.path.join(os.path.dirname(__file__), 'protos'))

import grpc
from concurrent import futures
import machine_pb2, machine_pb2_grpc
from time import sleep

class MachineServicer(machine_pb2_grpc.MachineServicer):
    def MakeCocktail(self, request, context):
        print("---------------------------")
        print(f"Cocktail composition : {request.steps}")
        steps = json.loads(request.steps)

        for step in steps:
            print(f"distribute {step['pressed']*0.5}cl of {step['slot']} and wait {step['delayAfter']}")
            sleep(step['delayAfter'])

        print(f"the cocktail is finished")
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