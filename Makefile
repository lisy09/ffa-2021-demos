ROOT_DIR=${PWD}

LOCAL_K8S_DIR=${ROOT_DIR}/local-k8s-cluster

.PHONY: local-k8s
local-k8s:
	cd ${LOCAL_K8S_DIR} && make deploy

.PHONY: local-k8s-undeploy
local-k8s-undeploy:
	cd ${LOCAL_K8S_DIR} && make undeploy

.PHONY: local-k8s-kubevela
local-k8s-kubevela:
	cd ${LOCAL_K8S_DIR} && make install-kubevela

.PHONY: local-k8s-observability
local-k8s-observability:
	cd ${LOCAL_K8S_DIR} && make install-observability