ROOT_DIR=${PWD}
SCRIPTS_DIR = ${ROOT_DIR}/scripts

.PHONY: all
all: incremental-tasks alway-run-tasks

.PHONY: incremental-tasks
incremental-tasks: docker-images

.PHONY: alway-run-tasks  
alway-run-tasks: 

.PHONY: docker-images
docker-images: demo

.PHONY: demo
demo:
	$(SCRIPTS_DIR)/build_image.sh -p DEMO

.PHONY: demo-deploy-local-load
demo-deploy-local-load:
	$(SCRIPTS_DIR)/load_images_to_local_cluster.sh

.PHONY: demo-deploy
demo-deploy:
	$(SCRIPTS_DIR)/deploy_demo.sh

.PHONY: demo-deploy-local
demo-deploy-local: demo-deploy-local-load demo-deploy

.PHONY: demo-undeploy
demo-undeploy:
	$(SCRIPTS_DIR)/undeploy_demo.sh

