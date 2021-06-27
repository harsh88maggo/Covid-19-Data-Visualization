
var g=0;

 function Submit()
 {
     if(g==0)
     {
         alert("You might have COVID 19!! Consult a Doctor!");
     }
     else if(g==4)
     {
         alert("CHILL!! Out of Danger"); 
     }
     else
     {
         alert("Mild chance of having COVID 19!")
     }
 }
 function checkAnswer()
 {
     g=g+1;   
 }

