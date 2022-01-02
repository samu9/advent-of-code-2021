package day15

import (
	"fmt"
)

const MAP_SIZE = 5

func getRisk(pos [2]int) int {
	tile_width := width / MAP_SIZE
	tile_height := height / MAP_SIZE
	y := pos[0] % tile_height
	x := pos[1] % tile_width
	reps := (pos[0] / tile_height) + (pos[1] / tile_width)
	level := levels[[2]int{y, x}]
	risk := ((level + reps) % 9)

	if risk == 0 {
		risk = 9
	}
	return risk
}

var weightsQueue = make([][2]int, 0)
var lowestKey = [2]int{-1, -1}

func setWeight(key [2]int, val int) {
	for i, w := range weightsQueue {
		if val < weight[w] {
			weightsQueue = append(weightsQueue[:i+1], weightsQueue[i:]...)
			weightsQueue[i] = key
			weight[key] = val
			return
		}
	}
	weightsQueue = append(weightsQueue, key)
	weight[key] = val

}

// func removeNode(key [2]int){

// }

func Main() {
	buildLevels()
	width *= MAP_SIZE
	height *= MAP_SIZE

	S := [][2]int{{0, 0}}
	T = make([][2]int, 0)

	for i := 0; i < height; i++ {
		for j := 0; j < width; j++ {
			T = append(T, [2]int{i, j})
		}
	}
	T = removeByIndex(T, 0)

	weight = make(map[[2]int]int)

	prev = make(map[[2]int][2]int)

	setWeight([2]int{0, 0}, 0)

	adj := getAdjacents([2]int{0, 0})
	for _, a := range adj {
		setWeight(a, getRisk(a)+weight[[2]int{0, 0}])
		// weight[a] = getRisk(a) + weight[[2]int{0, 0}]
		prev[a] = [2]int{0, 0}
	}
	weightsQueue = weightsQueue[1:]

	for len(T) > 0 {
		fmt.Println(len(T), "remaining")
		// u := getLowestWeight()
		u := weightsQueue[0]

		adj := getAdjacents(u)

		for _, a := range adj {
			if tmp, ok := weight[a]; getRisk(a)+weight[u] < tmp || !ok {
				setWeight(a, getRisk(a)+weight[u])
				prev[a] = u
			}
		}
		weightsQueue = weightsQueue[1:]
		T = removeByValue(T, u)
		S = append(S, u)
	}
	fmt.Println(weight[[2]int{height - 1, width - 1}])

	// getRisk([2]int{21, 12})
}
