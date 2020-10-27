// practice go with basic questions

// PRINT FUNCTIONS

// 10171 print cat
// package main

// import "fmt"

// func main() {
	// fmt.Println("\\    /\\")
	// fmt.Println(" )  ( ')")
	// fmt.Println("(  /  )")
	// fmt.Println(" \\(__)|")

// }

// ================================= //

package main

import (
	"fmt"
	"bufio"
	"os"
	"log"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

func solve(a int, b int) {
	fmt.Println(a+b);
}
