/**
 * 12/29/2025 - Puzzle 1
 * 
 */

const fs = require('fs');

const input = fs.readFileSync(__dirname + '/input.txt', 'utf-8').trim();

function part1(input: string): number {
    const lines = input.split('\n');
    const directions: string[] = [];

    let numPosZero = 0;
    let currentLoc = 50;

    for (const line of lines) {
        const direction = line[0];
        const movementAmt = parseInt(line.slice(1)) % 100;
        if (direction === 'L') {
            currentLoc -= movementAmt;
        } else {
            currentLoc += movementAmt;
        }

        const oldLoc = currentLoc;
        currentLoc = currentLoc % 100;
        if (currentLoc === 0) {
            numPosZero++;
        }
    }

    return numPosZero;
}

function part2(input: string): number {
    const lines = input.split('\n');
    let numPosZero = 0;
    let currentLoc = 50;

    for (const line of lines) {
        const direction = line[0];
        let movementAmt = parseInt(line.slice(1));
        let step = direction === 'L' ? -1 : 1;

        for (let i = 0; i < movementAmt; i++) {
            currentLoc = (currentLoc + step + 100) % 100;
            if (currentLoc === 0) {
                numPosZero++;
            }
        }
    }

    return numPosZero;
}

console.log('Part 1:', part1(input));
console.log('Part 2:', part2(input));