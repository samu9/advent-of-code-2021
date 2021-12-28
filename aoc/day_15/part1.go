package day15

import (
	"aoc/utils"
	"fmt"
	"math"
)

var input []string = utils.ReadInput("aoc/day_15/input.txt")
var levels map[[2]int]int
var previous [][]string
var costs [][]int

var width int
var height int

func buildLevels() {
	levels = make(map[[2]int]int)
	for i, line := range input {
		for j, l := range line {
			levels[[2]int{i, j}] = int(l - '0')
		}
	}
	width, height = len(input), len(input)
}

func clamp(value int) int {
	range_ := [2]int{0, width}
	return int(math.Min(math.Max(float64(value), float64(range_[0])), float64(range_[1])))
}

func getAdjacents(i int, j int) [][2]int {
	result := make([][2]int, 0)

	for x := clamp(i - 1); x <= clamp(i+1); x++ {
		if x != i {
			result = append(result, [2]int{x, j})
		}
	}
	for y := clamp(j - 1); y <= clamp(j+1); y++ {
		if y != j {
			result = append(result, [2]int{i, y})
		}
	}

	return result
}

func Main() {
	buildLevels()
	fmt.Println(getAdjacents(99, 100))
	S := [][2]int{{0, 0}}
	T := make([][2]int, 0)

	for i := 1; i < width; i++ {
		for j := 1; j < height; j++ {
			T = append(T, [2]int{i, j})
		}
	}

	f := make(map[[2]int]int)
	J := make(map[[2]int]int)
	f[[2]int{0, 0}] = 0
	J[[2]int{0, 0}] = 0
	adj := getAdjacents(0, 0)

	for _, a := range adj {
		f[a] = levels[a]
		J[a] = 1
	}
	fmt.Println(S, T)
}
