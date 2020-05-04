package main

import "fmt"

var number int

func main() {

	fmt.Println("Hello please enter decimal number: ")

	fmt.Scan(&number)

	fmt.Printf("%d binary representation is: %b\n", number, number)

}
