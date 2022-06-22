package main

import (
	"fmt"
	"math"
)

func main() {
	var x1 float64
	var y1 float64
	var x2 float64
	var y2 float64
	fmt.Print("Enter x coordinate of 1st point: ")
	fmt.Scan(&x1)
	fmt.Print("Enter y coordinate of 1st point: ")
	fmt.Scan(&y1)
	fmt.Print("Enter x coordinate of 2nd point: ")
	fmt.Scan(&x2)
	fmt.Print("Enter y coordinate of 2nd point: ")
	fmt.Scan(&y2)
	x := math.Pow((x2 - x1), 2)
	y := math.Pow((y2 - y1), 2)
	d := math.Sqrt((x + y))
	fmt.Print("distance is ", d)
}
