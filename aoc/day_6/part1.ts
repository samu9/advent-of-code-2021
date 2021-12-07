const fs = require("fs")
const path = require("path")

const input_: string[] = fs
    .readFileSync(path.join(path.dirname(__filename), "input.txt"), "utf-8")
    .split(",")

const CYCLE_DAYS = 6
const DAYS = 80

let lanternfishes: number[] = input_.map((i) => parseInt(i))

for (const i of Array(DAYS).keys()) {
    let sons = 0
    for (let j in lanternfishes) {
        lanternfishes[j]--
        if (lanternfishes[j] == 0) {
            sons++
            lanternfishes[j] = CYCLE_DAYS
        }
    }
    lanternfishes.push(...Array(sons).fill(CYCLE_DAYS + 2))
}

console.log(lanternfishes.length)

export {}
