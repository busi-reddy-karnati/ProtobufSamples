from asyncio import futures
from cgi import test
import imp
import grpc
import test_pb2
import test_pb2_grpc
import concurrent.futures
class SquareRootServiceServicer(test_pb2_grpc.SquareRootServiceServicer):
    def squareRoot(self, request, context):
        '''
        This is the actual implementation of the function. In main(), we add this Service to the gprc service
        '''
        result = request.input * request.input
        return test_pb2.Result(result = result)
    
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    test_pb2_grpc.add_SquareRootServiceServicer_to_server(SquareRootServiceServicer(), server)
    print("Hello Server")
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()
    
main()