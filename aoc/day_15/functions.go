package day15

import (
	"math"
)

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

func getAdjacents(n [2]int) [][2]int {
	i, j := n[0], n[1]
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

func removeByIndex(s [][2]int, i int) [][2]int {
	s[i] = s[len(s)-1]
	return s[:len(s)-1]
}

func removeByValue(s [][2]int, i [2]int) [][2]int {
	for x := range s {
		if s[x] == i {
			s = removeByIndex(s, x)
			break
		}
	}
	return s
}

func getLowestWeight() [2]int {
	lowestVal := math.Inf(0)
	lowestKey := [2]int{-1, -1}
	if len(T) == 1 {
		return T[0]
	}
	for _, k := range T {
		if tmp, ok := weight[k]; ok && float64(tmp) < lowestVal {
			lowestKey = k
			lowestVal = float64(weight[k])
		}
	}
	return lowestKey
}
