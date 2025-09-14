package main

import "fmt"

func main() {
    n := 5

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
