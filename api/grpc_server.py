import grpc
from concurrent import futures
import time
from blockchain.block import Block
from grpc import ServicerContext

class BlockchainServicer(grpc.Servicer):
    def GetBlock(self, request, context: ServicerContext):
        return Block(index=request.index)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc.add_BlockchainServicer_to_server(BlockchainServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
