from pathlib import Path

html = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BrainJuiceOS</title>

<style>

html,body{
    margin:0;
    width:100%;
    height:100%;
    overflow:hidden;
    font-family:Segoe UI,sans-serif;
}

body{
    background:#111;
}

/* Boot */

#boot{
    position:fixed;
    inset:0;
    background:black;
    color:#00ff88;
    font-family:Consolas,monospace;
    padding:20px;
    z-index:9999;
}

/* Login */

#login{
    position:fixed;
    inset:0;
    display:none;
    align-items:center;
    justify-content:center;
    background:linear-gradient(135deg,#111,#222,#333);
}

.login-box{
    width:350px;
    background:#1f1f1f;
    padding:20px;
    border-radius:10px;
    color:white;
}

.login-box input{
    width:100%;
    padding:10px;
    margin-top:10px;
    box-sizing:border-box;
}

/* Desktop */

#desktop{
    display:none;
    position:fixed;
    inset:0;
    background:linear-gradient(
        45deg,
        #0d1b2a,
        #1b263b,
        #415a77
    );
}

/* Dock */

#dock{
    position:absolute;
    left:0;
    top:0;
    bottom:40px;
    width:64px;
    background:rgba(0,0,0,.4);
}

.dock-btn{
    height:50px;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    color:white;
}

/* Desktop Icons */

#icons{
    margin-left:80px;
    margin-top:20px;
}

.icon{
    width:80px;
    color:white;
    text-align:center;
    margin-bottom:20px;
    cursor:pointer;
}

/* Windows */

#windows{
    position:absolute;
    inset:0;
}

.window{
    position:absolute;
    width:700px;
    height:500px;
    left:120px;
    top:60px;
    background:#1e1e1e;
    color:white;
    border-radius:8px;
    overflow:hidden;
    box-shadow:0 0 20px rgba(0,0,0,.5);
}

.titlebar{
    height:35px;
    background:#2d2d2d;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 10px;
}

.content{
    height:calc(100% - 35px);
    overflow:auto;
}

/* Taskbar */

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

#start{
    width:100px;
    height:100%;
}

#tasks{
    flex:1;
}

#clock{
    width:120px;
    text-align:center;
    color:white;
}

/* Start Menu */

#startMenu{
    position:absolute;
    left:0;
    bottom:40px;
    width:280px;
    height:400px;
    background:#1d1d1d;
    color:white;
    display:none;
}

.start-item{
    padding:10px;
    cursor:pointer;
}

.start-item:hover{
    background:#333;
}

</style>
</head>
<body>

<div id="boot">
BrainJuiceOS Booting...
</div>

<div id="login">
<div class="login-box">
<h2>BrainJuiceOS</h2>
<input id="user" value="admin">
<input id="pass" type="password" value="brainjuice">
<button onclick="login()">Login</button>
</div>
</div>

<div id="desktop">

<div id="dock">
<div class="dock-btn" onclick="openBrowser()">🌐</div>
<div class="dock-btn" onclick="openTerminal()">⌨️</div>
<div class="dock-btn" onclick="openFiles()">📁</div>
<div class="dock-btn" onclick="openSettings()">⚙️</div>
<div class="dock-btn" onclick="openStore()">🛒</div>
</div>

<div id="icons">
<div class="icon" ondblclick="openBrowser()">🌐<br>Browser</div>
<div class="icon" ondblclick="openTerminal()">⌨️<br>Terminal</div>
<div class="icon" ondblclick="openFiles()">📁<br>Files</div>
</div>

<div id="windows"></div>

<div id="startMenu">
<div class="start-item" onclick="openBrowser()">Browser</div>
<div class="start-item" onclick="openTerminal()">Terminal</div>
<div class="start-item" onclick="openFiles()">Files</div>
<div class="start-item" onclick="openSettings()">Settings</div>
<div class="start-item" onclick="openStore()">App Store</div>
</div>

<div id="taskbar">
<button id="start">Start</button>
<div id="tasks"></div>
<div id="clock"></div>
</div>

</div>

<script>

setTimeout(()=>{
    boot.style.display="none";
    login.style.display="flex";
},2000);

function login(){
    if(
        user.value==="admin" &&
        pass.value==="brainjuice"
    ){
        login.style.display="none";
        desktop.style.display="block";
    }
}

start.onclick=()=>{
    startMenu.style.display =
        startMenu.style.display==="block"
        ? "none"
        : "block";
};

function updateClock(){
    clock.textContent =
        new Date().toLocaleTimeString();
}
setInterval(updateClock,1000);
updateClock();

function createWindow(title,html){

    const win =
    document.createElement("div");

    win.className="window";

    win.innerHTML=`
        <div class="titlebar">
            <span>${title}</span>
            <button onclick="this.closest('.window').remove()">X</button>
        </div>
        <div class="content">
            ${html}
        </div>
    `;

    windows.appendChild(win);
}

function openBrowser(){
    createWindow(
        "Browser",
        "<h2>Browser Foundation</h2>"
    );
}

function openTerminal(){
    createWindow(
        "Terminal",
        "<pre>BrainJuice Terminal</pre>"
    );
}

function openFiles(){
    createWindow(
        "Files",
        "<ul><li>Desktop</li><li>Documents</li></ul>"
    );
}

function openSettings(){
    createWindow(
        "Settings",
        "<button onclick='localStorage.clear()'>Reset Storage</button>"
    );
}

function openStore(){
    createWindow(
        "App Store",
        "<p>GitHub app support coming later.</p>"
    );
}

</script>

</body>
</html>
"""

Path("BrainJuiceOS.html").write_text(html, encoding="utf-8")

print("Created BrainJuiceOS.html")
