from pathlib import Path

ROOT = Path("BrainJuiceOS")

TEMPLATES = ROOT / "templates"
OUTPUT = ROOT / "output"

for folder in [
    ROOT,
    TEMPLATES,
    OUTPUT
]:
    folder.mkdir(
        parents=True,
        exist_ok=True
    )

desktop_html = r'''
<div id="bootScreen">
<pre id="bootLog">
BrainJuiceOS Bootloader
Loading...
</pre>
</div>

<div id="loginScreen">

<div class="loginBox">

<h1>BrainJuiceOS</h1>

<input
id="username"
value="admin">

<input
id="password"
type="password"
value="brainjuice">

<button id="loginBtn">
Login
</button>

</div>

</div>

<div id="desktop">

<div id="dock">

<div class="dockIcon">
🌐
</div>

<div class="dockIcon">
📁
</div>

<div class="dockIcon">
⌨️
</div>

<div class="dockIcon">
⚙️
</div>

<div class="dockIcon">
🛒
</div>

</div>

<div id="desktopIcons">

<div class="desktopIcon">
🌐
<br>
Browser
</div>

<div class="desktopIcon">
📁
<br>
Files
</div>

<div class="desktopIcon">
⌨️
<br>
Terminal
</div>

<div class="desktopIcon">
⚙️
<br>
Settings
</div>

<div class="desktopIcon">
🛒
<br>
Store
</div>

</div>

<div id="windows"></div>

<div id="startMenu">

<h2>
BrainJuiceOS
</h2>

<div class="startItem">
Browser
</div>

<div class="startItem">
Files
</div>

<div class="startItem">
Terminal
</div>

<div class="startItem">
Settings
</div>

<div class="startItem">
Store
</div>

</div>

<div id="taskbar">

<button id="startButton">
Start
</button>

<div id="taskbarApps"></div>

<div id="clock"></div>

</div>

</div>
'''

desktop_css = r'''
html,
body{
margin:0;
width:100%;
height:100%;
overflow:hidden;
font-family:Segoe UI,sans-serif;
}

body{
background:black;
}

#bootScreen{
position:fixed;
inset:0;
background:black;
color:#00ff88;
padding:20px;
font-family:Consolas;
z-index:99999;
}

#loginScreen{
position:fixed;
inset:0;
display:none;
justify-content:center;
align-items:center;
background:
linear-gradient(
135deg,
#111,
#222,
#333
);
}

.loginBox{
width:400px;
background:#1f1f1f;
padding:25px;
border-radius:12px;
color:white;
}

.loginBox input{
width:100%;
padding:10px;
margin-top:10px;
box-sizing:border-box;
}

#desktop{
display:none;
position:fixed;
inset:0;
background:
linear-gradient(
45deg,
#0d1b2a,
#1b263b,
#415a77
);
}

#dock{
position:absolute;
left:0;
top:0;
bottom:40px;
width:64px;
background:rgba(0,0,0,.4);
}

.dockIcon{
height:50px;
display:flex;
align-items:center;
justify-content:center;
font-size:24px;
color:white;
cursor:pointer;
}

#desktopIcons{
margin-left:80px;
margin-top:20px;
color:white;
}

.desktopIcon{
width:80px;
text-align:center;
margin-bottom:20px;
cursor:pointer;
}

#windows{
position:absolute;
inset:0;
}

#taskbar{
position:absolute;
left:0;
right:0;
bottom:0;
height:40px;
background:#111;
display:flex;
align-items:center;
}

#startButton{
width:100px;
height:100%;
}

#taskbarApps{
flex:1;
}

#clock{
width:120px;
text-align:center;
color:white;
}

#startMenu{
position:absolute;
left:0;
bottom:40px;
width:300px;
height:450px;
display:none;
background:#222;
color:white;
padding:10px;
}

.startItem{
padding:10px;
cursor:pointer;
}
'''

desktop_js = r'''
const bootMessages = [

"Loading Kernel",
"Loading Desktop",
"Loading BrainFS",
"Loading Apps",
"Starting Services",
"Boot Complete"

];

let bootIndex = 0;

const bootLog =
document.getElementById(
"bootLog"
);

const bootTimer =
setInterval(()=>{

if(
bootIndex <
bootMessages.length
){

bootLog.textContent +=
"\\n"+
bootMessages[
bootIndex
];

bootIndex++;

}else{

clearInterval(
bootTimer
);

setTimeout(()=>{

document
.getElementById(
"bootScreen"
)
.style.display =
"none";

document
.getElementById(
"loginScreen"
)
.style.display =
"flex";

},1000);

}

},500);

document
.getElementById(
"loginBtn"
)
.onclick=()=>{

const user =
document
.getElementById(
"username"
).value;

const pass =
document
.getElementById(
"password"
).value;

if(
user==="admin" &&
pass==="brainjuice"
){

document
.getElementById(
"loginScreen"
)
.style.display=
"none";

document
.getElementById(
"desktop"
)
.style.display=
"block";

}

};

document
.getElementById(
"startButton"
)
.onclick=()=>{

const menu =
document
.getElementById(
"startMenu"
);

menu.style.display =
menu.style.display
==="block"
?
"none"
:
"block";

};

function updateClock(){

document
.getElementById(
"clock"
)
.textContent=
new Date()
.toLocaleTimeString();

}

setInterval(
updateClock,
1000
);

updateClock();
'''

build_py = r'''
from pathlib import Path

root = Path(__file__).parent

templates = root / "templates"

html = (
templates /
"desktop.html"
).read_text()

css = (
templates /
"desktop.css"
).read_text()

js = (
templates /
"desktop.js"
).read_text()

final = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>BrainJuiceOS</title>

<style>
{css}
</style>

</head>
<body>

{html}

<script>
{js}
</script>

</body>
</html>
"""

(
root /
"output" /
"BrainJuiceOS.html"
).write_text(
final,
encoding="utf-8"
)

print(
"Built BrainJuiceOS.html"
)
'''

(TEMPLATES / "desktop.html").write_text(
desktop_html,
encoding="utf-8"
)

(TEMPLATES / "desktop.css").write_text(
desktop_css,
encoding="utf-8"
)

(TEMPLATES / "desktop.js").write_text(
desktop_js,
encoding="utf-8"
)

(ROOT / "build.py").write_text(
build_py,
encoding="utf-8"
)

print(
"BrainJuiceOS Part 1 generated."
)
