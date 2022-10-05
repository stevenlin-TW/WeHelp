fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then((response)=>{
    return response.json();
}).then((data)=>{
    //console.log(data);
    // data.result.results[]
    for(let pic_num=1;pic_num<43;pic_num++){
        let url_string = data.result.results[pic_num-1].file;
        //console.log(url_string.length);
        let url_length = data.result.results[pic_num-1].file.length;
        var end_index = 0;
        for(let i=0;i<url_length;i++){
            if(url_string.substr(i,2) == 'gh' || url_string.substr(i,2) == 'Gh'){
                end_index = i+1;
                break;
            }
        };
        let pic_url = url_string.substring(0,end_index);
        //console.log(pic_url);
        //console.log("site" + pic_num.toString() + "_pic")
        const site_pic = document.createElement("img");
        site_pic.src = pic_url;
        const site_title = document.createElement("div");
        site_title.innerText = data.result.results[pic_num-1].stitle;
        
        if(pic_num<=2){
            //site_pic.style = "width: 80px;height: 50px;object-fit: cover"
            site_title.className = "title_text";
        }else{
            //site_pic.style = "width: 100%;object-fit: cover;z-index: -1"
            site_title.className = "row_title";
        }
        
        document.getElementById("site" + pic_num.toString() + "_pic").appendChild(site_pic);
        document.getElementById("site" + pic_num.toString()).appendChild(site_title);
    }
});

let i = 0;
const btn = document.getElementById("load_more");
btn.addEventListener("click", function(){
    if(i==0){
        let main2 = document.querySelectorAll(".main2");
        console.log(main2.length)
        for(let j=0;j<main2.length;j++){
            main2[j].style.display = "flex";
        };
    }else if(i==1){
        let main3 = document.querySelectorAll(".main3");
        for(let j=0;j<main3.length;j++){
            main3[j].style.display = "flex";
        };
    }else if(i==2){
        let main4 = document.querySelectorAll(".main4");
        for(let j=0;j<main4.length;j++){
            main4[j].style.display = "flex";
        };
    }else{
        let main5 = document.querySelectorAll(".main5");
        for(let j=0;j<main5.length;j++){
            main5[j].style.display = "flex";
        };
        document.querySelector(".btn").style.display = "none";
    }
    i += 1;
});



