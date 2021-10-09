document.addEventListener("DOMContentLoaded", function()
            { 
                var prevScrollpos = window.pageYOffset;
                window.onscroll = function() {
                var currentScrollPos = window.pageYOffset;
                  if (prevScrollpos > currentScrollPos) {
                    document.getElementById("xyz").style.top = "0";
                  } else {
                    document.getElementById("xyz").style.top = "-60px";
                  }
                  prevScrollpos = currentScrollPos;
                }
                
            });