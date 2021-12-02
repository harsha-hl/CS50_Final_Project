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

  let choice1 = document.querySelectorAll(".crocs");
  for(let i =0; i<choice1.length; i++)
  {
    choice1[i].addEventListener("click",function(){
      localStorage.setItem("type", "Crocs");
      localStorage.setItem("brand", "Crocs");
    });
  }

  let choice2 = document.querySelectorAll(".sneakers");
  for(let i =0; i<choice2.length; i++)
  {
    choice2[i].addEventListener("click",function(){
      alert("Nike");
      localStorage.setItem("type", "Sneakers");
    });
  }

  let choice3 = document.querySelectorAll(".sports");
  for(let i =0; i<choice3.length; i++)
  {
    choice3[i].addEventListener("click",function(){
      localStorage.setItem("type", "Sports");
    });
  }

  let choice4 = document.querySelectorAll(".nike");
  for(let i =0; i<choice4.length; i++)
  {
    choice4[i].addEventListener("click",function(){
      localStorage.setItem("brand", "Nike");
    });
  }

  let choice5 = document.querySelectorAll(".adidas");
  for(let i =0; i<choice5.length; i++)
  {
    choice5[i].addEventListener("click",function(){
      alert("Adidas");
      localStorage.setItem("brand", "Adidas");
    });
  }

  let images = document.querySelectorAll(".imagel");
  for(let i = 0; i < images.length; i++)
  {
    images[i].addEventListener("click",function(){
      let tmp = images[i].getAttribute("src");
      localStorage.setItem("source", tmp);
      console.log("hello")
      let cat ="";
      if(tmp.includes("nikeSneakers"))cat = "Nike / Sneakers";
      else if(tmp.includes("nikeSports"))cat = "Nike / Sports";
      else if(tmp.includes("adidasSneakers"))cat = "Adidas / Sneakers";
      else if(tmp.includes("adidasSports"))cat = "Adidas / Sports";
      else cat = "Crocs";
      
      let z = "";
      let x = tmp.substring(tmp.lastIndexOf("/")+1,tmp.lastIndexOf("."));
      if(x.charAt(4)>= '0' && x.charAt(4)<= '9')
      {
        z+= x.substring(0,5);
        x = x.substring(5);
        
      } 
      else
      {
        z+= x.substring(0,4);
        x= x.substring(4);
      } 
      let y = "";
      y+= x[0].toUpperCase();
      for(let i=1;x[i];i++)
      {
        if(x[i] == '_' || x[i] == '-' || x[i] == ' ')
        {
          y+= ' ' + x[++i].toUpperCase();
        }
        else y+= x[i];
      }
      localStorage.setItem("price", z);
      localStorage.setItem("category", cat);
      localStorage.setItem("name", y);
      tmp = tmp.replace(/.([^.]*)$/, "1." + '$1');
      localStorage.setItem("source1", tmp);
    });
    
  }              
});