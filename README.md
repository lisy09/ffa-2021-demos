# ffa-2021-demos

This repo summarizes several demos from Flink Forward Asia 2021.

## demos

- [Native Flink on k8s](.)
- [AIFlow](.)
- [Alink](.)
- [Incremental Training](.)

## Prerequisite

- The environemnt for build needs [docker engine installed](https://docs.docker.com/engine/install/)
- have [docker-compose](https://docs.docker.com/compose/install/) installed
- The environemnt for build needs GNU `make` > 3.8 installed
- The environemnt for build needs `bash` shell
- An available k8s cluster (e.g. k8s cluster in Docker Desktop), or using [kind](https://kind.sigs.k8s.io/) to setup local k8s cluster in docker containers
- k8s related cli installed
  - `kubectl`
  - `helm` (>= 3.0)

### Installing kind cli for using local k8s cluster with kind

On Linux:

```bash
curl -Lo ./kind "https://kind.sigs.k8s.io/dl/v0.11.1/kind-$(uname)-amd64"
chmod +x ./kind
mv ./kind /some-dir-in-your-PATH/kind
```

On macOS via Homebrew:

```bash
brew install kind
```

## Create/Destroy local k8s cluster with kind

```bash
make local-k8s
make local-k8s-undeploy
```

## Validating there is an available k8s cluster

```bash
kubectl get node
```