# Install dependance 
`pip install -r requirements.txt`

# Generation protos
`python3 -m grpc_tools.protoc -Iprotos --python_out=./protos --pyi_out=./protos --grpc_python_out=./protos protos/machine.proto`