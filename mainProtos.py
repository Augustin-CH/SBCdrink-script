import sys
import os
import json
from config.config import *
# from functions.getLiquid import getLiquid

# Ajouter le dossier protos au chemin du système
sys.path.append(os.path.join(os.path.dirname(__file__), 'protos'))

import grpc
from concurrent import futures
import machine_pb2, machine_pb2_grpc
from time import sleep

class MachineServicer(machine_pb2_grpc.MachineServicer):
    def MakeCocktail(self, request, context):
        print("---------------------------")
        print(f"Action demandée : {request.steps}")
        steps = json.loads(request.steps)

        # order steps by order key
        steps.sort(key=lambda step: step['order'])

        for step in steps:
            print(f"distribute {step['quantity']}cl of {step['ingredient']} from slot {step['slot']}")
            getLiquid(2)
            # sleep(1)

        return machine_pb2.MakeCocktailResponse(success=True, message="Action réalisée avec succès")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    machine_pb2_grpc.add_MachineServicer_to_server(
        MachineServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()