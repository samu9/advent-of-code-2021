package utils

import (
	"bufio"
	"log"
	"os"
)

func ReadInput(path string) []string {
	file, err := os.Open(path)

	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	result := make([]string, 0)

	for scanner.Scan() {
		result = append(result, scanner.Text())
	}
	return result
}

func ContainsString(str string, list []string) bool {
	for _, l := range list {
		if l == str {
			return true
		}
	}
	return false
}
