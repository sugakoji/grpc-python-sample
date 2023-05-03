import grpc
from pb import helloworld_pb2
from pb import helloworld_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:5001') as channel:
        stub = helloworld_pb2_grpc.HelloWorldServiceStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloWorldRequest())
    print("Reponse: %s" % response.message)

if __name__ == '__main__':
    run()