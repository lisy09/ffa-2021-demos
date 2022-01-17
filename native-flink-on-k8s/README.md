# native-flink-on-k8s

## Ref

- [Native Kubernetes Guide in Flink Homepage](https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/resource-providers/native_kubernetes/)
- [Optimizing Apache Flink on Amazon EKS using Amazon EC2 Spot Instances](https://aws.amazon.com/cn/blogs/compute/optimizing-apache-flink-on-amazon-eks-using-amazon-ec2-spot-instances/)

## Why using Application Mode

Flink can be run in different modes such as Session, Application, and Per-Job. The modes differ in cluster lifecycle, resource isolation and execution of the main() method. Flink can run jobs on Kubernetes via Application and Session Modes only.

- Application Mode: This is a lightweight and scalable way to submit an application on Flink and is the preferred way to launch application as it supports better resource isolation. Resource isolation is achieved by running a cluster per job. Once the application shuts down all the Flink components are cleaned up.
- Session Mode: This is a long running Kubernetes deployment of Flink. Multiple applications can be launched on a cluster and the applications competes for the resources. There may be multiple jobs running on a TaskManager in parallel. Its main advantage is that it saves time on spinning up a new Flink cluster for new jobs, however if one of the Task Managers fails it may impact all the jobs running on that

## How to start

```bash
# build demo image
make demo

# deploy with local k8s cluster
make demo-deploy-local

# kubectl login to pod
kubectl exec -it demo-flink-client bash

# in pod run this command
./bin/flink run-application \
    --target kubernetes-application \
    -Dkubernetes.service-account=demo \
    -Dkubernetes.container.image=lisy09/flink-on-k8s-demo:0.1 \
    local:///opt/flink/examples/table/WordCountSQLExample.jar

# clean up
make demo-undeploy
```