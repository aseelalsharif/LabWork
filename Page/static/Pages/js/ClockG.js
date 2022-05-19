var v=setInterval(time,1000)

function time(){ 
 var t=new Date() 
 var time=t.toDateString();
 var time=t.toTimeString();
  document.getElementById("demo1").innerHTML=time;
  document.getElementById("demo1").style.textAlign="left";
  document.getElementById("demo1").style.color="#765d69";
  document.getElementById("demo1").style.fontSize="large";
  document.getElementById("demo").style.padding="45px 0px 75px 100px";


}
