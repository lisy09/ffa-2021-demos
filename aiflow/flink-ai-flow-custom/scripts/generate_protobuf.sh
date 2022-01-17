#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly AIFLOW_DIR=$ROOT_DIR/ai_flow
source $ROOT_DIR/.env

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)    machine=Linux;;
    Darwin*)   machine=Mac;;
    *)         machine="UNKNOWN:${unameOut}"
esac
echo "Running on machine: ${machine}"

SED=sed
if [ "$machine" = "Mac" ]; then
    SED=gsed
fi

COMMANDS=docker,$SED
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

readonly SRC_DIR=$AIFLOW_DIR/protobuf/proto
readonly WORKSPACE_DIR=/workspace
readonly OUTPUT_DIR=/output

set -e
set -x

readonly GOLANG_OUTPUT_DIR=$AIFLOW_DIR/protobuf/go
rm -rf ${GOLANG_OUTPUT_DIR}
mkdir -p ${GOLANG_OUTPUT_DIR}
cmd="docker run --rm \
    --user=1000:1000 \
    -v $SRC_DIR:$WORKSPACE_DIR \
    -v $GOLANG_OUTPUT_DIR:$OUTPUT_DIR \
    ${PROTOBUF_IMAGE_FULL} \
    -I$WORKSPACE_DIR"
$cmd \
    --go_out=Mgoogle/api/annotations.proto=github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis/google/api,plugins=grpc:${OUTPUT_DIR} \
    $WORKSPACE_DIR/message.proto
$cmd \
    --go_out=Mgoogle/api/annotations.proto=github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis/google/api,plugins=grpc:${OUTPUT_DIR} \
    $WORKSPACE_DIR/*_service.proto
$cmd \
    --grpc-gateway_out=logtostderr=true:${OUTPUT_DIR} \
    $WORKSPACE_DIR/*_service.proto
readonly GOLANG_OUTPUT_SRC_DIR=$GOLANG_OUTPUT_DIR/ai_flow
$SED -i -E 's/\_ "github.com\/grpc-ecosystem\/grpc-gateway\/third_party\/googleapis\/google\/api"/\/\/\_ "github.com\/grpc-ecosystem\/grpc-gateway\/third_party\/googleapis\/google\/api"/g' ${GOLANG_OUTPUT_SRC_DIR}/metadata_service.pb.go
$SED -i -E 's/\_ "github.com\/grpc-ecosystem\/grpc-gateway\/third_party\/googleapis\/google\/api"/\/\/\_ "github.com\/grpc-ecosystem\/grpc-gateway\/third_party\/googleapis\/google\/api"/g' ${GOLANG_OUTPUT_SRC_DIR}/model_center_service.pb.go
$SED -i -E 's/\_ "github.com\/grpc-ecosystem\/grpc-gateway\/third_party\/googleapis\/google\/api"/\/\/\_ "github.com\/grpc-ecosystem\/grpc-gateway\/third_party\/googleapis\/google\/api"/g' ${GOLANG_OUTPUT_SRC_DIR}/scheduling_service.pb.go
$SED -i -E 's/\_ "github.com\/grpc-ecosystem\/grpc-gateway\/third_party\/googleapis\/google\/api"/\/\/\_ "github.com\/grpc-ecosystem\/grpc-gateway\/third_party\/googleapis\/google\/api"/g' ${GOLANG_OUTPUT_SRC_DIR}/metric_service.pb.go
cd $GOLANG_OUTPUT_SRC_DIR \
    && go mod init flink-ai-flow/protobuf \
    && go get


readonly JAVA_OUTPUT_DIR=$AIFLOW_DIR/java/client/src/main/java
readonly JAVA_PROTO_DIR=$JAVA_OUTPUT_DIR/com/aiflow/proto
rm -rf ${JAVA_PROTO_DIR}
mkdir -p ${JAVA_OUTPUT_DIR}
cmd="docker run --rm \
    --user=1000:1000 \
    -v $SRC_DIR:$WORKSPACE_DIR \
    -v $JAVA_OUTPUT_DIR:$OUTPUT_DIR \
    ${PROTOBUF_IMAGE_FULL} \
    -I$WORKSPACE_DIR"
$cmd \
    --java_out=$OUTPUT_DIR \
    $WORKSPACE_DIR/message.proto
$cmd \
    --java_out=$OUTPUT_DIR \
    $WORKSPACE_DIR/metadata_service.proto
$cmd \
    --grpc-java_out=$OUTPUT_DIR \
    $WORKSPACE_DIR/metadata_service.proto
$cmd \
    --java_out=$OUTPUT_DIR \
    $WORKSPACE_DIR/model_center_service.proto
$cmd \
    --grpc-java_out=$OUTPUT_DIR \
    $WORKSPACE_DIR/model_center_service.proto


readonly PYTHON_OUTPUT_DIR=$AIFLOW_DIR/protobuf
# rm -rf ${PYTHON_OUTPUT_DIR}
# mkdir -p ${PYTHON_OUTPUT_DIR}
# touch ${PYTHON_OUTPUT_DIR}/__init__.py
cmd="docker run --rm \
    --user=1000:1000 \
    -v $SRC_DIR:$WORKSPACE_DIR \
    -v $PYTHON_OUTPUT_DIR:$OUTPUT_DIR \
    ${PROTOBUF_IMAGE_FULL} \
    -I$WORKSPACE_DIR"
$cmd \
    --python_out=$OUTPUT_DIR \
    --mypy_out=$OUTPUT_DIR \
    $WORKSPACE_DIR/message.proto
$cmd \
    --python_out=$OUTPUT_DIR \
    --mypy_out=$OUTPUT_DIR \
    --grpc-python_out=$OUTPUT_DIR \
    $WORKSPACE_DIR/*_service.proto
$cmd \
    --python_out=$OUTPUT_DIR \
    --mypy_out=$OUTPUT_DIR \
    --grpc-python_out=$OUTPUT_DIR \
    $WORKSPACE_DIR/high_availability.proto

$SED -i -E 's/^import message_pb2 as message__pb2/from . import message_pb2 as message__pb2/' ${PYTHON_OUTPUT_DIR}/*pb2*.py
$SED -i -E 's/^import metadata_service_pb2 as metadata__service__pb2/from . import metadata_service_pb2 as metadata__service__pb2/' ${PYTHON_OUTPUT_DIR}/*pb2*.py
$SED -i -E 's/^import model_center_service_pb2 as model__center__service__pb2/from . import model_center_service_pb2 as model__center__service__pb2/' ${PYTHON_OUTPUT_DIR}/*pb2*.py
$SED -i -E 's/^import scheduling_service_pb2 as scheduling__service__pb2/from . import scheduling_service_pb2 as scheduling__service__pb2/' ${PYTHON_OUTPUT_DIR}/*pb2*.py
$SED -i -E 's/^import metric_service_pb2 as metric__service__pb2/from . import metric_service_pb2 as metric__service__pb2/' ${PYTHON_OUTPUT_DIR}/*pb2*.py
$SED -i -E 's/^import high_availability_pb2 as high__availability__pb2/from . import high_availability_pb2 as high__availability__pb2/' ${PYTHON_OUTPUT_DIR}/*pb2*.py

# add licence
current_dir=$AIFLOW_DIR/protobuf
java_dir=${current_dir}/../java/client/src/main/java/org/aiflow/client/proto
go_dir=${current_dir}/go/ai_flow
# Add licenses to generated python files
for i in ${current_dir}/*.py
do
   if ! [[ $i == *"__init__"* ]]; then
     $SED -i -e '1i \
#\
# Licensed to the Apache Software Foundation (ASF) under one\
# or more contributor license agreements.  See the NOTICE file\
# distributed with this work for additional information\
# regarding copyright ownership.  The ASF licenses this file\
# to you under the Apache License, Version 2.0 (the\
# "License"); you may not use this file except in compliance\
# with the License.  You may obtain a copy of the License at\
#\
#   http://www.apache.org/licenses/LICENSE-2.0\
#\
# Unless required by applicable law or agreed to in writing,\
# software distributed under the License is distributed on an\
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\
# KIND, either express or implied.  See the License for the\
# specific language governing permissions and limitations\
# under the License.\
#\
' $i
   fi

done

# Add licenses to generated java files
for i in ${java_dir}/*.java
do
   $SED -i -e '1i \
/*\
\ * Licensed to the Apache Software Foundation (ASF) under one\
\ * or more contributor license agreements.  See the NOTICE file\
\ * distributed with this work for additional information\
\ * regarding copyright ownership.  The ASF licenses this file\
\ * to you under the Apache License, Version 2.0 (the\
\ * "License"); you may not use this file except in compliance\
\ * with the License.  You may obtain a copy of the License at\
\ *\
\ *   http://www.apache.org/licenses/LICENSE-2.0\
\ *\
\ * Unless required by applicable law or agreed to in writing,\
\ * software distributed under the License is distributed on an\
\ * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\
\ * KIND, either express or implied.  See the License for the\
\ * specific language governing permissions and limitations\
\ * under the License.\
\ */
' $i
done


# Add licenses to generated go files
for i in ${go_dir}/*.gw.go
do
   $SED -i -e '1i \
//\
// Licensed to the Apache Software Foundation (ASF) under one\
// or more contributor license agreements.  See the NOTICE file\
// distributed with this work for additional information\
// regarding copyright ownership.  The ASF licenses this file\
// to you under the Apache License, Version 2.0 (the\
// "License"); you may not use this file except in compliance\
// with the License.  You may obtain a copy of the License at\
//\
//     http://www.apache.org/licenses/LICENSE-2.0\
//\
// Unless required by applicable law or agreed to in writing, software\
// distributed under the License is distributed on an "AS IS" BASIS,\
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\
// See the License for the specific language governing permissions and\
// limitations under the License.\
' $i
done


