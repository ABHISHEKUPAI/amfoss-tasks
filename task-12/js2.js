let n = 5;
for (let i = 1; i <= n; i++) {
  let line = "";
  for (let s = 0; s < n - i; s++) {
    line += " ";
  }
  if (i === 1) {
    line += "*"; 
  } else if (i === n) {
    for (let k = 0; k < 2 * n - 1; k++) {
      line += "*";
    }
  } else {
    line += "*";
    for (let sp = 0; sp < 2 * i - 3; sp++) {
      line += " ";
    }
    line += "*";
  }

  console.log(line);
}
