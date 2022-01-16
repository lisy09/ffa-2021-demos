ROOT_DIR=${PWD}
SCRIPTS_DIR = ${ROOT_DIR}/scripts

# build

.PHONY: all
all: incremental-tasks alway-run-tasks

.PHONY: incremental-tasks
incremental-tasks: docker-images push

.PHONY: alway-run-tasks  
alway-run-tasks:

.PHONY: docker-images
docker-images: nfs-docker

.PHONY: clean
clean: delete-docker-images

.PHONY: delete-docker-images
delete-docker-images:
	$(SCRIPTS_DIR)/delete_local_images.sh 

.PHONY: nfs-docker
nfs-docker:
	${SCRIPTS_DIR}/build_nfs_docker.sh

.PHONY: push
push:
	$(SCRIPTS_DIR)/push_docker_images.sh 

# deploy
.PHONY: deploy-nfs
deploy-nfs:
	${SCRIPTS_DIR}/deploy_nfs.sh
.PHONY: undeploy-nfs
undeploy-nfs:
	${SCRIPTS_DIR}/undeploy_nfs.sh

.PHONY: deploy-k8s
deploy-k8s:
	${SCRIPTS_DIR}/create_cluster.sh

.PHONY: undeploy-k8s
undeploy-k8s:
	${SCRIPTS_DIR}/delete_cluster.sh

.PHONY: deploy
deploy: deploy-k8s
# deploy: deploy-k8s deploy-nfs

.PHONY: undeploy
undeploy: undeploy-k8s
# undeploy: undeploy-k8s undeploy-nfs

# deploy
.PHONY: deploy-dns
deploy-dns:
	${SCRIPTS_DIR}/deploy_docker_dnsmasq.sh
.PHONY: undeploy-dfs
undeploy-dns:
	${SCRIPTS_DIR}/undeploy_docker_dnsmasq.sh

.PHONY: update-ingress-manifest
update-ingress-manifest:
	${SCRIPTS_DIR}/update_ingress_manifest.sh

.PHONY: install-kubevela
install-kubevela:
	${SCRIPTS_DIR}/install_kubevela.sh

.PHONY: install-observability
install-observability:
	${SCRIPTS_DIR}/install_observability.sh