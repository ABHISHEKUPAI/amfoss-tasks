AMFOSS CSS Battle Solutions - README(a brief idea of what i have done ) 

--------------------------------------------------
Task 1: Overlapping Boxes Pattern
--------------------------------------------------
- Used multiple <div> blocks (box1, box2, ..., box8).
- Positioned them with "position: absolute;" and "top/left/right".
- Rounded corners created using "border-radius".
- Key challenge: Aligning left and right blocks so they form a balanced shape.

--------------------------------------------------
Task 2: Bars with Center Block
--------------------------------------------------
- Created vertical red bars on left and right using <div class="bar">.
- A central black rounded rectangle made using another <div>.
- Commands used:
  - position: absolute;
  - width, height for bars and block;
  - border-radius for smooth rounded ends.

--------------------------------------------------
Task 3: Four Rounded Yellow Blocks
--------------------------------------------------
- Background: dark blue.
- Central square + four rounded corner boxes.
- Used border-radius (top-left, bottom-right, etc.) to create circular arcs.
- Important command: border-radius to simulate curved edges.

--------------------------------------------------
Task 4: Ladder-like Red Bars
--------------------------------------------------
- Multiple thin horizontal bars stacked at different "top" positions.
- Placed symmetrically on left and right sides.
- Commands used:
  - width, height for bar size.
  - top, left, right for positioning.
- Key challenge: Precise alignment to look like a pattern.

--------------------------------------------------
Task 5: Wooden Table Shape with Semi-Circles
--------------------------------------------------
- Created base rectangles for the table.
- Added semi-circular shapes using border-radius (top-left and top-right 150px).
- To cut small holes, placed another div with same background color as body.
- Commands used:
  - border-radius (to form half-circles),
  - position: absolute,
  - overlay "cut" divs for holes.

--------------------------------------------------
Key CSS/HTML Commands Used
--------------------------------------------------
- <div> elements for all shapes.
- position: absolute; for precise placement.
- top, left, right for coordinates.
- width, height for dimensions.
- background-color for fills.
- border-radius for circles and rounded edges.

--------------------------------------------------

