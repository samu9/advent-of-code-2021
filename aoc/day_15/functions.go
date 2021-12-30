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

func removeByValue(s [][2]int, i [2]int) ([][2]int, bool) {
	found := false
	for x := range s {
		if s[x] == i {
			s = removeByIndex(s, x)
			found = true
			break
		}
	}
	return s, found
}

func getLowestWeight() [2]int {
	lowestVal := -1
	lowestKey := [2]int{-1, -1}
	if len(T) == 1 {
		return T[0]
	}
	for _, k := range T {
		if weight[k] < lowestVal || (lowestVal == -1 && weight[k] != -1) {
			lowestKey = k
			lowestVal = weight[k]
		}
	}
	return lowestKey
}
