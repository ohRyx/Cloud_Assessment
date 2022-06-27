# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import safe_entry_pb2_grpc, safe_entry_pb2


class Safe_Entry(safe_entry_pb2_grpc.Safe_EntryServicer):

    def Check_In(self, request, context):
        return safe_entry_pb2.Check_In_Request(user_id=request.user_id, location=request.location, date=request.date,
                                               time=request.time)
    
    def Check_Out(self, request, context):
        return safe_entry_pb2.Check_Out_Request(user_id=request.user_id, location=request.location, date=request.date,
                                               time=request.time)
                                    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    safe_entry_pb2_grpc.add_Safe_EntryServicer_to_server(Safe_Entry(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
