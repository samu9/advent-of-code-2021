const fs = require("fs")
const path = require("path")

const input_ = fs
    .readFileSync(path.join(path.dirname(__filename), "input.txt"), "utf-8")
    .split("\n")

class Coord {
    x: number
    y: number
    constructor(values: number[]) {
        this.x = values[0]
        this.y = values[1]
    }
}

class Segment {
    constructor(public a: Coord, public b: Coord) {}

    applyToMap() {
        let startRow = this.a.x <= this.b.x ? this.a.x : this.b.x
        let endRow = this.a.x <= this.b.x ? this.b.x : this.a.x
        for (let i = startRow; i <= endRow; i++) {
            let startCol = this.a.y <= this.b.y ? this.a.y : this.b.y
            let endCol = this.a.y <= this.b.y ? this.b.y : this.a.y
            for (let j = startCol; j <= endCol; j++) {
                if (`${i}-${j}` in map) {
                    map[`${i}-${j}`]++
                } else {
                    map[`${i}-${j}`] = 1
                }
            }
        }
    }
    apply45DiagonalToMap() {
        let xStep = Math.sign(this.a.x - this.b.x) * -1
        let yStep = Math.sign(this.a.y - this.b.y) * -1
        let start = [this.a.x, this.a.y]
        let end = [this.b.x, this.b.y]
        while (start[0] != end[0] + xStep && start[1] != end[1] + yStep) {
            let i = start[0]
            let j = start[1]
            if (`${i}-${j}` in map) {
                map[`${i}-${j}`]++
            } else {
                map[`${i}-${j}`] = 1
            }
            start[0] += xStep
            start[1] += yStep
        }
    }
    isDiagonal() {
        return this.a.x != this.b.x && this.a.y != this.b.y
    }
    is45Diagonal() {
        return this.a.x - this.b.y == -this.a.y + this.b.x
    }
}

let map: { [key: string]: number } = {}

let segments: Segment[] = []

input_.forEach((v) => {
    let coords: string[] = v.split(" -> ")
    let segment = new Segment(
        new Coord(coords[0].split(",").map((x: string) => parseInt(x))),
        new Coord(coords[1].split(",").map((x: string) => parseInt(x)))
    )
    if (!segment.isDiagonal()) {
        segment.applyToMap()
    } else if (segment.is45Diagonal) {
        segment.apply45DiagonalToMap()
    }
})

console.log(Object.values(map).filter((x) => x > 1).length)

export {}
