fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then((response)=>{
    return response.json();
}).then((data)=>{
    console.log(data);
    // data.result.results[]
    for(var pic_num=1;pic_num<11;pic_num++){
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
    
    let main_num = 2;
    let main_pic_num = 2;
    const btn = document.getElementById("load_more");
    btn.addEventListener("click", ()=>{
        (()=>{
            for(let i = 0; i<2; i++){
                let main = document.createElement("div");
                main.className = "main";
                main.id = "main" + main_num.toString();
                main_top = document.getElementById("main" + (main_num-1).toString());
                main_top.parentNode.insertBefore(main, main_top.nextSibling);

                let main_pic = document.createElement("div");
                main_pic.className = "main_pic";
                main_pic.id = "main_pic" + main_pic_num.toString();
                document.getElementById(main.id).appendChild(main_pic);

                var first_num = 1;
                for(var num=pic_num;num<pic_num+4;num++){
                    if(num > data.result.results.length){
                        btn.style.display = "none";
                        return;
                    }else{            
                        let box = document.createElement("div");
                        box.className = "first" + first_num.toString();
                        box.id = "site" + num.toString();
                        document.getElementById(main_pic.id).appendChild(box);

                        let pic_box = document.createElement("div");
                        pic_box.className = "row_pic";
                        pic_box.id = "site" + num.toString() + "_pic";
                        document.getElementById(box.id).appendChild(pic_box);
                        
                        let url_string = data.result.results[num-1].file;
                        //console.log(url_string.length);
                        let url_length = data.result.results[num-1].file.length;
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
                        site_title.innerText = data.result.results[num-1].stitle;
                        site_title.className = "row_title";
                        
                        document.getElementById("site" + num.toString() + "_pic").appendChild(site_pic);
                        document.getElementById("site" + num.toString()).appendChild(site_title);


                        let star = document.createElement("div");
                        star.className = "star";
                        star.id = "star" + num.toString();
                        document.getElementById(box.id).appendChild(star)

                        let star_pic = document.createElement("img");
                        star_pic.src = "https://stevenlin-tw.github.io/WeHelp/star.png";
                        document.getElementById(star.id).appendChild(star_pic)
                        first_num += 1;
                    };
                };
                pic_num = num;
                if(pic_num > data.result.results.length){
                    btn.style.display = "none";
                    return;
                };
                main_num += 1;
                main_pic_num += 1;
            };
        })();
    });
});