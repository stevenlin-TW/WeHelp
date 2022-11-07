// Search Member Data
let search_btn = document.getElementById("search");
search_btn.addEventListener("click", ()=>{
    let username = document.getElementById("username").value;
    console.log(username)
    let url = "http://127.0.0.1:3000/api/member?username=" + username;
    fetch(url, {method: "GET"}).then((response)=>{
        return response.json();
    }).then((data)=>{
        let name = document.getElementById("name");
        console.log(data["data"]);
        name.style.display = "block";
        name.innerHTML = data["data"]["name"] + "(" + username + ")";
        
    });
})

// Rename Username
let update_btn = document.getElementById("update");
update_btn.addEventListener("click", ()=>{
    let url = "http://127.0.0.1:3000/api/member";
    let new_name = document.getElementById("new_name").value;
    header = {
        "Content-Type" : "application/json"
    };
    body = {
        "name" : new_name
    };
    fetch(url, {
        method: "PATCH",
        headers: header,
        body: JSON.stringify(body)
    })
        .then(response => response.json())
        .then((data)=>{
            let update_info = document.getElementById("update_info");
            update_info.innerHTML = "更新成功";
            update_info.style.display = "block";
        })
})