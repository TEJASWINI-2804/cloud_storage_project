import React, { useState } from "react";
import "./App.css";

function App() {
  const BASE_URL = "https://cloud-storage-backend.onrender.com";
  const [token, setToken] = useState("");
  const [file, setFile] = useState(null);
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
  if (!file) {
    alert("Select file first");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

 await fetch(`${BASE_URL}/upload/`, {
  method: "POST",
  headers: {
    Authorization: token
  },
  body: formData,
});

  alert("Uploaded successfully");
};

 const handleSearch = async () => {
  try {
    const res = await fetch(`${BASE_URL}/search/?query=${query}`, {
    headers: {
    Authorization: token
  }
});

    const data = await res.json();
    setResults(data.results);
  } catch (error) {
    console.error("Error:", error);
    alert("Search failed. Check backend.");
  }
};
const handleDelete = async (filename) => {
  try {
    await fetch(`https://cloud-storage-backend.onrender.com/delete/${filename}`, {
      method: "DELETE",
    });

    alert("File deleted");

    // refresh search results
    setResults(results.filter((item) => item.filename !== filename));
  } catch (error) {
    alert("Delete failed");
  }
};

const handleSignup = async () => {
  await fetch("https://cloud-storage-backend.onrender.com/signup", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  alert("Signup successful");
};

const handleLogin = async () => {
  console.log("Login clicked");

  const res = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const data = await res.json();

  console.log("Response:", data);

  if (data.token) {
    setToken(data.token);
    setIsLoggedIn(true);
  } else {
    alert("Login failed");
  }
};
 console.log("App loaded");
 return (

  <div>
    <h1>AI Cloud Storage Dashboard</h1>

    {!isLoggedIn && (
      <div className="login-box">
        <input
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={handleLogin}>Login</button>
        <button onClick={handleSignup}>Signup</button>
      </div>
    )}

    {isLoggedIn && (
      <div>

        {/* Upload */}
        <div className="upload-box">
          <input type="file" onChange={handleFileChange} />
          <button onClick={handleUpload}>Upload</button>
        </div>

        {/* Search */}
        <div className="search-box">
          <input
            type="text"
            placeholder="Search..."
            onChange={(e) => setQuery(e.target.value)}
          />
          <button onClick={handleSearch}>Search</button>
        </div>

        {/* Results */}
        <div className="results">
          {(results || []).map((item, index) => (
            <div key={index}>
              <h3>{item.filename}</h3>

               {/* ✅ ADD THIS IMAGE */}
              <img
                src={`http://cloud-storage-backend.onrender.com/files/${item.filename}`}
                alt="preview"
                width="150"
              />

              <p>{item.tags?.join(", ")}</p>

              <a
                href={`http://cloud-storage-backend.onrender.com/download/${item.filename}`}
                target="_blank"
                rel="noreferrer"
              >
                Download
              </a>

              <button onClick={() => handleDelete(item.filename)}>
                Delete
              </button>
            </div>
          ))}
        </div>

      </div>
    )}
  </div>
);
}

export default App;