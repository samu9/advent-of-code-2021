package day14

import (
	"aoc/utils"
	"strings"
)

var rules = make(map[string]string)

var steps int = 40
var occurs = make(map[string]int)

var input []string = utils.ReadInput("aoc/day_14/input.txt")
var pattern string = input[0]

func getBigrams(pattern string) map[string]int {
	bigrams := make(map[string]int, 0)

	for i := range pattern[:len(pattern)-1] {
		if _, ok := bigrams[pattern[i:i+2]]; ok {
			bigrams[pattern[i:i+2]]++
		} else {
			bigrams[pattern[i:i+2]] = 1
		}
	}
	return bigrams
}

func initRules() {
	for _, r := range input[2:] {
		rule := strings.Split(r, " -> ")
		rules[rule[0]] = rule[1]
	}
}

func mergeBigrams(bigrams []string) string {
	result := make([]string, 0, len(bigrams)+1)

	result = append(result, bigrams[0])

	for _, b := range bigrams[1:] {
		result = append(result, b[1:])
	}
	return strings.Join(result, "")
}

// func Main2() {
// 	input := utils.ReadInput("aoc/day_14/input.txt")

// 	pattern := input[0]

// 	rules := input[2:]

// 	steps := 15
// 	for i := 0; i < steps; i++ {
// 		fmt.Println(i, len(pattern))
// 		rules_applied := 0
// 		bigrams := getBigrams(pattern)

// 		for _, r := range rules {
// 			rule := strings.Split(r, " -> ")
// 			if strings.Contains(pattern, rule[0]) {
// 				startIndex := 0
// 				for strings.Count(pattern[startIndex:], rule[0]) > 0 {
// 					index := strings.Index(pattern[startIndex:], rule[0]) + startIndex
// 					bigrams[index] = string(bigrams[index][0]) + rule[1] + string(bigrams[index][1])
// 					rules_applied++

// 					startIndex = index + 1
// 				}
// 				// fmt.Println(rule[0], strings.Count(pattern, rule[0]))

// 			}
// 		}

// 		pattern = mergeBigrams(bigrams)
// 		// fmt.Println(pattern)
// 	}
// 	occurs := make(map[rune]int)
// 	for _, s := range pattern {
// 		if _, ok := occurs[s]; ok {
// 			occurs[s]++
// 		} else {
// 			occurs[s] = 1
// 		}
// 	}

// 	results := make([]int, 0, len(occurs))
// 	for _, v := range occurs {
// 		results = append(results, v)
// 	}
// 	sort.Ints(results)
// 	fmt.Println(results[len(results)-1] - results[0])
// }

// func Main3() {
// 	initRules()

// 	//init occurs
// 	for _, p := range pattern {
// 		if _, ok := occurs[string(p)]; ok {
// 			occurs[string(p)]++
// 		} else {
// 			occurs[string(p)] = 1
// 		}
// 	}

// 	// bigrams := getBigrams(pattern)

// 	// for _, b := range bigrams {

// 	// 	// nextStep(b, 0)
// 	// }
// 	results := make([]int, 0, len(occurs))
// 	for _, v := range occurs {
// 		results = append(results, v)
// 	}
// 	sort.Ints(results)
// 	fmt.Println(results[len(results)-1] - results[0])
// }

// func nextStep(bigram string, step int) {
// 	if _, ok := rules[bigram]; !ok || step == steps {
// 		// fmt.Println("ending", bigram, "step", step)
// 		return
// 	}

// 	char := rules[bigram]

// 	if _, ok := occurs[char]; ok {
// 		occurs[char]++
// 	} else {
// 		occurs[char] = 1
// 	}
// 	nextStep(string(bigram[0])+string(char), step+1)
// 	nextStep(string(char)+string(bigram[1]), step+1)

// }

func applyUpdates(bigrams map[string]int, updates map[string]int) {
	for k, v := range updates {
		if _, ok := bigrams[k]; ok {
			bigrams[k] += v
		} else {
			bigrams[k] = v
		}
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
			updates[k] = -bigrams[k]
			updates[string(k[0])+v] = bigrams[k]
			updates[v+string(k[1])] = bigrams[k]
		}
		applyUpdates(bigrams, updates)
	}
}
