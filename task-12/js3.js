const fs = require("fs");
const n = parseInt(fs.readFileSync("input.txt", "utf-8").trim(), 10);
for (let i = 1; i <= n; i++) {
    let line = "";
    for (let s = 0; s < n - i; s++) {
        line += " ";
    }
    if (i === 1) {
        line += "*";
    } else if (i === n) {
        for (let a = 0; a < 2 * n - 1; a++) {
            line += "*";
        }
    } else {
        line += "*";
        for (let p = 0; p < 2 * i - 3; p++) {
            line += " ";
        }
        line += "*";
    }

    console.log(line);
}
