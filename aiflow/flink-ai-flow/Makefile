ROOT_DIR=${PWD}
SCRIPTS_DIR = ${ROOT_DIR}/scripts

.PHONY: all
all: incremental-tasks alway-run-tasks

.PHONY: incremental-tasks
incremental-tasks: docker-images push

.PHONY: alway-run-tasks  
alway-run-tasks: 

.PHONY: docker-images
docker-images: devbase dev base

.PHONY: devbase
devbase:
	$(SCRIPTS_DIR)/build_dev_base.sh
.PHONY: dev
dev:
	$(SCRIPTS_DIR)/build_dev.sh
.PHONY: dev-deploy
dev-deploy:
	$(SCRIPTS_DIR)/deploy_dev.sh
.PHONY: dev-undeploy
dev-undeploy:
	$(SCRIPTS_DIR)/undeploy_dev.sh

.PHONY: base
base:
	$(SCRIPTS_DIR)/build_base.sh
.PHONY: base-deploy
base-deploy:
	$(SCRIPTS_DIR)/deploy_base.sh
.PHONY: base-undeploy
base-undeploy:
	$(SCRIPTS_DIR)/undeploy_base.sh

.PHONY: clean
clean: delete-docker-images

.PHONY: delete-docker-images
delete-docker-images:
	$(SCRIPTS_DIR)/delete_local_images.sh 

.PHONY: push
push:
	$(SCRIPTS_DIR)/push_docker_images.sh 

.PHONY: install-local
install-local:
	$(SCRIPTS_DIR)/install_local.sh 

.PHONY: test
test:
	$(SCRIPTS_DIR)/test_local.sh
# .PHONY: test-exit
# test-exit:
# 	$(SCRIPTS_DIR)/test_local.sh -x
# .PHONY: test-debug
# test-debug:
# 	$(SCRIPTS_DIR)/test_local.sh -d
# .PHONY: it-test
# it-test:
# 	$(SCRIPTS_DIR)/test_integration_local.sh
# .PHONY: coverage
# coverage:
# 	$(SCRIPTS_DIR)/test_local.sh -c

# .PHONY: test-notification-local
# test-notification-local:
# 	$(SCRIPTS_DIR)/test_notification_local.sh

.PHONY: protobuf
protobuf: protobuf-aiflow protobuf-notification

.PHONY: protobuf-aiflow
protobuf-aiflow:
	$(SCRIPTS_DIR)/generate_protobuf.sh 
.PHONY: protobuf-notification
protobuf-notification:
	$(SCRIPTS_DIR)/generate_protobuf_notification_service.sh 

.PHONY: start-local
start-local:
	$(SCRIPTS_DIR)/start_aiflow_in_dev_container.sh
.PHONY: stop-local
stop-local:
	stop-all-aiflow-services.sh
	
# .PHONY: docs
# docs:
# 	cd ${ROOT_DIR}/docs && ./docgen.sh && make clean html
# 	cd ${ROOT_DIR}/docs && ./docgen.sh


AIFLOW_FLINK_HIVE_SCRIPT_DIR = ${ROOT_DIR}/docker/aiflow-flink-hive/scripts
.PHONY: aiflow-flink-hive
aiflow-flink-hive:
	${AIFLOW_FLINK_HIVE_SCRIPT_DIR}/build_images.sh
.PHONY: aiflow-flink-hive-deploy
aiflow-flink-hive-deploy:
	${AIFLOW_FLINK_HIVE_SCRIPT_DIR}/deploy.sh
.PHONY: aiflow-flink-hive-undeploy
aiflow-flink-hive-undeploy:
	${AIFLOW_FLINK_HIVE_SCRIPT_DIR}/undeploy.sh

.PHONY: aiflow-flink-hive-dev-deploy
aiflow-flink-hive-dev-deploy:
	${AIFLOW_FLINK_HIVE_SCRIPT_DIR}/deploy_dev.sh
.PHONY: aiflow-flink-hive-dev-undeploy
aiflow-flink-hive-dev-undeploy:
	${AIFLOW_FLINK_HIVE_SCRIPT_DIR}/undeploy_dev.sh

TIDB_SCRIPT_DIR = ${ROOT_DIR}/docker/tidb/scripts
.PHONY: tidb-deploy
tidb-deploy:
	${TIDB_SCRIPT_DIR}/deploy.sh
.PHONY: tidb-undeploy
tidb-undeploy:
	${TIDB_SCRIPT_DIR}/undeploy.sh