#!/usr/bin/env bash
protoc -I=simple/ --python_out=simple/ simple/simple.proto
protoc -I=enum/ --python_out=enum/ enum/enum_example.proto