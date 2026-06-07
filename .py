.os-window{
    position:absolute;
    background:#1e1e1e;
    color:white;
    border-radius:8px;
    overflow:hidden;
    box-shadow:0 0 20px rgba(0,0,0,.5);
}

.window-titlebar{
    height:35px;
    background:#2d2d2d;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 10px;
    cursor:move;
    user-select:none;
}

.window-buttons{
    display:flex;
    gap:4px;
}

.window-buttons button{
    width:28px;
    height:24px;
}

.window-content{
    height:calc(100% - 35px);
    overflow:auto;
    background:#252525;
}

.resize-handle{
    position:absolute;
    right:0;
    bottom:0;
    width:16px;
    height:16px;
    cursor:nwse-resize;
}

.taskbar-app{
    margin:4px;
    padding:4px 12px;
}
