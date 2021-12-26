package day14

import (
	"aoc/utils"
	"fmt"
	"sort"
	"strings"
)

var rules = make(map[string]string)

var steps int = 40

var input []string = utils.ReadInput("aoc/day_14/input.txt")
var pattern string = input[0]

func getBigrams(pattern string) map[string]int {
	bigrams := make(map[string]int, 0)

	for i := range pattern[:len(pattern)-1] {
		bigrams[pattern[i:i+2]]++
	}
	return bigrams
}

func initRules() {
	for _, r := range input[2:] {
		rule := strings.Split(r, " -> ")
		rules[rule[0]] = rule[1]
	}
}

func applyUpdates(bigrams map[string]int, updates map[string]int) {
	for k, v := range updates {
		bigrams[k] += v
	}
}

func Main() {
	bigrams := getBigrams(pattern)

	initRules()

	for i := 0; i < steps; i++ {
		updates := make(map[string]int)

		for k, v := range rules {
			if _, ok := bigrams[k]; !ok {
				continue
			}
			updates[k] -= bigrams[k]
			updates[string(k[0])+v] += bigrams[k]
			updates[v+string(k[1])] += bigrams[k]
		}
		applyUpdates(bigrams, updates)
	}

	occ := make([]int, 0, len(bigrams))

	lettersOcc := make(map[string]int)

	for k, v := range bigrams {
		lettersOcc[string(k[0])] += v

	}

	for _, v := range lettersOcc {
		occ = append(occ, v)

	}
	sort.Ints(occ)
	fmt.Println(occ[len(occ)-1] - occ[0] - 1)
}
