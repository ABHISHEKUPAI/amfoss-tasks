    let canvas = document.getElementById("myCanvas");
    let ctx = canvas.getContext("2d");
    let dot = document.getElementById("dot");
    let scoreBox = document.getElementById("score");
    let bestBox = document.getElementById("best");
    let errorBox = document.getElementById("error");
    let bestScore = parseFloat(sessionStorage.getItem("bestScore")) || 0;
    let sound = document.getElementById("drawSound");
    let drawing = false;
    let points = [];
    dot.style.left = (canvas.offsetLeft + canvas.width/2) + "px";
    dot.style.top = (canvas.offsetTop + canvas.height/2) + "px";
    bestBox.textContent = "Best Score: " + bestScore.toFixed(1) + "%";

    function handleMouseDown(e)
    {
      drawing = true;
      points = [];
      ctx.clearRect(0,0,canvas.width,canvas.height);
      ctx.beginPath();
      ctx.moveTo(e.offsetX, e.offsetY);
      sound.currentTime = 0;
      sound.play();
    }
    canvas.addEventListener("mousedown",handleMouseDown);

    function handleMouseMove(e)
    {
      if (drawing) {
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.strokeStyle = "white";
        ctx.stroke();
        points.push([e.offsetX, e.offsetY]);
      }
    }
    canvas.addEventListener("mousemove", handleMouseMove);
    
    function Mouseup()
    {
      drawing = false;
      checkCircle();
    }
    canvas.addEventListener("mouseup",Mouseup);

    function checkCircle() {
      if (points.length < 10)
      {
        errorBox.textContent = "Too short! Try again.";
        return;
      }
      errorBox.textContent = "";

      let cx = canvas.width/2;
      let cy = canvas.height/2;
      ctx.beginPath();
      ctx.moveTo(points[0][0], points[0][1]);
      for (let i=1; i<points.length; i++) 
      {
        ctx.lineTo(points[i][0], points[i][1]);
      }
      ctx.closePath();
      if (!ctx.isPointInPath(cx, cy)) 
      {
        errorBox.textContent = "The red dot is not inside your circle!";
        return;
      }
      let dists = points.map(p => {
        let dx = p[0]-cx, dy = p[1]-cy;
        return Math.sqrt(dx*dx + dy*dy);
      });
      let avg = dists.reduce((a,b)=>a+b)/dists.length;
      let avgDiff = dists.map(r=>Math.abs(r-avg)).reduce((a,b)=>a+b)/dists.length; 
      let errorPct = (avgDiff/avg) * 100;
      let score = Math.max(0, 100 - errorPct);

      scoreBox.textContent = "Score: " + score.toFixed(1) + "%";

      if (score > bestScore) {
        bestScore = score;
        sessionStorage.setItem("bestScore", bestScore);
        bestBox.textContent = "Best Score: " + bestScore.toFixed(1) + "%";
      }
      setTimeout(()=>ctx.clearRect(0,0,canvas.width,canvas.height), 700);
    }
    