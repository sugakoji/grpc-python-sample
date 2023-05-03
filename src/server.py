from concurrent import futures
import grpc
from pb import helloworld_pb2
from pb import helloworld_pb2_grpc

# レスポンスの処理
class Greeter(helloworld_pb2_grpc.HelloWorldServiceServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloWorldResponse(message="hello world")
    
# サーバー起動処理
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_HelloWorldServiceServicer_to_server(Greeter(), server)

    # サーバーの立ち上げ
    server.add_insecure_port('[::]:5001')
    server.start()
    print("server started")
    server.wait_for_termination()
    

if __name__ == '__main__':
    serve()
    
