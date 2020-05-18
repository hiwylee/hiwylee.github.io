## OCI Designer Toolkit Usage Guide
* https://github.com/hiwylee/oci-designer-toolkit/blob/master/documentation/Usage.md
* https://www.ateam-oracle.com/introduction-to-okit-the-oci-designer-toolkit
### How to setup
```
sudo yum install  git
git clone -b v0.5.0 --depth 1 https://github.com/oracle/oci-designer-toolkit.git
sudo yum install docker-engine
sudo systemctl start docker
sudo systemctl enable docker

cd oci-designer-toolkit/docker/
./build-docker-image.sh

./start-okit-server.sh

```
