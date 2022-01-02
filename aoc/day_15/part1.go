package day15

import (
	"aoc/utils"
	"fmt"
)

var input []string = utils.ReadInput("aoc/day_15/input.txt")
var levels map[[2]int]int
var prev map[[2]int][2]int
var weight map[[2]int]int
var T [][2]int

var width int
var height int

func iteration(n [2]int) {
	adj := getAdjacents(n)

	for _, a := range adj {
		if tmp, ok := weight[a]; levels[a]+weight[n] < tmp || !ok {
			weight[a] = levels[a] + weight[n]
			prev[a] = n
		}
	}
}

func Part1() {
	// initialize
	buildLevels()
	S := [][2]int{{0, 0}}
	T = make([][2]int, 0)

	for i := 0; i < width; i++ {
		for j := 0; j < height; j++ {
			T = append(T, [2]int{i, j})
		}
	}
	T = removeByIndex(T, 0)

	weight = make(map[[2]int]int)
	prev = make(map[[2]int][2]int)

	weight[[2]int{0, 0}] = 0

	adj := getAdjacents([2]int{0, 0})
	for _, a := range adj {
		weight[a] = levels[a] + weight[[2]int{0, 0}]
		fmt.Println(a, weight[a])
		prev[a] = [2]int{0, 0}
	}

	for len(T) > 0 {
		u := getLowestWeight()

		iteration(u)
		T = removeByValue(T, u)
		S = append(S, u)
	}
	fmt.Println(weight[[2]int{99, 99}])
}
