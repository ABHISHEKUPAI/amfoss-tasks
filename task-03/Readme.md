How i approached the task:-

i learned 
          HTML by referring :-https://www.youtube.com/watch?v=HcOc7P5BMi4
          css by teferring :-https://www.youtube.com/watch?v=wRNinF7YQqQ
          js by reffering :-https://www.youtube.com/watch?v=ajdRvxDWH4w&list=PLGjplNEQ1it_oTvuLRNqXfz_v_0pq6unW(didnt go through everything in this video but went through some parts)
          canvas api by referring :- https://www.youtube.com/watch?v=gm1QtePAYTM
how i wrote the codes 
          
first was setting up of html part as that was what i learned first . initially i drew the outlay of the web page sort of in a paper and then wrote the codes .
then i took css as it was the second easiest part and i started giving color to canvas and edited the stiles of letter after that beautification was done in an overall sense as i enjoyed a bit and really liked experimenting it .Then came a bit difficult but main part the one and only js. 
JAVASCRIPT PART interesting but most time consuming so here is what i learned :-

analyzed what must happen when my code ran 
ie 

[THE BEGINNING] 

when user clicks the mouse for the first time (MouseDown) must get activated . previous points and the canvas drawings must be cleared and the pen (ctx) used for drawing in the canvas align with the mouse pointer and in the same time sound must be played .

[INTERMEDIATE]

once MouseDown activates after that MouseMove must activate which is based on drawing micro lines btw 2 points that user moves his/her mouse in order to draw a circle 

[END SORT OF]

MouseaUp comes into play once user completes the drawing 

[ACTUAL END]

correctness of circle :-
step 1 we analyze the points distance from the center ie the red dot by using Pythagoras theorem (a^2+b^2= c^2) 
 
this is that part of the code 

let dists = points.map(p => {
        let dx = p[0]-cx, dy = p[1]-cy;
        return Math.sqrt(dx*dx + dy*dy);
then each of the value of length obtained is summed up and then divided by number of values and stored under avg .now each value of the distence is substracted by avg value and then stored under avgdiff .now to get percentage value we divide avgdiff by avg value then multiply it by 100 .

this was the most important parts of the entire program and the method i followed to complete it .

A bit more in depth 

1]  let canvas = document.getElementById("myCanvas");
    let ctx = canvas.getContext("2d");
    let dot = document.getElementById("dot");
    let scoreBox = document.getElementById("score");
    let bestBox = document.getElementById("best");
    let errorBox = document.getElementById("error");
    let bestScore = parseFloat(sessionStorage.getItem("bestScore")) || 0;
    let sound = document.getElementById("drawSound");
    let drawing = false;
    let points = [];

let <smt> = <smt else> is format of declairing a varible like (int x = 5; in c) for js  

2]  dot.style.left = (canvas.offsetLeft + canvas.width/2) + "px";
    dot.style.top = (canvas.offsetTop + canvas.height/2) + "px";
    bestBox.textContent = "Best Score: " + bestScore.toFixed(1) + "%";
    
dot.style.left is for altering the dot from left part of the window 
canvas.offsetLeft is the distance of canvas end from the left part of window 
canvas.width/2 is the value equavelent to half of the width of canvas 
now why this comand is executed is because the dot must be positoned in the centre of canvas so that distance from the left end is = to the distance of canvas end from the left part of window + canvaswidth/2

same thing goes with other line below this one

bestBox.textContent → sets the text inside an element called bestBox."Best Score: " → is a plain string.bestScore.toFixed(1) → formats the number bestScore so it always shows one decimal place (e.g., 87.4 instead of 87.43214)."%" → appends a percentage sign at the end.

3] now to mousedown function 

why we set drawing = true the reason is this its usually a flag to indicate that the user has started drawing (holding down the mouse).Later, when drawing is checked in mousemove or mouseup, the program knows whether it should continue drawing or stop.

4] 
points = [];
Resets the points array to empty.used to store all (x, y) positions of the mouse while drawing.

5] 
ctx.clearRect(0, 0, canvas.width, canvas.height);Clears the entire canvas.(0, 0) → top left corner of canvas.(canvas.width, canvas.height) → entire width and height.This ensures that every new drawing starts on a blank canvas

6] 
ctx.beginPath();
Tells the canvas: “Start a new path.”It’s like lifting a pen and putting it down again to start fresh.

7] 
ctx.moveTo(e.offsetX, e.offsetY);Moves the drawing cursor to the mouse position where the click happened. e.offsetX and e.offsetY → mouse coordinates relative to the canvas.

8] 
sound.currentTime = 0;
Resets the audio playback to the start (0 seconds).

9] 
sound.play();
Plays the sound effect.

10] 
the little e is called event object It’s like a package of information about the mouse event that just happened.

11] 
canvas.addEventListener("mousemove", handleMouseMove)

.addEventListener("mousemove", ...) → tells the browser: “Whenever the mouse moves over this canvas, run the function I give you.”
"mousemove" → the event type (fires every time the mouse moves while inside the canvas).
handleMouse → the function that will run each time the event happens.
The browser automatically passes the event object (e) into handleMouse, just like with mousedown.

12]
function checkCircle() {

function — declares a function.
checkCircle — function name.
() — parameter list (empty here: no parameters).
{ — start the function body.
if (points.length < 10) {
if — conditional statement.
points.length — .length property of the points array (number of entries).
< 10 — comparison operator (true if fewer than 10).
( ) — enclosing the condition.
{ — start of the if block.

13]
errorBox.textContent = "Too short! Try again.";

errorBox — a DOM element reference.Document Object Model A DOM element is basically a piece of your webpage (like a tag in HTML) that JavaScript can directly interact with.
.textContent — DOM property that sets the element’s visible text (plain text).
; — statement terminator.
return — immediately exit the function. (Nothing returned because no value specified.
errorBox.textContent = "";
Clear any previous error message by setting text to an empty string.
ctx — 2D canvas context.
.beginPath() — starts a new path (so old strokes don’t connect).

14]
ctx.moveTo(points[0][0], points[0][1]);

points[0] — first item in points (assumed [x, y]).
points[0][0] and points[0][1] — x and y of first point.
ctx.moveTo(x, y) — move the drawing cursor to this point (without drawing).

15]
ctx.lineTo(points[i][0], points[i][1]);

ctx.lineTo(x,y) — add a straight line from current path position to the given point. Repeats to build the path.
closes the for loop.
ctx.closePath();
Closes the path (draws a straight line from last point back to start).

16]
if (!ctx.isPointInPath(cx, cy)) 

ctx.isPointInPath(x, y) — returns true if the point (x,y) is inside the current path.
! — logical NOT operator (negates the boolean). So this condition is true when the center is not inside the drawn path.

17]

let dists = points.map(p => {

points.map(...) — creates a new array by calling the provided function for each element of points.
p => { ... } — an arrow function (parameter p, block body). p is each point (likely [x,y]).
let dx = p[0]-cx, dy = p[1]-cy;
let dx = ... , dy = ...; — multiple variable declarations separated by comma.
p[0]-cx — horizontal difference between point’s x and center x.
p[1]-cy — vertical difference.
return Math.sqrt(dx*dx + dy*dy);
Math.sqrt(...) — square root.
dx*dx + dy*dy — squared distance from center (Pythagoras).
closes the map call; dists becomes an array of distances from center for all points.

18]
let avg = dists.reduce((a,b)=>a+b)/dists.length;

dists.reduce((a,b)=>a+b) — reduce combines array elements by repeatedly calling the function; here it sums all distances.
(a,b)=>a+b — arrow function with expression body (implicit return). First call: a starts as first element, b second.
/ dists.length — divide sum by count → arithmetic mean (average).

Note: reduce with no initial value is safe here because dists.length >= 10.

19]
let avgDiff = dists.map(r=>Math.abs(r-avg)).reduce((a,b)=>a+b)/dists.length;

dists.map(r => Math.abs(r-avg)) — for each distance r, compute absolute deviation from the mean.
.reduce((a,b)=>a+b) — sum those absolute deviations.
Math.abs(...) — absolute value.
avgDiff/avg — fraction relative to average radius.

* 100 — convert to percentage.

20]

let score = Math.max(0, 100 - errorPct);

100 - errorPct — higher error means lower score.
Math.max(0, ...) — ensure score never drops below zero.

21]

scoreBox.textContent = "Score: " + score.toFixed(1) + "%";

score.toFixed(1) — format number to one decimal place (returns a string).
"Score: " + ... + "%" — string concatenation using +.
Assign to scoreBox.textContent to display.

22]

if (score > bestScore) {
If this run’s score is better than the stored bestScore.
bestScore = score;
update the bestScore variable.

23]

sessionStorage.setItem("bestScore", bestScore);

sessionStorage — browser storage that lasts for the page session (cleared when tab/window closes).
.setItem(key, value) — store a key/value pair. Note: values are stored as strings (the number is converted to string).
bestBox.textContent = "Best Score: " + bestScore.toFixed(1) + "%";
update the displayed best score.
close if (score > bestScore).

24]

setTimeout(()=>ctx.clearRect(0,0,canvas.width,canvas.height), 700);
setTimeout(callback, delay) — schedule callback to run after delay milliseconds.
()=>ctx.clearRect(...) — arrow function used as callback. Because it's a single expression, it implicitly returns the expression result (not used here).
ctx.clearRect(0,0,canvas.width,canvas.height) — clears the whole canvas (x=0, y=0, width, height).
700 — delay in milliseconds (0.7 seconds).

Short glossary of important syntax used above

function name(...) { ... } — define a function.

if (cond) { ... } / return — conditional and early exit.

let — block-scoped variable. (const would be read-only.)

. — property access (e.g., array.length, obj.prop).

[] — array indexing (points[0][1]).

for (init; cond; inc) { } — standard for-loop.

=> — arrow function. Two forms:

x => x*2 (concise body, implicit return)

x => { return x*2; } (block body, explicit return)

.map(fn) — makes a new array by applying fn to each element.

.reduce(fn) — reduces the array to a single value by combining elements.

Math.sqrt, Math.abs, Math.max — standard math helpers.

string + value — string concatenation.

toFixed(n) — format number to n decimal places (returns string).

sessionStorage.setItem(key, value) — store data for this browser session.

setTimeout(fn, ms) — run fn after ms milliseconds.
