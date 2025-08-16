# Docker

**Step 1: Create Dockerfile**
- Creating Docker file with same name "**Dockerfile**"

**Step 2: Creating Docker Image**
```
docker build .
```
- **Result**

```
writing image sha256:163c56b07d4b80c15ed9025c276c3114df01d2fffba887ae 
```
**Step 3: List of Docker Images**
- For checking image:

```
docker image ls
```
- **Result**

| REPOSITORY | TAG | IMAGE ID | CREATED | SIZE |
|--------------|-------------|--------------|-------------|------------|
| none | none | 163c56b07d4b | 44 seconds ago | 1.16GB |
                 
**Step 4: Run and Manage docker container**
- Creating container:
```
docker run <imageId>
```

- **Result**
```
testapp@0.0.0 dev
> vite


  VITE v7.1.2  ready in 178 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose

This site can’t be reached
```

- **(Question)** Why these **This site can’t be reached** the message show when we going to **http://localhost:3000** that **Expose 3000** is assign in docker file?


- **(Answer)** This error occurs because Docker containers run in an isolated environment. In the Dockerfile, `EXPOSE 3000` only informs that the application inside the container will use port 3000, but it does not automatically make it accessible from the host machine.
When you run `docker run {imageId}`, the application is running inside the container on port 3000, but your host system cannot reach it directly. To access it from your browser at `http://localhost:3000`, you need to publish the port using:


---
