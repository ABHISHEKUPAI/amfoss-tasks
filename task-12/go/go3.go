package main

import (
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    // Step 1: Read file
    data, err := os.ReadFile("input.txt")
    if err != nil {
        fmt.Println("Error reading input.txt:", err)
        return
    }

    // Step 2: Convert to integer
    content := strings.TrimSpace(string(data))
    n, _ := strconv.Atoi(content)

    // Step 3: Print pyramid
    for i := 1; i <= n; i++ {
        spaces := n - i

        if i == 1 {
            fmt.Println(repeat(" ", spaces) + "*")
        } else if i == n {
            fmt.Println(repeat("*", 2*n-1))
        } else {
            innerSpaces := 2*i - 3
            fmt.Println(repeat(" ", spaces) + "*" + repeat(" ", innerSpaces) + "*")
        }
    }
}

func repeat(s string, count int) string {
    result := ""
    for i := 0; i < count; i++ {
        result += s
    }
    return result
}
