document.getElementById("loginButton").addEventListener("click", function () {
    // Backend API URL (Make sure ALB listens on HTTP, not port 5000)
    const backendURL = "http://backendlb-1940925447.ap-south-1.elb.amazonaws.com/booksawindex.html";  // Replace with actual ALB DNS

    fetch(backendURL, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok " + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        if (data.username && data.email) {
            window.open(backendURL, '_self');
        } else {
            document.getElementById("response").innerText = "No user data found!";
        }
    })
    .catch(error => {
        console.error("Error fetching data:", error);
        document.getElementById("response").innerText = "Failed to load data!";
    });
});
