# Docker

**Step 1: Create Dockerfile**
- Creating Docker file with same name "**Dockerfile**"

**Step 2: Creating Docker Image**
```
docker build .
```
- **Result ✅**

```
writing image sha256:163c56b07d4b80c15ed9025c276c3114df01d2fffba887ae 
```
**Step 3: List of Docker Images**
- For checking image:

```
docker image ls
```
- **Result ✅**

| REPOSITORY | TAG | IMAGE ID | CREATED | SIZE |
|--------------|-------------|--------------|-------------|------------|
| none | none | 163c56b07d4b | 44 seconds ago | 1.16GB |
                 
**Step 4: Run and Manage docker container**
- Creating container:
```
docker run <imageId>
```

- **Result ☑️**
```
testapp@0.0.0 dev
> vite


  VITE v7.1.2  ready in 178 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose

This site can’t be reached
```

- **(Question)** Why these **This site can’t be reached** the message show when we going to **http://localhost:5173** that **Expose 5173** is assign in docker file?


- **(Answer)** This error occurs because Docker containers run in an isolated environment. In the Dockerfile, `EXPOSE 5173` only informs that the application inside the container will use port 5173, but it does not automatically make it accessible from the host machine.
When you run `docker run {imageId}`, the application is running inside the container on port 3000, but your host system cannot reach it directly. To access it from your browser at `http://localhost:5173`, 

---

### you need to publish the port using:

- **Port Binding For Accessing site in outside the container**

- **Left side (5173)** = port on your host machine (MacBook in your case).

- **Right side (5173)** = port inside the container where the app is running.

```
docker run -p <which PORT>:<Expose PORT> <imageId>
```
---

### 🖼️ Simple analogy:

- **localhost only:** “Main sirf apne ghar ke andar ki baatein sununga.”

- **0.0.0.0:** “Main sabhi darwaazon pe baatein sununga, chaahe padosi ya bahar se koi aaye.”


---
### Process state:
- **For Checking which process is running [The (docker ps) command only shows containers that are in the running state.]** 
```
docker ps
```
- **Result ✅**

| CONTAINER ID | IMAGE ID | COMMAND | CREATED | STATUS | PORTS | NAMES |
|--------------|-------------|--------------|-------------|------------|------------|------------|
| 5feefd9d375a | b82aff127418 | docker-entrypoint.s… | 19 seconds ago | Up 19 minutes | 0.0.0.0:5173->5173/tcp, [::]:5173->5173/tcp | adoring_cohen |

---
- **And How to stop**
```
docker stop <NAMES>
```
---

### 🏃 Running container in detached mode:
- Detached Mode is useful for running application in background without stuck terminal at same point.
- Detached Mode ka use application ko background me run karne ke liye hota hai, taaki terminal busy na ho.
- Is mode me container background me run karta hai aur aapka terminal free rehta hai.

```
docker run -d -p 5173:5173 <imageId>
```

- **Result ✅**
```
d81c1717adc694f40297e43bd9adfdd14467048926d09387f88955f2546b0d13
```


---

### 🏃 Running Mutiple Container/Application with single Image:
**My Container 1 Running PORT At 5173 And We Listen on Machine 5173**
- **When we listen again same PORT:**
```
docker run -d -p 5173:5173 b82aff127418
```
- **Result ❌**
```
docker: Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint admiring_raman (9bfbe510fc2f1fc47a8116fd8bf3c7d5b662a82e5e21a2e16bf7f4573710c37f): Bind for 0.0.0.0:5173 failed: port is already allocated

Run 'docker run --help' for more information

NOTE: These response in you PC alread PORT 5173 in used.
```

- **(Question) So how we create mutiple container with same image ?**
- **(Answer) We run the Container 2 PORT At 5173 And We Listen on Machine with (Differet PORT) 3000**

**Container 2**
```
docker run -d -p 3000:5173 b82aff127418
```
- **Result ✅**
```
912bf56e56e49ee77f34d7ea5a4810f36a74661d86903978521ef5744a03bec7
```

**Container 3**
```
docker run -d -p 4000:5173 b82aff127418
```
- **Result ✅**
```
1b000d819425de59be94a8e125b2e5f0fc50792ccb824ced09801a1b2b0d7c6d
```

---

### 🐳 Here we come to the advantages of DOCKER and the proof that every container has an isolated env:
- We can run multiple containers from a single image.
- Here we also say that **container 1**, **container 2**, **container 3** run on same port that **is not possible if container is not isolated Environment.**.
- For example, **Container 1**, **Container 2**, and **Container 3** **can run independently**. **They cannot use the same port on the same host, but because containers are isolated environments**, they can still run without conflict (by mapping to different host ports).
- Running multiple containers from the same image can also help in **load balancing** for websites.

---

### Process state status:
- **The (docker ps -a) command shows all containers, including those in running, exited, and created states.**
```
docker ps -a
```
- **Result ✅**

| CONTAINER ID | IMAGE ID | COMMAND | CREATED | STATUS | PORTS | NAMES |
|--------------|-------------|--------------|-------------|------------|------------|------------|
| ec9e210d867c | b82aff127418 | docker-entrypoint.s… | 12 hours ago | Created | 0.0.0.0:5173->5173/tcp, [::]:5173->5173/tcp | adoring_cohen |
| 912bf56e56e4 | b82aff127418 | docker-entrypoint.s… | 12 hours ago | Running | 0.0.0.0:5173->5173/tcp, [::]:5173->5173/tcp | adoring_cohen |
| 1b000d819425 | b82aff127418 | docker-entrypoint.s… | 12 hours ago | Running | 0.0.0.0:5173->5173/tcp, [::]:5173->5173/tcp | adoring_cohen |
| 5feefd9d375a | b82aff127418 | docker-entrypoint.s… | 13 hours ago | Exited | 0.0.0.0:5173->5173/tcp, [::]:5173->5173/tcp | adoring_cohen |

---

### 🗑️ Removing Docker containers that are in the **(Created)** or **(Exited)** state:
- **Removing a (single) Docker container in Created or Exited state:**
```
docker rm <Names>
```
- **Result ✅**
```
admiring_raman
```
- **Removing a (multiple) Docker container in Created or Exited state:**
```
docker rm <Names> <Names> <Names> <Names>....
```
- **Result ✅**
```
brave_haibt
boring_rubin
adoring_cohen
```

---

### 🗑️ Automatically removing a container when it is in the Exited state:
- **These containers only run until they are stopped. If I stop one, it is automatically removed.**
```
docker run -d --rm -p 4000:5173 <imageId>
```
- **Result ✅**
```
80b50976e8cd81dbce4d03984284c3b991cfd56d343bbe9941389ad9ea358557
```

---

### Naming the Container:
- By default, Docker gives containers a random name **(like adoring_cohen).**
```
docker run -d --rm --name "myWebApp" -p 4000:5173 <imageId>
```
- **Result ✅**
```
80b50976e8cd81dbce4d03984284c3b991cfd56d343bbe9941389ad9ea358557
```
- **With the help of the container name, we can remove the container.**
```
docker rm 'myWebApp'
```
- **Result ✅**
```
myWebApp
```
---

### 🏹 Managing Docker Images
- **Giving Name to the (image) repo and (taging) to the image:**
```
docker build -t myfirstimage:01 .
docker build -t <repo_name>:<tag> .
```

- **Note(1):** . dot means jis directory me Dockerfile present hai.
- **Note(2):** repository name must be lowercase.
- **Result ✅**
```
writing image sha256:b82aff12741884d5716d5a9fa275a9f7a089d3f304d5ec208bf76907b02207f3
naming to docker.io/library/myfirstimage:01
```

- **All Images:**
```
docker image ls
```

- **Result ✅**

| REPOSITORY | TAG | IMAGE ID | CREATED | SIZE |
|--------------|-------------|--------------|-------------|------------|
| myfirstimage | 01 | b82aff127418 | 14 hours ago | 1.16GB |


- **If we create version 2 of that image [b82aff127418]:**
```
docker build -t myfirstimage:02 .
```

- **Result ✅**
```
writing image sha256:b82aff12741884d5716d5a9fa275a9f7a089d3f304d5ec208bf76907b02207f3
naming to docker.io/library/myfirstimage:02
```

```
docker image ls
```

- **Result ✅**

| REPOSITORY | TAG | IMAGE ID | CREATED | SIZE |
|--------------|-------------|--------------|-------------|------------|
| myfirstimage | 01 | b82aff127418 | 14 hours ago | 1.16GB |
| myfirstimage | 02 | b82aff127418 | 14 hours ago | 1.16GB |

**🗑️ For Deleting the image:**
```
docker rmi <repo_name>:<tag>
```

- **Result ✅**
```
Untagged: myfirstimage:02
```

---
