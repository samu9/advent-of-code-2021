package day15

import (
	"aoc/utils"
	"math"
)

var input []string = utils.ReadInput("aoc/day_15/input.txt")
var levels [][]int
var previous [][]string
var costs [][]int

var width int
var height int

func buildLevels() {
	levels := make([][]int, len(input))
	for i, line := range input {
		levels[i] = make([]int, len(line))
		for j, l := range line {
			levels[i][j] = int(l - '0')
		}
	}
	width = len(levels[0])
	height = len(levels)
}

func clamp(value int, range_ [2]int) int {
	math.Min(float(value), float)
	min := math.MinInt(value, range_[0])
	return math.MaxInt(min, range_[1])
}

func getAdjacents(i int, j int) [][2]int {
	// for (i:= )
}

func Main() {
	buildLevels()

}
