const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());

// Connect to MongoDB on host machine
mongoose.connect("mongodb://atlas-local:27017/testdb", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log("Connected to MongoDB on host machine!");
}).catch((err) => {
    console.error("MongoDB connection error:", err);
});

// Simple API
app.get("/", (req, res) => {
    res.send("Hello from Dockerized Node.js backend!");
});

app.listen(5000, () => {
    console.log("Server running on port 5000");
});
