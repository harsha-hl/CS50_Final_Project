document.addEventListener("DOMContentLoaded", function(){
  var prevScrollpos = window.pageYOffset;
  window.onscroll = function(){
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
      document.getElementById("xyz").style.top = "0";
    }
    else{
      document.getElementById("xyz").style.top = "-60px";
    }
    prevScrollpos = currentScrollPos;
  }

  let images = document.querySelectorAll(".imagel");
  for(let i = 0; i < images.length; i++)
  {
    images[i].addEventListener("click",function(){
      let tmp = images[i].getAttribute("src");
      localStorage.setItem("source", tmp);
      
      let flag;
      print(tmp)
if(tmp.includes("nikeSneakers"))flag = "Nike / Sneakers";
else if(tmp.includes("nikeSports"))flag = "Nike / Sports";
else if(tmp.includes("adidasSneakers"))flag = "Adidas / Sneakers";
else if(tmp.includes("adidasSports"))flag = "Adidas / Sports";
else flag = "Crocs";


let f = tmp.substring(tmp.lastIndexOf("/")+1,tmp.indexOf("."));
f = f.replace(/-/g, ' ');
let y="";
y = y+f[0].toUpperCase()
for(var i=1;i<f.length;i++)
{
    if(f[i]==' ')
    {y = y+" "+f[i+1].toUpperCase()
    i = i+1
    }
    else y = y + f[i]
}
localStorage.setItem("c", flag);
localStorage.setItem("n", y);
tmp = tmp.replace(".","1.");
      localStorage.setItem("source1", tmp);
    });
    
  }              
});