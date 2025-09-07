Circularity Task 

This project is an interactive web app where the user must draw a circle around a red dot on a canvas. 
The app calculates how close the drawing is to a perfect circle and assigns a score.

How it works
1. Input Handling
   - `mousedown`→ Starts drawing, resets old points, and plays a sound.
   - `mousemove`→ Records mouse positions (`[x, y]`) and draws a line on the canvas.
   - `mouseup` → Stops drawing and runs the circle-checking algorithm.

2. Circle Quality Measurement
   - For each point, the distance from the canvas center (`cx, cy`) is calculated.
   - An average radius is computed.
   - The average difference from this radius is measured.
   - Error percentage = `(average difference / average radius) × 100`.
   - Final score = `100 - error percentage` (clamped at 0).

3. Dot Inside Check
   - The red dot must lie inside the path created by the user’s drawing. 
   - If not, the attempt is invalid.

4. Scoring System
   - Current attempt score is shown as Score
   - Best score is stored in sessionStorage and displayed as “Best Score”
   - A reset option can clear the best score.

Most Difficult Parts
- Path Checking (`ctx.isPointInPath`)
  Ensures that the red dot is enclosed by the drawn shape.
  
- Radius Deviation Calculation
  Instead of checking perfect geometry, the algorithm compares every point’s distance to the average radius, making it tolerant but fair.

- Session Storage for Best Score
  Best score persists across page reloads using browser storage:
  js
  sessionStorage.setItem("bestScore", bestScore);

