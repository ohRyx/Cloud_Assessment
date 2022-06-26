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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
from datetime import datetime, date

import logging

import grpc
import safe_entry_pb2_grpc, safe_entry_pb2

# Get the today date
today = date.today()
current_date = today.strftime("%d/%m/%Y")

# Get the current time
now = datetime.now()
current_time = now.strftime("%I:%M %p")


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = safe_entry_pb2_grpc.Safe_EntryStub(channel)
        print("Which User ID You Want Check-In as ?")
        print("1: 2002513")
        print("2: 2002514")
        rpc_call = input("I will be login as: ")

        if rpc_call == "1":
            print("Welcome, 2002513")
            print("Please Pick Location to check-in:")
            location_input = input("1: Bedok Mall,\n2: Changi Village Hawker Centre,\n3: Whitesands Mall\n")

            if location_input == "1":
                check_in_request = safe_entry_pb2.Check_In_Request(user_id="2002513", location="Bedok Mall",
                                                                   date=current_date, time=current_time)
                check_in_reply = stub.Check_In(check_in_request)
                print("=== Check-In Information ===")
                print("Check-In Location: " + str(check_in_reply.location_res))
                print("Check-In Date: " + str(check_in_reply.date_res))
                print("Check-In Time: " + str(check_in_reply.time_res))
                print("============================")

            elif location_input == "2":
                check_in_request = safe_entry_pb2.Check_In_Request(user_id="2002513",
                                                                   location="Changi Village Hawker Centre",
                                                                   date=current_date, time=current_time)
                check_in_reply = stub.Check_In(check_in_request)
                print("=== Check-In Information ===")
                print("Check-In Location: " + str(check_in_reply.location_res))
                print("Check-In Date: " + str(check_in_reply.date_res))
                print("Check-In Time: " + str(check_in_reply.time_res))
                print("============================")

            elif location_input == "3":
                check_in_request = safe_entry_pb2.Check_In_Request(user_id="2002513", location="Whitesands Mall",
                                                                   date=current_date, time=current_time)
                check_in_reply = stub.Check_In(check_in_request)
                print("=== Check-In Information ===")
                print("Check-In Location: " + str(check_in_reply.location_res))
                print("Check-In Date: " + str(check_in_reply.date_res))
                print("Check-In Time: " + str(check_in_reply.time_res))
                print("============================")

        elif rpc_call == "2":
            print("Welcome, 2002514")
            print("Please Pick Location to check-in:")
            location_input = input("1: Bedok Mall,\n2: Changi Village Hawker Centre,\n3: Whitesands Mall\n")

            if location_input == "1":
                check_in_request = safe_entry_pb2.Check_In_Request(user_id="2002514", location="Bedok Mall",
                                                                   date=current_date, time=current_time)
                check_in_reply = stub.Check_In(check_in_request)
                print("=== Check-In Information ===")
                print("Check-In Location: " + str(check_in_reply.location_res))
                print("Check-In Date: " + str(check_in_reply.date_res))
                print("Check-In Time: " + str(check_in_reply.time_res))
                print("============================")

            elif location_input == "2":
                check_in_request = safe_entry_pb2.Check_In_Request(user_id="2002514",
                                                                   location="Changi Village Hawker Centre",
                                                                   date=current_date, time=current_time)
                check_in_reply = stub.Check_In(check_in_request)
                print("=== Check-In Information ===")
                print("Check-In Location: " + str(check_in_reply.location_res))
                print("Check-In Date: " + str(check_in_reply.date_res))
                print("Check-In Time: " + str(check_in_reply.time_res))
                print("============================")

            elif location_input == "3":
                check_in_request = safe_entry_pb2.Check_In_Request(user_id="2002514", location="Whitesands Mall",
                                                                   date=current_date, time=current_time)
                check_in_reply = stub.Check_In(check_in_request)
                print("=== Check-In Information ===")
                print("Check-In Location: " + str(check_in_reply.location_res))
                print("Check-In Date: " + str(check_in_reply.date_res))
                print("Check-In Time: " + str(check_in_reply.time_res))
                print("============================")
        else:
            print("Invalid user, restart program")


if __name__ == '__main__':
    logging.basicConfig()
    run()
