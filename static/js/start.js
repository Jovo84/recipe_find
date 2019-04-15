console.log("test");

let browseButtonElement=document.querySelector('.dropButton');
if (browseButtonElement){
    browseButtonElement.addEventListener("click", function(){
        console.log("button clicked");
        let browseMenuElement=document.querySelector('#browseMenu');
        if(browseMenuElement.classList.contains("hide")){
            browseMenuElement.classList.remove("hide");
        } else {
            browseMenuElement.classList.add("hide");
        }
    });
}



let favHolder=document.querySelectorAll(".fav-holder");
if (favHolder){
    for (let i = 0; i < favHolder.length; i++) {
        favHolder[i].addEventListener("click", function(e){
            console.log(e.target);
            if(e.target.getAttribute('alt')=='fav-empty'){
                let holder = e.target.parentElement;
                e.target.classList.add('hide');
                holder.querySelector('[alt="fav-full"]').classList.remove("hide");
            }else{
                e.target.querySelector('[alt="fav-empty"]').classList.add("hide")
                e.target.querySelector('[alt="fav-full"]').classList.remove("hide")
            }
        });
    }
}
