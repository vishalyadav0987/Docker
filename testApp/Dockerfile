FROM node:20
# When we using like that 
# it we specify any version of node



# FROM node  
# It here i am using latest version of node Image
# In docker hub platform lots image lots of version 
# Present of node image



WORKDIR /myapp
# It's mean create working directory in container
# we know lots of isoltaed also there



# COPY source dest
COPY . .
# Copy whole in myapp work directory 
# 1st dot -- means testApp[souce]
# 2nd dot -- means myapp[destination]



RUN npm install
# We know when deploy any sofware on open we remove the node_mod



EXPOSE 5173
# (Optional)
#  Here we write coorect port ki hamara App kis PORT pe run kar raha hai



CMD ["npm","run","dev"]
# We here only create docker so not direct run the npm i command
# That why we are using CMD [ "executable" ] executable tool


